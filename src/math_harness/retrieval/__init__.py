"""Retrieval: decide *whether* and *what* to retrieve, per docs/04-retrieval-policy.md."""

from .router import (
    RetrievalTrigger,
    SOURCE_ORDER,
    should_retrieve,
    source_order,
    route,
)

__all__ = [
    "RetrievalTrigger",
    "SOURCE_ORDER",
    "should_retrieve",
    "source_order",
    "route",
]
