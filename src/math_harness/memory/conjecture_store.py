"""Store conjectures / patterns inferred from computational examples."""

from __future__ import annotations

from pathlib import Path

from ._jsonl_store import JsonlStore


class ConjectureStore(JsonlStore):
    def __init__(self, problem_dir: str | Path) -> None:
        super().__init__(Path(problem_dir) / "notes" / "conjectures.jsonl")

    def record(self, statement: str, evidence: str = "", status: str = "open", **extra) -> None:
        self.append({"statement": statement, "evidence": evidence, "status": status, **extra})
