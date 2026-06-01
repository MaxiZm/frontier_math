# nauty / Traces

Status: documented interface; runner stubbed in this pass.

## Purpose

nauty/Traces provides graph isomorphism testing, canonical labeling, automorphism groups, and non-isomorphic graph enumeration.

## Use when

- NetworkX prototypes produce many isomorphic duplicates.
- You need canonical labels or graph certificates.
- You need exhaustive enumeration of non-isomorphic graphs.
- You need automorphism groups for graph constructions.

## Do not use when

- The graph task is a tiny prototype; use NetworkX first.
- You need general symbolic or numeric math.
- You have not defined the graph encoding and decoding conventions.
- The final candidate can simply include an explicit graph.

## Availability check

```bash
command -v geng && command -v dreadnaut && command -v labelg
```

Expected successful output:

```txt
/path/to/geng
/path/to/dreadnaut
/path/to/labelg
```

## Installation notes

Install the nauty/Traces package from official sources or an OS package manager. The Python package `pynauty` can cover some canonical-labeling workflows but is not identical to the CLI tools.

## Minimal smoke test

```bash
geng 4 | labelg
```

Expected output: graph6/canonical graph data for 4-vertex graphs.

## Common workflows

### Workflow 1: Enumerate non-isomorphic graphs

Goal: produce one representative per isomorphism class.

Steps: call `geng` with parameter filters, pipe to `shortg`/`labelg`, decode into candidate graphs.

Code:

```bash
geng 7 -d2 | labelg
```

Expected output: canonical graph stream for 7-vertex graphs with minimum degree 2.

### Workflow 2: Canonical deduplication

Goal: avoid revisiting isomorphic graph candidates.

Steps: encode candidate to graph6, canonicalize, store certificate in a seen set.

Code:

```python
# Future harness integration may shell out to labelg or use pynauty.certificate.
certificate = "canonical-graph-certificate"
```

Expected output: stable certificate for isomorphic copies.

## Typical mathematical objects

nauty/Traces is good for simple graphs, directed graphs through related tools, canonical graph labels, graph6/sparse6 encodings, automorphism groups, and isomorphism-class enumeration.

## Agent protocol

When using nauty/Traces, the agent must:

1. State why NetworkX is insufficient.
2. Run a tiny `geng` smoke test first.
3. Save shell commands or wrapper scripts under `experiments/`.
4. Save graph streams/certificates under `experiments/results/` when reusable.
5. Record filters and decoding assumptions in `notes/attempt_log.md`.
6. Validate any final decoded graph with the problem validator.

## Pitfalls

- graph6/sparse6 decoding mistakes are easy.
- CLI flags are compact and easy to misuse.
- Canonical labels prove isomorphism of encoded graphs, not correctness of the mathematical construction.
- Enumeration can explode quickly despite isomorphism reduction.

## Example integration with the harness

```python
from math_harness.tools.availability import is_available

if is_available("nauty"):
    print("nauty geng is available for future runner wiring")
```

## Final-answer compliance notes

nauty/Traces is a research-time enumeration and deduplication tool. Final candidates should include explicit graph data or deterministic construction code; do not call nauty during final evaluation unless explicitly allowed.
