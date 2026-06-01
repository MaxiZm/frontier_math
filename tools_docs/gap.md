# GAP

Status: documented interface; runner stubbed in this pass.

## Purpose

GAP is a computational discrete-algebra system for finite groups, group actions, permutation groups, automorphism groups, and combinatorial designs with symmetry.

## Use when

- The problem has an explicit group action or symmetry.
- You want to reduce a search space by orbits or stabilizers.
- You need finite-group calculations, conjugacy classes, or permutation groups.
- A combinatorial design is governed by automorphisms.

## Do not use when

- You need generic symbolic algebra; use SymPy or Sage.
- You need numerical constants; use mpmath or PARI/GP.
- The problem has no exploitable symmetry.
- A final candidate must be a simple explicit object and GAP is only needed to discover it.

## Availability check

```bash
gap --version
```

Expected successful output:

```txt
GAP ...
```

## Installation notes

Install GAP from an OS package manager or the official GAP distribution. Some advanced design functionality may require GAP packages.

## Minimal smoke test

```gap
G := SymmetricGroup(4);
Size(G);
Elements(G);
quit;
```

Expected output includes size `24`.

## Common workflows

### Workflow 1: Orbit reduction

Goal: reduce equivalent cases under a group action.

Steps: define the permutation group, define the domain, compute orbits or stabilizers.

Code:

```gap
G := SymmetricGroup(4);
Orbits(G, [1..4]);
Stabilizer(G, 1);
```

Expected output: orbit and stabilizer data.

### Workflow 2: Symmetric design exploration

Goal: inspect a candidate design's automorphism-like structure.

Steps: encode permutations, compute generated group, inspect order and orbits.

Code:

```gap
G := Group((1,2,3,4), (1,2));
Size(G);
ConjugacyClasses(G);
```

Expected output: group size and conjugacy classes.

## Typical mathematical objects

GAP is good for finite groups, permutation groups, group actions, stabilizers, orbits, conjugacy classes, automorphism groups, and symmetry-reduced combinatorial designs.

## Agent protocol

When using GAP, the agent must:

1. State the symmetry being exploited.
2. Run a tiny group calculation first.
3. Save `.g` scripts under `experiments/`.
4. Save outputs under `experiments/results/`.
5. Record orbit/stabilizer conclusions in `notes/attempt_log.md`.
6. Translate discovered symmetric objects into explicit final data.

## Pitfalls

- GAP is not a generic CAS.
- Package availability varies by installation.
- Group action conventions can invert composition/order assumptions.
- Symmetry-reduced results must be lifted back to actual objects.

## Example integration with the harness

```python
from math_harness.tools.gap_runner import available, run

if available():
    run("G := SymmetricGroup(4);; Size(G);")
```

## Final-answer compliance notes

GAP is appropriate for research-time symmetry reduction and verification. Final candidates should contain explicit constructions or formulas, not live GAP calls, unless the problem allows GAP at evaluation time.
