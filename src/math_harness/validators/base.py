"""Validator base class and per-problem validator loading.

Each problem directory contains a ``validator.py`` exposing EITHER:

* ``def validate(output) -> dict``  -- the simple, function-style convention
  (the dict matches :class:`ValidationResult` field names), OR
* ``class Validator(BaseValidator)`` -- full control over candidate execution.

``load_problem_validator(problem)`` discovers whichever is present and adapts it.
The function-style validator runs the candidate through the sandbox to obtain its
output, then calls ``validate(output)``.
"""

from __future__ import annotations

import hashlib
import importlib.util
from abc import ABC, abstractmethod
from typing import Any, Callable

from ..core.candidate import Candidate
from ..core.exceptions import ValidatorError
from ..core.problem import Problem
from ..core.score import ValidationResult
from .sandbox import run_candidate


class Validator(ABC):
    name: str = "base"

    @abstractmethod
    def validate(self, candidate: Candidate, problem: Problem) -> ValidationResult:
        ...


class _FunctionValidator(Validator):
    """Adapts a problem's ``validate(output) -> dict`` into a :class:`Validator`."""

    name = "function"

    def __init__(self, fn: Callable[[Any], dict], *, use_sandbox: bool = True) -> None:
        self._fn = fn
        self._use_sandbox = use_sandbox

    def validate(self, candidate: Candidate, problem: Problem) -> ValidationResult:
        if self._use_sandbox:
            sb = run_candidate(candidate, problem)
            if sb.timed_out:
                return ValidationResult.fail(
                    f"candidate timed out after {problem.validator.timeout_seconds}s",
                    validator=self.name,
                )
            if not sb.ok:
                return ValidationResult.fail(
                    f"candidate failed in sandbox: {sb.error}",
                    validator=self.name,
                    details={"stderr": sb.stderr, **sb.details},
                )
            output = sb.output
        else:
            output = candidate.run()

        raw = self._fn(output)
        if isinstance(raw, ValidationResult):
            return raw
        if not isinstance(raw, dict):
            raise ValidatorError(
                f"validate() must return a dict or ValidationResult, got {type(raw)!r}"
            )
        result = ValidationResult.from_dict(raw)
        if result.validator is None:
            result.validator = "problem.validate"
        return result


def _load_module(path):
    digest = hashlib.sha1(str(path).encode()).hexdigest()[:12]
    spec = importlib.util.spec_from_file_location(f"mh_validator_{digest}", path)
    if spec is None or spec.loader is None:
        raise ValidatorError(f"Cannot import validator at {path}")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def load_problem_validator(problem: Problem) -> Validator:
    """Discover and return the validator for ``problem``."""
    path = problem.validator_path()
    if not path.is_file():
        raise ValidatorError(f"validator.py not found at {path}")

    module = _load_module(path)

    cls = getattr(module, "Validator", None)
    if isinstance(cls, type) and issubclass(cls, Validator) and cls is not Validator:
        return cls()  # type: ignore[call-arg]

    fn = getattr(module, "validate", None)
    if callable(fn):
        use_sandbox = problem.validator.deterministic or True
        return _FunctionValidator(fn, use_sandbox=use_sandbox)

    raise ValidatorError(
        f"{path} must define a `validate(output) -> dict` function or a "
        f"`Validator` subclass."
    )
