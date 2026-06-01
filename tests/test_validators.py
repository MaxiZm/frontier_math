from __future__ import annotations

from math_harness.core.score import (
    ValidationResult,
    better_result,
    compute_improved,
    is_better,
)
from math_harness.validators.numeric_closed_form import compare_numeric
from math_harness.validators.optimization_checker import score_objective


def test_is_better_directions():
    assert is_better(1.0, 2.0, "minimize")
    assert not is_better(2.0, 1.0, "minimize")
    assert is_better(2.0, 1.0, "maximize")


def test_compute_improved_handles_none():
    assert compute_improved(None, 1.0, "minimize") is False
    assert compute_improved(0.5, None, "minimize") is False
    assert compute_improved(0.5, 1.0, "minimize") is True


def test_better_result_prefers_passing():
    a = ValidationResult(passed=False, objective_value=0.1)
    b = ValidationResult(passed=True, objective_value=0.5)
    assert better_result(a, b, "minimize") is b


def test_better_result_compares_objective_among_passing():
    a = ValidationResult(passed=True, objective_value=0.5)
    b = ValidationResult(passed=True, objective_value=0.1)
    assert better_result(a, b, "minimize") is b
    assert better_result(a, b, "maximize") is a


def test_validation_result_round_trip():
    r = ValidationResult(passed=True, score=1.0, objective_value=0.3, messages=["ok"])
    assert ValidationResult.from_dict(r.to_dict()) == r


def test_compare_numeric_pass_and_fail():
    ok, err = compare_numeric("pi**2/6", "pi**2/6", 1e-30)
    assert ok and err < 1e-30
    ok2, err2 = compare_numeric("pi**2/5", "pi**2/6", 1e-30)
    assert not ok2 and err2 > 0


def test_score_objective_improvement():
    r = score_objective(7.0, baseline=8.0, direction="minimize")
    assert r.passed and r.improved
    r2 = score_objective(9.0, baseline=8.0, direction="minimize")
    assert r2.passed and not r2.improved
