"""Store dead ends so they are not re-tried (docs: save every useful failed path)."""

from __future__ import annotations

from pathlib import Path

from ._jsonl_store import JsonlStore


class FailedPaths(JsonlStore):
    def __init__(self, problem_dir: str | Path) -> None:
        super().__init__(Path(problem_dir) / "notes" / "failed_paths.jsonl")

    def record(self, approach: str, why_failed: str, **extra) -> None:
        self.append({"approach": approach, "why_failed": why_failed, **extra})
