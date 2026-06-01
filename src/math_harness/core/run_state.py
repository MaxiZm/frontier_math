"""Run state: ladder level, attempts, best candidate/score, persisted to run.json."""

from __future__ import annotations

import json
import os
from dataclasses import dataclass, field
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

from .exceptions import RunStateError
from .problem import Problem
from .score import ValidationResult, better_result


def _now() -> str:
    return datetime.now(timezone.utc).isoformat()


@dataclass(slots=True)
class Attempt:
    index: int
    candidate_path: str
    result: ValidationResult
    level: int = 0
    timestamp: str = field(default_factory=_now)

    def to_dict(self) -> dict[str, Any]:
        return {
            "index": self.index,
            "candidate_path": self.candidate_path,
            "level": self.level,
            "timestamp": self.timestamp,
            "result": self.result.to_dict(),
        }

    @classmethod
    def from_dict(cls, d: dict[str, Any]) -> "Attempt":
        return cls(
            index=d["index"],
            candidate_path=d["candidate_path"],
            result=ValidationResult.from_dict(d["result"]),
            level=d.get("level", 0),
            timestamp=d.get("timestamp", _now()),
        )


@dataclass(slots=True)
class RunState:
    problem_id: str
    run_dir: Path
    ladder_level: int = 0
    attempts: list[Attempt] = field(default_factory=list)
    best_result: ValidationResult | None = None
    best_candidate_path: str | None = None
    objective_direction: str | None = None
    status: str = "in_progress"  # in_progress | passed | failed | error

    @classmethod
    def new(cls, problem: Problem, run_dir: str | Path) -> "RunState":
        return cls(
            problem_id=problem.id,
            run_dir=Path(run_dir),
            objective_direction=problem.objective.direction,
        )

    # -- attempts --------------------------------------------------------------

    def record_attempt(
        self, candidate_path: str | Path, result: ValidationResult
    ) -> Attempt:
        attempt = Attempt(
            index=len(self.attempts),
            candidate_path=str(candidate_path),
            result=result,
            level=self.ladder_level,
        )
        self.attempts.append(attempt)

        new_best = better_result(self.best_result, result, self.objective_direction)
        if new_best is result:
            self.best_result = result
            self.best_candidate_path = str(candidate_path)
        elif self.best_result is None:
            self.best_result = result
            self.best_candidate_path = str(candidate_path)

        if result.passed:
            self.status = "passed"
        elif self.status != "passed":
            self.status = "failed"
        return attempt

    # -- persistence -----------------------------------------------------------

    def to_dict(self) -> dict[str, Any]:
        return {
            "problem_id": self.problem_id,
            "ladder_level": self.ladder_level,
            "status": self.status,
            "objective_direction": self.objective_direction,
            "best_candidate_path": self.best_candidate_path,
            "best_result": self.best_result.to_dict() if self.best_result else None,
            "attempts": [a.to_dict() for a in self.attempts],
        }

    def save(self) -> None:
        """Atomically write ``run.json`` (temp file + os.replace)."""
        self.run_dir.mkdir(parents=True, exist_ok=True)
        target = self.run_dir / "run.json"
        tmp = target.with_suffix(".json.tmp")
        tmp.write_text(json.dumps(self.to_dict(), indent=2))
        os.replace(tmp, target)

    @classmethod
    def load(cls, run_dir: str | Path) -> "RunState":
        run_dir = Path(run_dir)
        target = run_dir / "run.json"
        if not target.is_file():
            raise RunStateError(f"No run.json in {run_dir}")
        try:
            d = json.loads(target.read_text())
        except json.JSONDecodeError as exc:
            raise RunStateError(f"Corrupt run.json in {run_dir}: {exc}") from exc

        state = cls(
            problem_id=d["problem_id"],
            run_dir=run_dir,
            ladder_level=d.get("ladder_level", 0),
            objective_direction=d.get("objective_direction"),
            status=d.get("status", "in_progress"),
            best_candidate_path=d.get("best_candidate_path"),
        )
        if d.get("best_result"):
            state.best_result = ValidationResult.from_dict(d["best_result"])
        state.attempts = [Attempt.from_dict(a) for a in d.get("attempts", [])]
        return state
