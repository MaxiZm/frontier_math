"""PARI/GP runner -- STUB.

Exposes the intended interface but raises ToolUnavailable until the binary is
installed. Availability is checked via tools.availability.require("pari").
See docs/02-tool-router.md for when to reach for PARI/GP.
"""

from __future__ import annotations

from .availability import is_available, require


def available() -> bool:
    return is_available("pari")


def run(script: str, *, timeout: float = 60.0) -> dict:
    """Run a PARI/GP script and return its result. Stub: requires the binary."""
    require("pari")  # raises ToolUnavailable with install guidance
    raise NotImplementedError(
        "PARI/GP integration is stubbed. The binary was found; wire up the call here."
    )
