"""AST-based compliance checks on a SUBMITTED final candidate.

Philosophy (see ``docs/07-final-answer-compliance.md``):

* Deterministic finite loops that *construct an explicit object* are allowed --
  loops are not cheating.
* What is forbidden (when the problem's rules say so) is *hidden search* inside
  the final answer: numerical optimization / root-finding / integration,
  randomness, network access, subprocesses, file I/O, and known search-library
  imports.

The checker separates research-time exploration (anything goes) from final-answer
admissibility (this module).
"""

from __future__ import annotations

import ast
from dataclasses import dataclass, field
from pathlib import Path

from ..core.candidate import Candidate
from ..core.exceptions import ComplianceViolation
from ..core.problem import Compliance, Problem
from ..core.score import ValidationResult

# Modules that signal hidden search / optimization in a final answer.
_DEFAULT_SEARCH_IMPORTS = frozenset(
    {
        "scipy.optimize",
        "scipy",
        "ortools",
        "pulp",
        "cvxpy",
        "pyomo",
        "nevergrad",
        "deap",
        "hyperopt",
        "optuna",
    }
)
# Modules that imply non-determinism, I/O, or escaping the sandbox.
_NONDETERMINISTIC_IMPORTS = frozenset({"random", "secrets", "numpy.random"})
_IO_NETWORK_IMPORTS = frozenset(
    {"socket", "urllib", "urllib.request", "requests", "httpx", "subprocess", "os", "shutil"}
)
# Call names that are forbidden in a final answer by default.
_DEFAULT_FORBIDDEN_CALLS = frozenset({"eval", "exec", "compile", "__import__", "open"})


@dataclass(slots=True)
class ComplianceReport:
    compliant: bool
    violations: list[str] = field(default_factory=list)

    def as_result(self) -> ValidationResult:
        return ValidationResult(
            passed=self.compliant,
            validator="compliance",
            messages=list(self.violations),
            details={"violations": list(self.violations)},
        )


class ComplianceChecker:
    def __init__(self, compliance: Compliance) -> None:
        self.compliance = compliance

    # -- helpers ---------------------------------------------------------------

    def _import_names(self, node: ast.AST) -> list[str]:
        names: list[str] = []
        if isinstance(node, ast.Import):
            names.extend(alias.name for alias in node.names)
        elif isinstance(node, ast.ImportFrom):
            if node.module:
                names.append(node.module)
        return names

    def _is_forbidden_import(self, modname: str) -> str | None:
        c = self.compliance
        extra = set(c.forbidden_imports)
        # Match on dotted prefixes so "scipy.optimize.foo" is caught by "scipy.optimize".
        candidates = {modname, modname.split(".")[0]}
        if candidates & extra:
            return "forbidden import (problem rule)"
        if not c.allow_search_inside_final_solution and candidates & _DEFAULT_SEARCH_IMPORTS:
            return "hidden-search library import not allowed in final answer"
        if candidates & _IO_NETWORK_IMPORTS:
            return "network / subprocess / file-I/O import not allowed in final answer"
        if c.require_deterministic and candidates & _NONDETERMINISTIC_IMPORTS:
            return "non-deterministic (randomness) import not allowed in final answer"
        return None

    # -- public API ------------------------------------------------------------

    def check_source(
        self, source: str, filename: str = "proposed_solution.py"
    ) -> ComplianceReport:
        try:
            tree = ast.parse(source, filename=filename)
        except SyntaxError as exc:
            return ComplianceReport(False, [f"syntax error: {exc}"])

        violations: list[str] = []
        forbidden_calls = set(self.compliance.forbidden_calls) | _DEFAULT_FORBIDDEN_CALLS

        for node in ast.walk(tree):
            if isinstance(node, (ast.Import, ast.ImportFrom)):
                for name in self._import_names(node):
                    reason = self._is_forbidden_import(name)
                    if reason:
                        violations.append(f"{reason}: import {name!r}")
            elif isinstance(node, ast.Call):
                fname = _call_name(node.func)
                if fname and fname in forbidden_calls:
                    violations.append(f"forbidden call: {fname}()")

        return ComplianceReport(compliant=not violations, violations=violations)

    def check_candidate(self, candidate: Candidate) -> ComplianceReport:
        return self.check_source(candidate.read_source(), filename=str(candidate.path))


def _call_name(func: ast.AST) -> str | None:
    if isinstance(func, ast.Name):
        return func.id
    if isinstance(func, ast.Attribute):
        return func.attr
    return None


def check_compliance(
    file: str | Path, problem: Problem, *, raise_on_violation: bool = False
) -> list[str]:
    """Convenience: return the list of compliance violations for a final answer."""
    source = Path(file).read_text()
    report = ComplianceChecker(problem.compliance).check_source(source, filename=str(file))
    if raise_on_violation and not report.compliant:
        raise ComplianceViolation("; ".join(report.violations))
    return report.violations
