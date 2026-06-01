"""Chronological log of attempts at a problem."""

from __future__ import annotations

from pathlib import Path

from ._jsonl_store import JsonlStore


class AttemptLog(JsonlStore):
    def __init__(self, problem_dir: str | Path) -> None:
        super().__init__(Path(problem_dir) / "notes" / "attempt_log.jsonl")

    def record(self, level: int, idea: str, result: str, **extra) -> None:
        self.append({"level": level, "idea": idea, "result": result, **extra})
