"""Validate a numeric / closed-form candidate against a target value."""

from __future__ import annotations

from typing import Any

import mpmath

from ..core.candidate import Candidate
from ..core.problem import Problem
from ..core.score import ValidationResult
from .base import Validator
from .sandbox import run_candidate


def _to_mpf(value: Any, dps: int) -> mpmath.mpf:
    """Coerce a candidate output (number, string, or sympy expression) to mpf."""
    mpmath.mp.dps = dps
    if isinstance(value, (int, float)):
        return mpmath.mpf(value)
    text = str(value)
    try:
        return mpmath.mpf(text)
    except (ValueError, TypeError):
        from sympy import sympify  # local import to keep import cost off hot paths

        return mpmath.mpf(sympify(text).evalf(dps))


def compare_numeric(
    value: Any,
    target: Any,
    tol: float,
    *,
    relative: bool = False,
    dps: int = 50,
) -> tuple[bool, float]:
    """Return ``(passed, abs_error)`` comparing ``value`` to ``target``."""
    mpmath.mp.dps = dps
    v = _to_mpf(value, dps)
    t = _to_mpf(target, dps)
    err = abs(v - t)
    threshold = mpmath.mpf(tol)
    if relative and t != 0:
        passed = err / abs(t) <= threshold
    else:
        passed = err <= threshold
    return bool(passed), float(err)


class NumericClosedFormValidator(Validator):
    name = "numeric_closed_form"

    def __init__(
        self,
        target: Any,
        tol: float = 1e-12,
        *,
        relative: bool = False,
        dps: int = 50,
    ) -> None:
        self.target = target
        self.tol = tol
        self.relative = relative
        self.dps = dps

    def validate(self, candidate: Candidate, problem: Problem) -> ValidationResult:
        sb = run_candidate(candidate, problem)
        if not sb.ok:
            msg = sb.error or "candidate failed in sandbox"
            return ValidationResult.fail(msg, validator=self.name)

        passed, err = compare_numeric(
            sb.output, self.target, self.tol, relative=self.relative, dps=self.dps
        )
        baseline = problem.objective.baseline
        direction = problem.objective.direction
        improved = (
            baseline is not None
            and direction == "minimize"
            and err < baseline
        )
        return ValidationResult(
            passed=passed,
            score=1.0 if passed else 0.0,
            objective_value=err,
            baseline=baseline,
            improved=improved,
            validator=self.name,
            messages=[] if passed else [f"abs_error {err} exceeds tolerance {self.tol}"],
            details={"target": str(self.target), "value": str(sb.output), "abs_error": err},
        )
