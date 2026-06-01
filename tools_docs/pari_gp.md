# PARI/GP

Status: documented interface; runner stubbed in this pass.

## Purpose

PARI/GP is a fast number-theory system for algebraic recognition, modular arithmetic, L-functions, zeta-like computations, and high-speed integer arithmetic.

## Use when

- You need `algdep` or `lindep` to recognize a high-precision constant.
- You need fast factorization, modular arithmetic, or number-field calculations.
- You need number-theoretic constants or L-function experiments.
- Sage is too heavy and the task is primarily arithmetic.

## Do not use when

- The task is generic symbolic algebra; use SymPy or Sage.
- You need group theory; use GAP.
- You only have low-precision numerical data.
- You need a final answer that must avoid runtime recognition/search.

## Availability check

```bash
gp --version
```

Expected successful output:

```txt
GP/PARI CALCULATOR Version ...
```

## Installation notes

Install PARI/GP from an OS package manager or official binaries. The Python binding `cypari2` requires libpari and may be harder to install than the CLI.

## Minimal smoke test

```bash
gp -q <<'GP'
algdep(1.41421356237309504880, 2)
lindep([1, Pi, Pi^2])
quit
GP
```

Expected output includes a polynomial such as `x^2 - 2` for the first command.

## Common workflows

### Workflow 1: Algebraic number recognition

Goal: infer a polynomial for a high-precision numeric value.

Steps: compute many digits with mpmath, pass them to `algdep`, then verify symbolically or numerically.

Code:

```gp
algdep(1.414213562373095048801688724209698, 2)
```

Expected output: a degree-2 relation for sqrt(2).

### Workflow 2: Integer relation search

Goal: detect a linear relation among constants.

Steps: collect constants at high precision, run `lindep`, verify the proposed relation independently.

Code:

```gp
lindep([1, Pi, Pi^2])
```

Expected output: no low-complexity relation in this toy list.

## Typical mathematical objects

PARI/GP is good for integers, modular residues, rational numbers, number fields, algebraic numbers, elliptic curves, L-functions, class groups, and high-precision constants.

## Agent protocol

When using PARI/GP, the agent must:

1. State the number-theoretic question.
2. Ensure input precision is high enough.
3. Save `.gp` scripts under `experiments/`.
4. Save GP output under `experiments/results/`.
5. Record candidate relations and independent verification in `notes/attempt_log.md`.
6. Treat recognition output as a conjecture until validated.

## Pitfalls

- Low precision can produce false `algdep` relations.
- `gp` may be shadowed by shell aliases; verify it is the PARI binary.
- Recognition is not proof without independent verification.
- Syntax and precision defaults differ from Python tools.

## Example integration with the harness

```python
from math_harness.tools.pari_runner import available, run

if available():
    run("algdep(1.41421356237309504880, 2)")
```

## Final-answer compliance notes

PARI/GP is for research-time recognition and arithmetic experiments. A final candidate should emit the recognized exact expression or explicit construction, not call `algdep`, `lindep`, or L-function searches at scoring time unless explicitly allowed.
