"""Seeded hill-climbing local search over an arbitrary candidate space."""

from __future__ import annotations

import random
from dataclasses import dataclass
from typing import Any, Callable

from ..core.score import is_better


@dataclass(slots=True)
class SearchResult:
    best: Any
    best_value: float
    iterations: int
    seed: int | None


def hill_climb(
    initial: Any,
    neighbors: Callable[[Any, random.Random], Any],
    objective: Callable[[Any], float],
    *,
    direction: str = "minimize",
    iterations: int = 1000,
    seed: int | None = None,
) -> SearchResult:
    """Greedy local search. ``neighbors(state, rng)`` proposes a candidate move."""
    rng = random.Random(seed)
    best = initial
    best_value = objective(best)
    for i in range(iterations):
        cand = neighbors(best, rng)
        value = objective(cand)
        if is_better(value, best_value, direction):
            best, best_value = cand, value
    return SearchResult(best=best, best_value=best_value, iterations=iterations, seed=seed)
