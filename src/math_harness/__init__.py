"""math_harness: a verifier-driven mathematical-discovery harness.

The package is deterministic bookkeeping + verification. It does not call an LLM:
the agent writes candidate solution files; the harness loads a problem, runs the
candidate in a sandbox, runs the validator, scores it, and records the result.
"""

from .core.problem import Problem
from .core.candidate import Candidate
from .core.score import ValidationResult, Score
from .core.run_state import RunState

__all__ = ["Problem", "Candidate", "ValidationResult", "Score", "RunState"]

__version__ = "0.1.0"
