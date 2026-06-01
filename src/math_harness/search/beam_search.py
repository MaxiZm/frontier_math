"""beam_search: seeded candidate search (lightweight stub).

Provides a documented interface; a full implementation can be dropped in later.
All stochastic entry points must accept and log a `seed`.
"""

from __future__ import annotations

from ..core.exceptions import HarnessError


def run(*args, seed: int | None = None, **kwargs):
    raise HarnessError(
        "beam_search is not implemented yet. Use search.local_search.hill_climb, "
        "search.simulated_annealing, or search.random_baselines."
    )
