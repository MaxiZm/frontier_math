"""Seeded random-sampling baseline (a control for ablation comparisons)."""

from __future__ import annotations

import random
from typing import Any, Callable

from ..core.score import is_better
from .local_search import SearchResult


def random_search(
    sampler: Callable[[random.Random], Any],
    objective: Callable[[Any], float],
    *,
    direction: str = "minimize",
    iterations: int = 1000,
    seed: int | None = None,
) -> SearchResult:
    """Sample ``iterations`` candidates and return the best. Always log the seed."""
    rng = random.Random(seed)
    best = None
    best_value = None
    for _ in range(iterations):
        cand = sampler(rng)
        value = objective(cand)
        if best_value is None or is_better(value, best_value, direction):
            best, best_value = cand, value
    return SearchResult(best=best, best_value=best_value or 0.0, iterations=iterations, seed=seed)
