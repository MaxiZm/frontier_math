"""Seeded simulated annealing."""

from __future__ import annotations

import math
import random
from typing import Any, Callable

from .local_search import SearchResult


def simulated_annealing(
    initial: Any,
    neighbors: Callable[[Any, random.Random], Any],
    objective: Callable[[Any], float],
    *,
    direction: str = "minimize",
    iterations: int = 5000,
    t0: float = 1.0,
    cooling: float = 0.999,
    seed: int | None = None,
) -> SearchResult:
    rng = random.Random(seed)
    sign = 1.0 if direction == "minimize" else -1.0
    cur = initial
    cur_v = objective(cur)
    best, best_v = cur, cur_v
    temp = t0
    for _ in range(iterations):
        cand = neighbors(cur, rng)
        cand_v = objective(cand)
        delta = sign * (cand_v - cur_v)
        if delta < 0 or rng.random() < math.exp(-delta / max(temp, 1e-12)):
            cur, cur_v = cand, cand_v
            if sign * (cur_v - best_v) < 0:
                best, best_v = cur, cur_v
        temp *= cooling
    return SearchResult(best=best, best_value=best_v, iterations=iterations, seed=seed)
