# Sage (SageMath)

Status: documented interface; runner stubbed in this pass.

## Purpose

SageMath is a large exact-mathematics environment combining PARI, GAP, Singular, NetworkX, and many other libraries behind a Python-like interface.

## Use when

- You need exact algebra beyond SymPy.
- You need polynomial rings, rational arithmetic, finite fields, matrices, or lattices.
- You need number theory experiments such as factorization, elliptic curves, modular arithmetic, or algebraic structures.
- You need combinatorial designs or exact constructions with mathematical structure.

## Do not use when

- A small SymPy/mpmath experiment is enough.
- Startup cost or installation size would dominate the task.
- You need a final candidate that must be dependency-light and self-contained.
- You need formal proof checking; use Lean/mathlib for that.

## Availability check

```bash
sage --version
```

Expected successful output:

```txt
SageMath version ...
```

## Installation notes

Install SageMath from its official distribution, an OS package manager, or a conda package when available. It is large; verify the `sage` executable is on `PATH` before relying on it.

## Minimal smoke test

Save as `experiments/sage_smoke.sage` and run `sage experiments/sage_smoke.sage`:

```python
R.<x> = PolynomialRing(QQ)
print(factor(x^4 - 1))
F = GF(7)
print(F(3)^3)
A = Matrix(QQ, [[1, 2], [3, 4]])
print(A.det())
```

Expected output includes a factorization of `x^4 - 1`, `6` in `GF(7)`, and determinant `-2`.

## Common workflows

### Workflow 1: Exact algebra and polynomial rings

Goal: factor or manipulate expressions over explicit rings.

Steps: create a ring, construct elements, factor or solve exactly.

Code:

```python
R.<x> = PolynomialRing(QQ)
print(factor(x^4 - 1))
print((x^2 - 1).quo_rem(x - 1))
```

Expected output: exact polynomial factors and quotient/remainder.

### Workflow 2: Finite fields and matrices

Goal: test algebraic constructions over finite fields or exact rationals.

Steps: define a field or matrix space, construct objects, compute invariants.

Code:

```python
F = GF(7)
print(F(3)^3)
A = Matrix(QQ, [[1, 2], [3, 4]])
print(A.det())
```

Expected output: exact finite-field and rational-matrix results.

### Workflow 3: Number theory experiments

Goal: inspect arithmetic objects before committing to a construction.

Steps: use Sage's number-theory libraries and record the exact object.

Code:

```python
E = EllipticCurve([0, 0, 1, -7, 6])
print(E.rank())
print(factor(2^67 - 1))
```

Expected output: exact rank/factorization data.

## Typical mathematical objects

Sage is good for polynomial rings, finite fields, exact matrices, lattices, elliptic curves, modular forms, groups through GAP, PARI-backed arithmetic, combinatorial designs, and graph objects.

## Agent protocol

When using Sage, the agent must:

1. State why SymPy/mpmath are insufficient.
2. Run a tiny `.sage` smoke test first.
3. Save `.sage` or `sage -python` code under `experiments/`.
4. Save output under `experiments/results/`.
5. Record exact objects and conclusions in `notes/attempt_log.md`.
6. Convert any final construction into explicit Python/data unless Sage is allowed by the problem.

## Pitfalls

- Sage syntax such as `R.<x>` is not valid plain Python.
- Sage startup and installation are heavy.
- Parent rings matter; the same expression over different rings can behave differently.
- Sage evidence is not a formal proof unless the mathematical argument is captured.

## Example integration with the harness

```python
from math_harness.tools.sage_runner import available, run

if available():
    run("R.<x> = PolynomialRing(QQ); print(factor(x^4 - 1))")
```

## Final-answer compliance notes

Sage is usually a research-time tool. Final submitted candidates should contain explicit constants, formulas, or constructions found with Sage, not live Sage calls, unless the problem explicitly permits Sage in final code.
