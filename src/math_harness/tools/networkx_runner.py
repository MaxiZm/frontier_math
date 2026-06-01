"""NetworkX: graph prototypes (docs/02)."""

from __future__ import annotations

from typing import Any

import networkx as nx


def from_edges(edges: list[tuple[Any, Any]]) -> nx.Graph:
    g = nx.Graph()
    g.add_edges_from(edges)
    return g


def is_triangle_free(graph: nx.Graph) -> bool:
    return nx.triangles(graph) == {} or max(nx.triangles(graph).values(), default=0) == 0


def properties(graph: nx.Graph) -> dict:
    return {
        "n_nodes": graph.number_of_nodes(),
        "n_edges": graph.number_of_edges(),
        "is_connected": nx.is_connected(graph) if graph.number_of_nodes() else False,
        "max_degree": max((d for _, d in graph.degree()), default=0),
    }
