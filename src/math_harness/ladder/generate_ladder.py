"""Build the default P0..P10 task ladder (docs/03-task-ladder-protocol.md)."""

from __future__ import annotations

from ..core.problem import Problem
from .ladder_schema import Ladder, LadderLevel

_DEFAULT_LEVELS: list[tuple[str, str]] = [
    ("Restate", "Restate definitions and output format."),
    ("Valid candidate", "Produce any syntactically valid candidate."),
    ("Smallest case", "Solve the smallest parameter case."),
    ("Relaxed version", "Solve a relaxed version."),
    ("Special case", "Solve a symmetric/special case."),
    ("Examples", "Generate computational examples."),
    ("Pattern", "Infer a reusable pattern."),
    ("Restricted proof", "Prove or validate the pattern in a restricted setting."),
    ("Scale up", "Scale to near-original parameters."),
    ("Beat baseline", "Beat a weak or approximate baseline."),
    ("Original", "Solve the original problem."),
]


def default_ladder(problem: Problem | str) -> Ladder:
    """Return the canonical 11-rung (P0..P10) ladder for a problem."""
    pid = problem.id if isinstance(problem, Problem) else str(problem)
    levels = [
        LadderLevel(index=i, name=name, goal=goal)
        for i, (name, goal) in enumerate(_DEFAULT_LEVELS)
    ]
    return Ladder(problem_id=pid, levels=levels)
