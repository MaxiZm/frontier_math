"""Subprocess child that executes a candidate entrypoint in isolation.

Protocol: read a JSON request from stdin::

    {"file": ..., "function_name": ..., "args": [...], "kwargs": {...},
     "cpu_seconds": int|null, "memory_mb": int|null}

Apply best-effort POSIX resource limits, import the candidate file, call the
entrypoint, then print ``SENTINEL`` followed by a JSON response on stdout.
Output is JSON only (never pickle) to keep the trust boundary safe.
"""

from __future__ import annotations

import importlib.util
import json
import sys
import traceback

SENTINEL = "<<<MH_RESULT>>>"


def _apply_limits(cpu_seconds, memory_mb) -> None:
    try:
        import resource  # POSIX only
    except ImportError:  # pragma: no cover - non-POSIX
        return
    if cpu_seconds:
        try:
            resource.setrlimit(resource.RLIMIT_CPU, (int(cpu_seconds), int(cpu_seconds) + 1))
        except (ValueError, OSError):  # pragma: no cover - best effort
            pass
    if memory_mb:
        try:
            nbytes = int(memory_mb) * 1024 * 1024
            resource.setrlimit(resource.RLIMIT_AS, (nbytes, nbytes))
        except (ValueError, OSError):  # pragma: no cover - best effort
            pass


def _json_safe(value):
    """Coerce arbitrary return values into JSON-serializable form."""
    try:
        json.dumps(value)
        return value, False
    except (TypeError, ValueError):
        return repr(value), True


def main() -> int:
    raw = sys.stdin.read()
    try:
        req = json.loads(raw)
    except json.JSONDecodeError as exc:  # pragma: no cover - defensive
        sys.stdout.write(SENTINEL + json.dumps({"ok": False, "error": f"bad request: {exc}"}))
        return 1

    _apply_limits(req.get("cpu_seconds"), req.get("memory_mb"))

    try:
        spec = importlib.util.spec_from_file_location("mh_sandboxed_candidate", req["file"])
        module = importlib.util.module_from_spec(spec)  # type: ignore[arg-type]
        spec.loader.exec_module(module)  # type: ignore[union-attr]
        fn = getattr(module, req["function_name"])
        output = fn(*req.get("args", []), **req.get("kwargs", {}))
        safe, non_json = _json_safe(output)
        payload = {"ok": True, "output": safe, "non_json": non_json}
    except Exception as exc:  # noqa: BLE001
        payload = {
            "ok": False,
            "error": f"{type(exc).__name__}: {exc}",
            "traceback": traceback.format_exc(),
        }

    sys.stdout.write(SENTINEL + json.dumps(payload, default=str))
    sys.stdout.flush()
    return 0 if payload.get("ok") else 1


if __name__ == "__main__":
    raise SystemExit(main())
