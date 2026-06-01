"""Validator for the triangle-free max-edges example.

Expects ``solve()`` to return an edge list ``[[u, v], ...]`` on vertices 0..5.
Checks: exactly 6 vertices used (subset of {0..5}), simple graph, triangle-free;
objective = number of edges; must beat the baseline of 8.
"""

from __future__ import annotations

import networkx as nx

N = 6
BASELINE = 8


def validate(output) -> dict:
    try:
        g = nx.Graph()
        g.add_nodes_from(range(N))
        g.add_edges_from(tuple(e) for e in output)
    except Exception as exc:  # noqa: BLE001
        return {
            "passed": False,
            "messages": [f"could not build graph from output: {exc}"],
            "details": {"output": str(output)},
        }

    messages: list[str] = []
    ok = True

    if any(v not in range(N) for v in g.nodes):
        ok = False
        messages.append(f"vertices must lie in 0..{N - 1}")

    triangles = max(nx.triangles(g).values(), default=0)
    if triangles > 0:
        ok = False
        messages.append("graph contains a triangle (must be triangle-free)")

    edges = g.number_of_edges()
    improved = edges > BASELINE
    # "passed" = feasible (triangle-free, valid vertices). Improvement is separate.
    return {
        "passed": bool(ok),
        "score": float(edges) / BASELINE,
        "objective_value": edges,
        "baseline": BASELINE,
        "improved": bool(ok and improved),
        "messages": messages,
        "details": {"edge_count": edges, "triangles": triangles},
    }
