"""OEIS client. Offline by default: queries are stubbed unless a fetcher is wired.

The lookup helper formats a query and raises ToolUnavailable if no network
backend is configured, so callers fail clearly rather than silently.
"""

from __future__ import annotations

from ..core.exceptions import ToolUnavailable


def format_sequence(terms: list[int]) -> str:
    return ",".join(str(t) for t in terms)


def lookup(terms: list[int]):
    raise ToolUnavailable(
        "oeis",
        "No OEIS backend configured. Wire up the mcp_servers/oeis_search server "
        f"to query the sequence {format_sequence(terms)}.",
    )
