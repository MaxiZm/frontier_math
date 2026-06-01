# nauty / Traces

## What it's for
State-of-the-art tools for **graph canonical labeling, isomorphism testing, and
automorphism groups**, plus high-throughput **graph generation** (`geng`,
`genbg`, `directg`, …).

## When to use it
Per the tool router (`docs/02-tool-router.md`), use nauty/traces for graph
isomorphism and enumeration:
- decide whether two candidate graphs are isomorphic;
- canonically label graphs to deduplicate a search;
- exhaustively generate all non-isomorphic graphs on *n* vertices (with degree /
  girth / connectivity filters) for extremal searches;
- compute automorphism groups.

## How to call it
Solver binaries (`geng`, `dreadnaut`, `labelg`, `shortg`), or the Python binding
`pynauty`:

```bash
geng 7 -d2 | labelg            # all 7-vertex graphs, min degree 2, canonical form
```

```python
import pynauty
g = pynauty.Graph(4)
g.connect_vertex(0, [1, 2])
pynauty.certificate(g)         # canonical certificate for iso testing
```

## Install
Install the nauty/Traces package (provides `geng`, `dreadnaut`, etc.), or
`pip install pynauty`. Verify with `geng --help`.

> **Runner status: STUB.** The harness tool runner for nauty/Traces raises
> `ToolUnavailable` until the nauty binaries (or `pynauty`) are installed.
