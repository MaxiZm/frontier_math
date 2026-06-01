"""Helpers for creating an easier intermediate (P k-0.5) level.

When the agent is stuck at level ``k`` (see ``stuck_detector.is_stuck``), it
inserts a level that relaxes *exactly one* constraint, solves that, extracts a
lemma/heuristic, and returns to ``k``.
"""

from __future__ import annotations

from .ladder_schema import Ladder, LadderLevel


def insert_relaxed_level(ladder: Ladder, after_index: int, relaxation: str) -> LadderLevel:
    """Insert a half-step relaxed level after ``after_index`` and return it."""
    half = LadderLevel(
        index=after_index,  # displayed as a half-step in notes; kept adjacent here
        name=f"Relaxed-{after_index}",
        goal=f"Relax exactly one constraint of P{after_index} and solve that.",
        relaxation=relaxation,
    )
    pos = next(
        (i for i, lvl in enumerate(ladder.levels) if lvl.index == after_index),
        len(ladder.levels) - 1,
    )
    ladder.levels.insert(pos + 1, half)
    return half
