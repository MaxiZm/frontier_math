# NetworkX

## Purpose

NetworkX is a pure-Python graph library for graph prototypes, graph property checks, small exhaustive searches, and construction validators.

## Use when

- You need to build and inspect small candidate graphs quickly.
- You need connectivity, degree, clique, independent-set, matching, or cycle checks.
- You are writing a graph construction validator.
- You want a clear Python prototype before moving to nauty/traces or custom C++.

## Do not use when

- You need high-throughput exhaustive graph enumeration.
- You need canonical labeling or serious isomorphism deduplication; use nauty/traces.
- You need performance on very large dense graphs.

## Availability check

```bash
python - <<'PY'
import networkx as nx
print(nx.__version__)
PY
```

Expected successful output:

```txt
<networkx version>
```

## Installation notes

NetworkX is a project dependency. Install the harness with `pip install -e ".[dev]"` or `uv sync`.

## Minimal smoke test

```python
import networkx as nx

G = nx.cycle_graph(5)
print(nx.is_connected(G))
print(max(len(c) for c in nx.find_cliques(G)))
```

Expected output:

```txt
True
2
```

## Common workflows

### Workflow 1: Validate a graph construction

Goal: check a candidate edge list against graph constraints.

Steps: build a graph, check vertex/edge counts, then run property predicates.

Code:

```python
import networkx as nx
G = nx.cycle_graph(5)
print(G.number_of_nodes(), G.number_of_edges(), nx.is_connected(G))
```

Expected output: `5 5 True`.

### Workflow 2: Search small examples

Goal: brute-force tiny parameter cases before writing a faster search.

Steps: enumerate candidate edges, build graphs, keep those satisfying predicates, and log the best example.

Code:

```python
import networkx as nx
G = nx.complete_graph(4)
print(nx.triangles(G))
```

Expected output: each vertex has `3` triangles.

## Typical mathematical objects

NetworkX is good for simple graphs, directed graphs, bipartite graphs, graph invariants, connectivity, cliques, independent sets, matchings, cuts, paths, and graph-based validators.

## Agent protocol

When using NetworkX, the agent must:

1. State the graph property or construction being tested.
2. Run the smallest graph first.
3. Save code under `experiments/`.
4. Save useful outputs under `experiments/results/`.
5. Record the graph representation and conclusion in `notes/attempt_log.md`.
6. Move to nauty/traces or optimized code when isomorphism or enumeration dominates.

## Pitfalls

- NetworkX is convenient but slow for huge exhaustive searches.
- Some APIs move across NetworkX versions; keep smoke tests simple.
- Isomorphic duplicates can overwhelm naive searches.
- Default graph types may silently merge parallel edges.

## Example integration with the harness

```python
from math_harness.validators.construction_checker import ConstructionChecker

checker = ConstructionChecker(predicates=[lambda G: G.number_of_nodes() == 5])
```

## Final-answer compliance notes

NetworkX is fine for research-time graph prototyping. In final candidates, prefer explicit edge lists or deterministic construction code; importing NetworkX is allowed only if the problem permits it and the validator environment includes it.
