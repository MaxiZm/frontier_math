"""Evaluate a single candidate against a problem and record the result.

This is the deterministic core every other runner builds on. The flow:

    compliance check -> load validator -> validate (candidate runs in sandbox)
    -> log -> record in RunState -> save run.json
"""

from __future__ import annotations

import argparse
import time
from dataclasses import dataclass
from pathlib import Path

from ..core.candidate import Candidate
from ..core.exceptions import HarnessError
from ..core.logging import RunLogger
from ..core.problem import Problem
from ..core.run_state import RunState
from ..core.score import ValidationResult
from ..validators.base import load_problem_validator
from ..validators.compliance_checker import ComplianceChecker


@dataclass(slots=True)
class EvaluationOutcome:
    result: ValidationResult
    run_state: RunState


def _default_run_dir(problem: Problem) -> Path:
    repo_root = Path(__file__).resolve().parents[3]
    return repo_root / "runs" / "local" / problem.id


def evaluate(
    problem: Problem,
    candidate: Candidate,
    run_dir: str | Path | None = None,
    *,
    run_state: RunState | None = None,
    check_compliance: bool = True,
) -> EvaluationOutcome:
    """Run compliance + validation for one candidate and persist the result."""
    rd = Path(run_dir) if run_dir is not None else _default_run_dir(problem)
    logger = RunLogger(rd)
    state = run_state or RunState.new(problem, rd)

    logger.transcript(
        "problem",
        f"id: {problem.id}\nbenchmark: {problem.benchmark}\n"
        f"output_type: {problem.output_type}\ncandidate: {candidate.path}",
    )

    # 1. Compliance (fail fast on a non-compliant final answer).
    if check_compliance:
        report = ComplianceChecker(problem.compliance).check_candidate(candidate)
        if not report.compliant:
            result = ValidationResult.fail(
                "compliance violation",
                validator="compliance",
                messages=report.violations,
                details={"violations": report.violations},
            )
            logger.event("compliance_failed", violations=report.violations)
            state.record_attempt(candidate.path, result)
            state.save()
            return EvaluationOutcome(result=result, run_state=state)

    # 2. Validate (candidate executes inside the sandbox via the validator).
    start = time.perf_counter()
    try:
        validator = load_problem_validator(problem)
        result = validator.validate(candidate, problem)
    except HarnessError as exc:
        result = ValidationResult.fail(
            f"validator infrastructure error: {exc}", validator="harness"
        )
    duration = time.perf_counter() - start

    logger.log_validator_call(result.validator or "unknown", problem.id, result, duration)
    logger.transcript(
        "result",
        f"passed: {result.passed}\nscore: {result.score}\n"
        f"objective_value: {result.objective_value}\nimproved: {result.improved}\n"
        f"messages: {result.messages}",
    )
    state.record_attempt(candidate.path, result)
    state.save()
    return EvaluationOutcome(result=result, run_state=state)


def _print_summary(result: ValidationResult) -> None:
    if result.passed:
        print("VALIDATION PASSED ✓")
    else:
        print("VALIDATION FAILED ✗")
    if result.objective_value is not None:
        print(f"  objective_value: {result.objective_value}")
    if result.baseline is not None:
        print(f"  baseline: {result.baseline}  improved: {result.improved}")
    for msg in result.messages:
        print(f"  - {msg}")


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Evaluate a candidate against a problem.")
    parser.add_argument("--problem", required=True, help="Problem directory or problem.yaml")
    parser.add_argument("--candidate", help="Candidate file (defaults to the entrypoint)")
    parser.add_argument("--run-dir", help="Where to write run artifacts")
    args = parser.parse_args(argv)

    problem = Problem.load(args.problem)
    candidate = Candidate.from_problem(problem, override_path=args.candidate)
    outcome = evaluate(problem, candidate, run_dir=args.run_dir)
    _print_summary(outcome.result)
    return 0 if outcome.result.passed else 1


if __name__ == "__main__":
    raise SystemExit(main())
