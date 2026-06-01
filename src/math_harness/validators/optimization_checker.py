"""Score an objective value against a baseline and decide improvement."""

from __future__ import annotations

from typing import Any, Callable

from ..core.candidate import Candidate
from ..core.problem import Problem
from ..core.score import ValidationResult, compute_improved
from .base import Validator
from .sandbox import run_candidate

FeasibilityFn = Callable[[Any], "tuple[bool, str]"]


def score_objective(
    objective_value: float | None,
    baseline: float | None,
    direction: str | None,
    *,
    feasible: bool = True,
    require_improvement: bool = False,
) -> ValidationResult:
    """Build a :class:`ValidationResult` for an optimization candidate."""
    improved = compute_improved(objective_value, baseline, direction)
    passed = feasible and (improved if require_improvement else True)
    score = None
    if objective_value is not None and baseline not in (None, 0):
        score = float(objective_value) / float(baseline)
    return ValidationResult(
        passed=passed,
        score=score,
        objective_value=objective_value,
        baseline=baseline,
        improved=improved,
        validator="optimization",
    )


class OptimizationChecker(Validator):
    name = "optimization"

    def __init__(
        self,
        objective_fn: Callable[[Any], float],
        feasibility_fns: tuple[FeasibilityFn, ...] = (),
        *,
        direction: str | None = None,
        baseline: float | None = None,
        require_improvement: bool = False,
        reify: Callable[[Any], Any] | None = None,
    ) -> None:
        self.objective_fn = objective_fn
        self.feasibility_fns = feasibility_fns
        self.direction = direction
        self.baseline = baseline
        self.require_improvement = require_improvement
        self.reify = reify

    def validate(self, candidate: Candidate, problem: Problem) -> ValidationResult:
        sb = run_candidate(candidate, problem)
        if not sb.ok:
            return ValidationResult.fail(
                sb.error or "candidate failed in sandbox", validator=self.name
            )

        obj = self.reify(sb.output) if self.reify else sb.output
        direction = self.direction or problem.objective.direction
        baseline = self.baseline if self.baseline is not None else problem.objective.baseline

        messages: list[str] = []
        feasible = True
        for check in self.feasibility_fns:
            ok, msg = check(obj)
            if not ok:
                feasible = False
                messages.append(msg)

        objective_value = None
        if feasible:
            try:
                objective_value = float(self.objective_fn(obj))
            except Exception as exc:  # noqa: BLE001
                feasible = False
                messages.append(f"objective computation failed: {exc}")

        result = score_objective(
            objective_value,
            baseline,
            direction,
            feasible=feasible,
            require_improvement=self.require_improvement,
        )
        result.messages = messages
        result.validator = self.name
        return result
