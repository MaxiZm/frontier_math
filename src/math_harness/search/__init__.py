"""Candidate-search strategies.

All stochastic strategies take and log a ``seed`` so runs are reproducible and
comparable (see docs/11-evaluation-integrity.md).
"""

from .local_search import hill_climb
from .simulated_annealing import simulated_annealing
from .random_baselines import random_search

__all__ = ["hill_climb", "simulated_annealing", "random_search"]
