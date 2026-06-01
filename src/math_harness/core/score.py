"""Validation results and objective-comparison helpers.

All "what counts as better / improved" logic lives here so that run-state
bookkeeping and the optimization validator share one source of truth.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any


def is_better(a: float, b: float, direction: str) -> bool:
    """True if objective value ``a`` is strictly better than ``b``."""
    if direction == "minimize":
        return a < b
    if direction == "maximize":
        return a > b
    raise ValueError(f"Unknown objective direction: {direction!r}")


def compute_improved(
    objective_value: float | None,
    baseline: float | None,
    direction: str | None,
) -> bool:
    """True if ``objective_value`` beats ``baseline`` in the given direction."""
    if objective_value is None or baseline is None or direction is None:
        return False
    return is_better(objective_value, baseline, direction)


@dataclass(slots=True)
class ValidationResult:
    """The outcome of validating a candidate.

    ``passed`` is the only field a binary validator must set. ``objective_value``
    / ``baseline`` / ``improved`` describe optimization-style problems.
    """

    passed: bool
    score: float | None = None
    objective_value: float | None = None
    baseline: float | None = None
    improved: bool = False
    messages: list[str] = field(default_factory=list)
    details: dict[str, Any] = field(default_factory=dict)
    validator: str | None = None

    @classmethod
    def ok(cls, **kwargs: Any) -> "ValidationResult":
        kwargs.setdefault("passed", True)
        return cls(**kwargs)

    @classmethod
    def fail(cls, message: str | None = None, **kwargs: Any) -> "ValidationResult":
        kwargs["passed"] = False
        msgs = list(kwargs.pop("messages", []))
        if message:
            msgs.append(message)
        return cls(messages=msgs, **kwargs)

    # Backwards-friendly alias used in a couple of call sites.
    failure = fail

    def to_dict(self) -> dict[str, Any]:
        return {
            "passed": self.passed,
            "score": self.score,
            "objective_value": self.objective_value,
            "baseline": self.baseline,
            "improved": self.improved,
            "messages": list(self.messages),
            "details": dict(self.details),
            "validator": self.validator,
        }

    @classmethod
    def from_dict(cls, d: dict[str, Any]) -> "ValidationResult":
        return cls(
            passed=bool(d.get("passed", False)),
            score=d.get("score"),
            objective_value=d.get("objective_value"),
            baseline=d.get("baseline"),
            improved=bool(d.get("improved", False)),
            messages=list(d.get("messages", [])),
            details=dict(d.get("details", {})),
            validator=d.get("validator"),
        )


# Naming alias requested by the architecture spec.
Score = ValidationResult


def better_result(
    a: ValidationResult | None,
    b: ValidationResult | None,
    direction: str | None,
) -> ValidationResult | None:
    """Pick the better of two results.

    A passing result beats a non-passing one. Among passing results, compare by
    ``objective_value`` honoring ``direction``; if objective values are missing,
    keep the incumbent (``a``).
    """
    if a is None:
        return b
    if b is None:
        return a
    if a.passed != b.passed:
        return a if a.passed else b
    # Same pass/fail status: compare objectives when possible.
    if direction and a.objective_value is not None and b.objective_value is not None:
        return a if not is_better(b.objective_value, a.objective_value, direction) else b
    return a
