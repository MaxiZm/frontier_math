"""Run candidate code in an isolated subprocess with a wall-clock timeout.

Pure-Python; docker is optional. Output crosses the boundary as JSON only.
"""

from __future__ import annotations

import json
import subprocess
import sys
import time
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any

from ..core.candidate import Candidate
from ..core.exceptions import SandboxExecutionError, SandboxTimeout
from ..core.problem import Problem
from ._runner_shim import SENTINEL


@dataclass(slots=True)
class SandboxResult:
    ok: bool
    output: Any = None
    stdout: str = ""
    stderr: str = ""
    duration_s: float = 0.0
    timed_out: bool = False
    returncode: int | None = None
    error: str = ""
    details: dict[str, Any] = field(default_factory=dict)


def run_candidate(
    candidate: Candidate,
    problem: Problem | None = None,
    *,
    timeout_s: float | None = None,
    args: tuple = (),
    kwargs: dict[str, Any] | None = None,
    cpu_seconds: int | None = None,
    memory_mb: int | None = None,
    raise_on_timeout: bool = False,
) -> SandboxResult:
    """Execute ``candidate``'s entrypoint in a subprocess and capture its output."""
    if timeout_s is None:
        timeout_s = problem.validator.timeout_seconds if problem else 30.0

    request = {
        "file": str(Path(candidate.path).resolve()),
        "function_name": candidate.function_name,
        "args": list(args),
        "kwargs": kwargs or {},
        "cpu_seconds": cpu_seconds,
        "memory_mb": memory_mb,
    }

    cmd = [sys.executable, "-m", "math_harness.validators._runner_shim"]
    start = time.perf_counter()
    try:
        proc = subprocess.run(
            cmd,
            input=json.dumps(request),
            capture_output=True,
            text=True,
            timeout=timeout_s,
        )
    except subprocess.TimeoutExpired as exc:
        duration = time.perf_counter() - start
        if raise_on_timeout:
            raise SandboxTimeout(
                f"Candidate exceeded {timeout_s}s time budget."
            ) from exc
        return SandboxResult(
            ok=False,
            timed_out=True,
            duration_s=duration,
            stderr=(exc.stderr or "") if isinstance(exc.stderr, str) else "",
            error=f"timeout after {timeout_s}s",
        )

    duration = time.perf_counter() - start
    stdout = proc.stdout or ""
    payload: dict[str, Any] = {}
    if SENTINEL in stdout:
        pre, _, raw = stdout.partition(SENTINEL)
        stdout_clean = pre
        try:
            payload = json.loads(raw)
        except json.JSONDecodeError:  # pragma: no cover - defensive
            payload = {"ok": False, "error": "could not decode sandbox payload"}
    else:
        stdout_clean = stdout
        payload = {
            "ok": False,
            "error": "sandbox produced no result payload",
        }

    result = SandboxResult(
        ok=bool(payload.get("ok")),
        output=payload.get("output"),
        stdout=stdout_clean,
        stderr=proc.stderr or "",
        duration_s=duration,
        returncode=proc.returncode,
        error=payload.get("error", ""),
        details={k: v for k, v in payload.items() if k not in {"ok", "output", "error"}},
    )
    return result


def require_output(result: SandboxResult) -> Any:
    """Return the candidate output or raise a structured sandbox error."""
    if result.timed_out:
        raise SandboxTimeout(result.error or "candidate timed out")
    if not result.ok:
        raise SandboxExecutionError(result.error or "candidate failed in sandbox")
    return result.output
