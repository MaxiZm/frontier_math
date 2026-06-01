"""Re-run evaluation under toggled conditions to characterize the harness.

Ablation arms (see docs/09-benchmarking.md):
    raw_model -> tools_only -> tools_plus_ladder
    -> tools_plus_ladder_plus_retrieval -> full_harness

Here we provide the deterministic *evaluation* side: given candidates produced
under each arm, re-evaluate and record results side by side. The arm labels are
metadata; the agent (not this runner) varies its own behavior per arm.
"""

from __future__ import annotations

import argparse
import json
from pathlib import Path

from ..core.candidate import Candidate
from ..core.problem import Problem
from .run_problem import evaluate

ARMS = (
    "raw_model",
    "tools_only",
    "tools_plus_ladder",
    "tools_plus_ladder_plus_retrieval",
    "full_harness",
)


def run_ablation(problem_dir: str | Path, candidates: dict[str, str], run_root: str | Path) -> dict:
    """``candidates`` maps an arm label -> candidate file path."""
    problem = Problem.load(problem_dir)
    run_root = Path(run_root)
    report: dict[str, dict] = {}
    for arm, cand_path in candidates.items():
        candidate = Candidate.from_problem(problem, override_path=cand_path)
        outcome = evaluate(problem, candidate, run_dir=run_root / arm / problem.id)
        report[arm] = outcome.result.to_dict()
    run_root.mkdir(parents=True, exist_ok=True)
    (run_root / "ablation_report.json").write_text(json.dumps(report, indent=2))
    return report


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Run an ablation across harness arms.")
    parser.add_argument("--problem", required=True)
    parser.add_argument("--run-root", required=True)
    parser.add_argument(
        "--candidate",
        action="append",
        default=[],
        metavar="ARM=PATH",
        help="Repeatable: arm label and candidate file, e.g. full_harness=final/proposed_solution.py",
    )
    args = parser.parse_args(argv)
    candidates = dict(item.split("=", 1) for item in args.candidate)
    run_ablation(args.problem, candidates, args.run_root)
    print(f"Ablation report written to {args.run_root}/ablation_report.json")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
