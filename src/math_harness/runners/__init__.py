"""Deterministic orchestration / bookkeeping.

None of these runners call an LLM. The agent writes candidate files; the runners
load a problem, run the candidate in a sandbox, run the validator + compliance
checks, update run state, and write reports.
"""

from .run_problem import evaluate, EvaluationOutcome

__all__ = ["evaluate", "EvaluationOutcome"]
