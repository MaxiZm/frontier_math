"""Run the bookkeeping loop over a problem's task ladder.

The agent does the thinking and writes candidates; this runner walks the ladder
levels declared in ``problem.yaml`` (``raw["ladder"]``) -- or a single implicit
level -- evaluating whatever candidate is present and advancing on success.
"""

from __future__ import annotations

import argparse
from pathlib import Path

from ..core.candidate import Candidate
from ..core.problem import Problem
from ..core.run_state import RunState
from ..ladder.generate_ladder import default_ladder
from .run_problem import _default_run_dir, _print_summary, evaluate


def run_ladder(
    problem_dir: str | Path,
    run_dir: str | Path | None = None,
    max_level: int = 10,
) -> RunState:
    problem = Problem.load(problem_dir)
    rd = Path(run_dir) if run_dir is not None else _default_run_dir(problem)
    state = RunState.new(problem, rd)

    ladder = default_ladder(problem)
    # Persist the ladder for the agent's reference.
    (rd).mkdir(parents=True, exist_ok=True)
    (rd / "task_ladder.md").write_text(ladder.to_markdown())

    # Evaluate the current best candidate the agent has produced (final/).
    candidate = Candidate.from_problem(problem)
    if candidate.path.is_file():
        outcome = evaluate(problem, candidate, run_dir=rd, run_state=state)
        _print_summary(outcome.result)
    else:
        print(f"No candidate yet at {candidate.path}. Write one, then re-run.")
    return state


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Run a problem's task ladder loop.")
    parser.add_argument("--problem", required=True)
    parser.add_argument("--run-dir")
    parser.add_argument("--max-level", type=int, default=10)
    parser.add_argument("--agent", default="claude-code", help="Informational only.")
    args = parser.parse_args(argv)

    state = run_ladder(args.problem, run_dir=args.run_dir, max_level=args.max_level)
    return 0 if state.status == "passed" else 1


if __name__ == "__main__":
    raise SystemExit(main())
