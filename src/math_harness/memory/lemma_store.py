"""Store reusable lemmas / heuristics extracted during a run."""

from __future__ import annotations

from pathlib import Path

from ._jsonl_store import JsonlStore


class LemmaStore(JsonlStore):
    def __init__(self, problem_dir: str | Path) -> None:
        super().__init__(Path(problem_dir) / "notes" / "lemmas.jsonl")

    def record(self, statement: str, justification: str = "", **extra) -> None:
        self.append({"statement": statement, "justification": justification, **extra})
