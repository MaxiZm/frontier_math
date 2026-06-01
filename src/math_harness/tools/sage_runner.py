"""Sage runner -- STUB.

Exposes the intended interface but raises ToolUnavailable until the binary is
installed. Availability is checked via tools.availability.require("sage").
See docs/02-tool-router.md for when to reach for Sage.
"""

from __future__ import annotations

from .availability import is_available, require


def available() -> bool:
    return is_available("sage")


def run(script: str, *, timeout: float = 60.0) -> dict:
    """Run a Sage script and return its result. Stub: requires the binary."""
    require("sage")  # raises ToolUnavailable with install guidance
    raise NotImplementedError(
        "Sage integration is stubbed. The binary was found; wire up the call here."
    )
