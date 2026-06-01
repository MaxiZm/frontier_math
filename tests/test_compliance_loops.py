"""Loops that *construct* an explicit object are compliant; hidden search is not."""

from __future__ import annotations

from math_harness.core.problem import Compliance
from math_harness.validators.compliance_checker import ComplianceChecker


def _checker() -> ComplianceChecker:
    return ComplianceChecker(
        Compliance(allow_search_inside_final_solution=False, require_deterministic=True)
    )


def test_deterministic_construction_loop_is_compliant():
    src = (
        "def solve():\n"
        "    edges = []\n"
        "    for u in [0, 1, 2]:\n"
        "        for v in [3, 4, 5]:\n"
        "            edges.append([u, v])\n"
        "    return edges\n"
    )
    report = _checker().check_source(src)
    assert report.compliant, report.violations


def test_hidden_optimization_loop_is_flagged():
    src = (
        "from scipy.optimize import minimize\n"
        "def solve():\n"
        "    best = None\n"
        "    for _ in range(100):\n"
        "        best = minimize(lambda x: x, 0)\n"
        "    return best\n"
    )
    assert not _checker().check_source(src).compliant


def test_random_search_loop_is_flagged():
    src = (
        "import random\n"
        "def solve():\n"
        "    best = 0\n"
        "    for _ in range(100):\n"
        "        best = max(best, random.random())\n"
        "    return best\n"
    )
    assert not _checker().check_source(src).compliant
