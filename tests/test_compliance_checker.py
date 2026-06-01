from __future__ import annotations

from math_harness.core.problem import Compliance
from math_harness.validators.compliance_checker import ComplianceChecker


def _checker(**overrides) -> ComplianceChecker:
    base = dict(
        allow_search_inside_final_solution=False,
        require_deterministic=True,
        forbidden_imports=(),
        forbidden_calls=(),
    )
    base.update(overrides)
    return ComplianceChecker(Compliance(**base))


def test_clean_source_is_compliant():
    src = "from sympy import pi\n\ndef solve():\n    return pi**2/6\n"
    assert _checker().check_source(src).compliant


def test_search_library_flagged_when_disallowed():
    src = "from scipy.optimize import minimize\n\ndef solve():\n    return minimize(...)\n"
    report = _checker().check_source(src)
    assert not report.compliant
    assert any("hidden-search" in v for v in report.violations)


def test_search_library_allowed_when_enabled():
    src = "from scipy.optimize import minimize\n\ndef solve():\n    return 1\n"
    report = _checker(allow_search_inside_final_solution=True).check_source(src)
    # scipy is still not a network/IO import; with search allowed it should pass.
    assert report.compliant


def test_eval_call_flagged():
    src = "def solve():\n    return eval('1+1')\n"
    report = _checker().check_source(src)
    assert not report.compliant
    assert any("eval" in v for v in report.violations)


def test_randomness_flagged_when_deterministic_required():
    src = "import random\n\ndef solve():\n    return random.random()\n"
    report = _checker(require_deterministic=True).check_source(src)
    assert not report.compliant


def test_network_import_flagged():
    src = "import requests\n\ndef solve():\n    return 1\n"
    assert not _checker().check_source(src).compliant


def test_syntax_error_is_non_compliant():
    report = _checker().check_source("def solve(:\n")
    assert not report.compliant
