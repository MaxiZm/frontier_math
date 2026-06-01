"""Build search queries for retrieval backends from problem context."""

from __future__ import annotations

from dataclasses import dataclass


@dataclass(slots=True)
class Query:
    text: str
    topics: tuple[str, ...] = ()
    max_results: int = 10


def build_query(terms: list[str], topics: list[str] | None = None, max_results: int = 10) -> Query:
    return Query(text=" ".join(terms), topics=tuple(topics or ()), max_results=max_results)
