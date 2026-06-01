"""Structured, append-only run logging.

No global ``logging`` config is mutated -- callers hold an explicit
:class:`RunLogger` bound to a run directory. Each JSONL line is self-contained.
"""

from __future__ import annotations

import json
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

from .score import ValidationResult


def _now() -> str:
    return datetime.now(timezone.utc).isoformat()


def jsonl_append(path: Path, record: dict[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("a", encoding="utf-8") as fh:
        fh.write(json.dumps(record, default=str) + "\n")


class RunLogger:
    """Writes tool_calls.jsonl, validator_calls.jsonl, events.jsonl, transcript.md."""

    def __init__(self, run_dir: str | Path) -> None:
        self.run_dir = Path(run_dir)
        self.run_dir.mkdir(parents=True, exist_ok=True)

    def log_tool_call(
        self,
        tool: str,
        args: dict[str, Any],
        result: dict[str, Any],
        *,
        ok: bool,
        duration_s: float,
        seed: int | None = None,
    ) -> None:
        jsonl_append(
            self.run_dir / "tool_calls.jsonl",
            {
                "ts": _now(),
                "tool": tool,
                "ok": ok,
                "duration_s": duration_s,
                "seed": seed,
                "args": args,
                "result": result,
            },
        )

    def log_validator_call(
        self,
        validator: str,
        problem_id: str,
        result: ValidationResult,
        duration_s: float,
    ) -> None:
        jsonl_append(
            self.run_dir / "validator_calls.jsonl",
            {
                "ts": _now(),
                "validator": validator,
                "problem_id": problem_id,
                "duration_s": duration_s,
                "result": result.to_dict(),
            },
        )

    def event(self, kind: str, **fields: Any) -> None:
        jsonl_append(self.run_dir / "events.jsonl", {"ts": _now(), "kind": kind, **fields})

    def transcript(self, section: str, body: str) -> None:
        path = self.run_dir / "transcript.md"
        path.parent.mkdir(parents=True, exist_ok=True)
        with path.open("a", encoding="utf-8") as fh:
            fh.write(f"\n## {section}\n\n{body}\n")
