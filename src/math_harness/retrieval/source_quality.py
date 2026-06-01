"""Rank retrieval sources by a simple, transparent quality heuristic."""

from __future__ import annotations

_VENUE_WEIGHTS = {
    "annals": 1.0,
    "inventiones": 0.95,
    "jams": 0.95,
    "survey": 0.8,
    "arxiv": 0.5,
    "preprint": 0.4,
}


def score_source(venue: str | None, year: int | None = None, citations: int | None = None) -> float:
    base = _VENUE_WEIGHTS.get((venue or "").lower(), 0.5)
    if citations:
        base += min(citations / 1000.0, 0.5)
    return round(base, 3)
