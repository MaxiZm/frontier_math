"""a SAT solver runner -- STUB.

Exposes the intended interface but raises ToolUnavailable until the binary is
installed. Availability is checked via tools.availability.require("z3").
See docs/02-tool-router.md for when to reach for a SAT solver.
"""

from __future__ import annotations

from .availability import is_available, require


def available() -> bool:
    return is_available("z3")


def run(script: str, *, timeout: float = 60.0) -> dict:
    """Run a a SAT solver script and return its result. Stub: requires the binary."""
    require("z3")  # raises ToolUnavailable with install guidance
    raise NotImplementedError(
        "a SAT solver integration is stubbed. The binary was found; wire up the call here."
    )
