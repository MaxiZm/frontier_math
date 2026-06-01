"""Validate a combinatorial / geometric construction against constraints."""

from __future__ import annotations

from typing import Any, Callable

import networkx as nx

from ..core.candidate import Candidate
from ..core.problem import Problem
from ..core.score import ValidationResult, compute_improved
from .base import Validator
from .sandbox import run_candidate

# A constraint takes the constructed object and returns (satisfied, message).
ConstraintFn = Callable[[Any], "tuple[bool, str]"]


def build_graph(serialized: Any) -> nx.Graph:
    """Rebuild an ``nx.Graph`` from a serialized candidate output.

    Accepts: an edge list ``[[u, v], ...]``, an adjacency dict
    ``{u: [v, ...]}``, or a dict ``{"nodes": [...], "edges": [[u, v], ...]}``.
    """
    g = nx.Graph()
    if isinstance(serialized, dict) and "edges" in serialized:
        g.add_nodes_from(serialized.get("nodes", []))
        g.add_edges_from(tuple(e) for e in serialized["edges"])
    elif isinstance(serialized, dict):
        for u, nbrs in serialized.items():
            g.add_node(u)
            for v in nbrs:
                g.add_edge(u, v)
    else:  # assume edge list
        g.add_edges_from(tuple(e) for e in serialized)
    return g


class ConstructionChecker(Validator):
    name = "construction"

    def __init__(
        self,
        constraints: list[ConstraintFn],
        objective_fn: Callable[[Any], float] | None = None,
        *,
        reify: Callable[[Any], Any] | None = None,
    ) -> None:
        self.constraints = constraints
        self.objective_fn = objective_fn
        self.reify = reify

    def validate(self, candidate: Candidate, problem: Problem) -> ValidationResult:
        sb = run_candidate(candidate, problem)
        if not sb.ok:
            return ValidationResult.fail(
                sb.error or "candidate failed in sandbox", validator=self.name
            )

        obj = self.reify(sb.output) if self.reify else sb.output

        messages: list[str] = []
        all_ok = True
        for constraint in self.constraints:
            ok, msg = constraint(obj)
            if not ok:
                all_ok = False
                messages.append(msg)

        objective_value = None
        if self.objective_fn is not None:
            try:
                objective_value = float(self.objective_fn(obj))
            except Exception as exc:  # noqa: BLE001
                all_ok = False
                messages.append(f"objective computation failed: {exc}")

        baseline = problem.objective.baseline
        direction = problem.objective.direction
        improved = all_ok and compute_improved(objective_value, baseline, direction)

        return ValidationResult(
            passed=all_ok,
            score=1.0 if all_ok else 0.0,
            objective_value=objective_value,
            baseline=baseline,
            improved=improved,
            validator=self.name,
            messages=messages,
            details={"objective_value": objective_value},
        )
