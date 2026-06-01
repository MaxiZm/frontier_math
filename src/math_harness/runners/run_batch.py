"""Evaluate every problem under a directory and aggregate pass/fail + objective."""

from __future__ import annotations

import argparse
import json
from pathlib import Path

from ..core.candidate import Candidate
from ..core.problem import Problem
from .run_problem import evaluate


def run_batch(problems_dir: str | Path, run_dir: str | Path) -> dict:
    problems_dir = Path(problems_dir)
    run_dir = Path(run_dir)
    run_dir.mkdir(parents=True, exist_ok=True)

    summary: dict[str, dict] = {}
    for yaml_path in sorted(problems_dir.glob("*/problem.yaml")):
        problem = Problem.load(yaml_path)
        candidate = Candidate.from_problem(problem)
        if not candidate.path.is_file():
            summary[problem.id] = {"status": "no_candidate"}
            continue
        outcome = evaluate(problem, candidate, run_dir=run_dir / problem.id)
        summary[problem.id] = {
            "passed": outcome.result.passed,
            "objective_value": outcome.result.objective_value,
            "improved": outcome.result.improved,
        }

    (run_dir / "batch_summary.json").write_text(json.dumps(summary, indent=2))
    return summary


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Batch-evaluate a directory of problems.")
    parser.add_argument("--problems", required=True)
    parser.add_argument("--run-dir", required=True)
    args = parser.parse_args(argv)
    summary = run_batch(args.problems, args.run_dir)
    passed = sum(1 for v in summary.values() if v.get("passed"))
    print(f"{passed}/{len(summary)} problems passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
