"""Detect when the agent is stuck at a ladder level and should relax a constraint."""

from __future__ import annotations

from collections.abc import Sequence


def is_stuck(results: Sequence[bool], threshold: int = 3) -> bool:
    """True if the last ``threshold`` attempts all failed.

    ``results`` is a chronological sequence of pass/fail booleans for the current
    level. Mirrors docs/03: "If stuck for 3 attempts at level k, create level
    k-0.5, relax exactly one constraint, ...".
    """
    if threshold <= 0:
        return False
    if len(results) < threshold:
        return False
    return not any(results[-threshold:])


def consecutive_failures(results: Sequence[bool]) -> int:
    count = 0
    for ok in reversed(results):
        if ok:
            break
        count += 1
    return count
