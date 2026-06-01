from __future__ import annotations

import pytest

from math_harness.core.exceptions import ProblemLoadError
from math_harness.core.problem import Problem


def test_template_problem_loads_and_round_trips(template_dir):
    problem = Problem.load(template_dir)
    assert problem.id == "template_problem"
    assert problem.benchmark == "custom"
    assert problem.output_type == "construction"
    assert problem.entrypoint.function_name == "solve"
    assert problem.validator.timeout_seconds == 120
    # Path helpers resolve relative to the problem dir.
    assert problem.entrypoint_path().name == "proposed_solution.py"
    assert problem.validator_path().name == "validator.py"


def test_load_from_yaml_path_directly(template_dir):
    problem = Problem.load(template_dir / "problem.yaml")
    assert problem.id == "template_problem"


def test_missing_required_field_raises(tmp_path):
    bad = tmp_path / "problem.yaml"
    bad.write_text("id: x\nbenchmark: y\n")  # missing output_type/evaluation_mode/...
    with pytest.raises(ProblemLoadError):
        Problem.load(bad)


def test_invalid_enum_value_raises(tmp_path):
    bad = tmp_path / "problem.yaml"
    bad.write_text(
        "id: x\nbenchmark: y\noutput_type: not_a_type\n"
        "evaluation_mode: ground_truth_computable\n"
        "entrypoint: {function_name: solve, file: final/proposed_solution.py}\n"
        "validator: {file: validator.py}\n"
    )
    with pytest.raises(ProblemLoadError):
        Problem.load(bad)


def test_malformed_yaml_raises(tmp_path):
    bad = tmp_path / "problem.yaml"
    bad.write_text("id: [unterminated\n")
    with pytest.raises(ProblemLoadError):
        Problem.load(bad)
