"""Decide whether to promote the run to the next ladder level."""

from __future__ import annotations

from ..core.run_state import RunState


def should_promote(state: RunState) -> bool:
    """Promote once the current level has a passing attempt."""
    return state.best_result is not None and state.best_result.passed


def promote(state: RunState, max_level: int = 10) -> int:
    """Advance the ladder level (capped at ``max_level``) and return the new level."""
    if state.ladder_level < max_level:
        state.ladder_level += 1
    return state.ladder_level
