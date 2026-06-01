"""Track candidate files and their best-known scores for a problem."""

from __future__ import annotations

from pathlib import Path

from ._jsonl_store import JsonlStore


class CandidateStore(JsonlStore):
    def __init__(self, problem_dir: str | Path) -> None:
        super().__init__(Path(problem_dir) / "candidates" / "candidate_index.jsonl")

    def record(self, candidate_path: str, passed: bool, objective_value=None, **extra) -> None:
        self.append(
            {
                "candidate_path": candidate_path,
                "passed": passed,
                "objective_value": objective_value,
                **extra,
            }
        )
