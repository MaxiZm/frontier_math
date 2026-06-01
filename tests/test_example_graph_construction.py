from __future__ import annotations

from math_harness.core.candidate import Candidate
from math_harness.core.problem import Problem
from math_harness.runners.run_problem import evaluate


def test_graph_example_passes_and_improves(graph_dir, tmp_path):
    problem = Problem.load(graph_dir)
    candidate = Candidate.from_problem(problem)
    outcome = evaluate(problem, candidate, run_dir=tmp_path / "run")
    assert outcome.result.passed
    # K_{3,3} has 9 edges, beating the baseline of 8.
    assert outcome.result.objective_value == 9
    assert outcome.result.improved


def test_graph_with_triangle_fails(graph_dir, tmp_path):
    problem = Problem.load(graph_dir)
    wrong = graph_dir / "final" / "wrong_solution.py"
    candidate = Candidate.from_problem(problem, override_path=wrong)
    outcome = evaluate(problem, candidate, run_dir=tmp_path / "run")
    assert not outcome.result.passed
    assert any("triangle" in m for m in outcome.result.messages)
