"""Resume an in-progress run by re-evaluating the current candidate.

``evaluate`` is pure given (problem, candidate, run_dir), so resuming is just
loading the saved RunState and re-running at its current ladder level.
"""

from __future__ import annotations

import argparse
from pathlib import Path

from ..core.candidate import Candidate
from ..core.problem import Problem
from ..core.run_state import RunState
from .run_problem import evaluate


def resume_run(problem_dir: str | Path, run_dir: str | Path) -> RunState:
    problem = Problem.load(problem_dir)
    state = RunState.load(run_dir)
    if state.status == "passed":
        return state
    candidate = Candidate.from_problem(problem)
    evaluate(problem, candidate, run_dir=run_dir, run_state=state)
    return state


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Resume an in-progress run.")
    parser.add_argument("--problem", required=True)
    parser.add_argument("--run-dir", required=True)
    args = parser.parse_args(argv)
    state = resume_run(args.problem, args.run_dir)
    print(f"Run status: {state.status}")
    return 0 if state.status == "passed" else 1


if __name__ == "__main__":
    raise SystemExit(main())
