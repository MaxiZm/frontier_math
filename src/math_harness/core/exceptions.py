"""Harness exception hierarchy.

Design rule: a candidate that *validates false* is NOT an exception -- it is a
``ValidationResult(passed=False)``. Exceptions are reserved for harness / infra
failures (bad problem files, sandbox crashes, missing tools, etc.).
"""

from __future__ import annotations


class HarnessError(Exception):
    """Base class for all harness errors."""


class ProblemLoadError(HarnessError):
    """A problem.yaml is missing, malformed, or fails schema validation."""


class CandidateExecutionError(HarnessError):
    """The candidate file could not be imported or its entrypoint failed."""


class EntrypointNotFoundError(CandidateExecutionError):
    """The configured entrypoint function does not exist in the candidate file."""


class ValidatorError(HarnessError):
    """A validator could not be loaded or crashed (infrastructure failure)."""


class SandboxTimeout(ValidatorError):
    """The candidate exceeded its wall-clock time budget in the sandbox."""


class SandboxExecutionError(ValidatorError):
    """The sandboxed subprocess crashed or exited non-zero."""


class ComplianceViolation(HarnessError):
    """A submitted final candidate violates the problem's compliance rules."""


class RunStateError(HarnessError):
    """A run.json is missing or corrupt."""


class ToolUnavailable(HarnessError):
    """A requested external tool (Sage, GAP, PARI, Z3, Lean, ...) is not installed.

    Carries actionable install guidance so callers can surface a clear message
    instead of a bare ``NotImplementedError`` or a missing-binary traceback.
    """

    def __init__(self, tool: str, guidance: str = "") -> None:
        self.tool = tool
        self.guidance = guidance
        msg = f"Tool {tool!r} is not available in this environment."
        if guidance:
            msg += f" {guidance}"
        super().__init__(msg)
