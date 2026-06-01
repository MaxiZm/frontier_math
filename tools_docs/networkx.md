# NetworkX

## What it's for
Pure-Python graph and network library: build graphs, compute standard invariants
(degrees, connectivity, cliques, matchings, spectra), and prototype graph
algorithms quickly.

## When to use it
- Graph prototypes (per the tool router, `docs/02-tool-router.md`): rapidly build
  and inspect candidate graphs.
- Computing properties of a construction (edge counts, girth, chromatic-ish
  bounds, eigenvalues via the Laplacian/adjacency matrix).
- **Not** the tool for canonical isomorphism testing or exhaustive enumeration of
  graphs — use nauty/traces (`tools_docs/nauty_traces.md`) for that.

## How to call it
Pure-Python package, imported directly:

```python
import networkx as nx
G = nx.Graph()
G.add_edges_from([(0,1),(1,2),(2,0)])
nx.number_of_edges(G)            # 3
list(nx.find_cliques(G))
nx.adjacency_spectrum(G)
```

## Install
`pip install networkx`. Pure Python; no external binary. Available in the harness
by default.
