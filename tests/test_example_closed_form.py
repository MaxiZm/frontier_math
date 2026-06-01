from __future__ import annotations

from math_harness.core.candidate import Candidate
from math_harness.core.problem import Problem
from math_harness.runners.run_problem import evaluate


def test_closed_form_example_passes(closed_form_dir, tmp_path):
    problem = Problem.load(closed_form_dir)
    candidate = Candidate.from_problem(problem)
    outcome = evaluate(problem, candidate, run_dir=tmp_path / "run")
    assert outcome.result.passed
    # Artifacts were written.
    assert (tmp_path / "run" / "run.json").is_file()
    assert (tmp_path / "run" / "validator_calls.jsonl").is_file()
    assert (tmp_path / "run" / "transcript.md").is_file()
    assert outcome.run_state.status == "passed"


def test_closed_form_wrong_candidate_fails(closed_form_dir, tmp_path):
    problem = Problem.load(closed_form_dir)
    wrong = closed_form_dir / "final" / "wrong_solution.py"
    candidate = Candidate.from_problem(problem, override_path=wrong)
    outcome = evaluate(problem, candidate, run_dir=tmp_path / "run")
    assert not outcome.result.passed


def test_cli_main_exit_code(closed_form_dir, tmp_path):
    from math_harness.runners.run_problem import main

    code = main(
        [
            "--problem",
            str(closed_form_dir),
            "--candidate",
            str(closed_form_dir / "final" / "proposed_solution.py"),
            "--run-dir",
            str(tmp_path / "run"),
        ]
    )
    assert code == 0
