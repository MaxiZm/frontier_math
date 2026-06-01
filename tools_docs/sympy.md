# SymPy

## Purpose

SymPy is the lightweight pure-Python CAS for symbolic simplification, factorization, exact rational arithmetic, polynomial manipulation, simple equation solving, matrices, and expression comparison.

## Use when

- You need quick symbolic manipulation or expression testing.
- You want exact rational arithmetic without launching Sage.
- You need to factor or expand polynomials over common domains.
- You want a small reproducible experiment that can run inside the Python harness.

## Do not use when

- You need finite fields, serious algebraic number theory, lattices, or combinatorial designs; prefer Sage.
- You need a proof assistant; SymPy is not Lean.
- Simplification failure would be catastrophic; SymPy forms are not always canonical.

## Availability check

```bash
python - <<'PY'
import sympy as sp
print(sp.__version__)
PY
```

Expected successful output:

```txt
<sympy version>
```

## Installation notes

SymPy is a project dependency. Install the harness with `pip install -e ".[dev]"` or `uv sync`.

## Minimal smoke test

```python
from sympy import Rational, factor, simplify, symbols

x = symbols("x")
print(factor(x**4 - 1))
print(simplify((x**2 - 1) / (x - 1)))
print(Rational(1, 3) + Rational(1, 6))
```

## Common workflows

### Workflow 1: Compare symbolic expressions

Goal: check whether two candidate formulas appear equivalent.

Steps: define symbols, subtract expressions, simplify, then test numerically on sample points if simplification is inconclusive.

Code:

```python
from sympy import simplify, symbols
x = symbols("x")
expr = (x**2 - 1) / (x - 1)
print(simplify(expr - (x + 1)))
```

Expected output: `0`.

### Workflow 2: Polynomial manipulation

Goal: factor or expand a candidate closed form.

Steps: construct the polynomial over exact rationals, factor, inspect roots or coefficients.

Code:

```python
from sympy import Poly, factor, symbols
x = symbols("x")
print(factor(x**4 - 1))
print(Poly(x**4 - 1, x).all_coeffs())
```

Expected output includes `(x - 1)*(x + 1)*(x**2 + 1)`.

## Typical mathematical objects

SymPy is good for rational numbers, symbolic expressions, univariate and small multivariate polynomials, exact matrices, recurrences, sums, limits, and simple equations.

## Agent protocol

When using SymPy, the agent must:

1. State the identity or manipulation being tested.
2. Run a minimal expression first.
3. Save experiment code under `experiments/`.
4. Save output under `experiments/results/` if it affects the search path.
5. Record conclusions in `notes/attempt_log.md`.
6. Treat simplification as evidence unless a proof or exact derivation follows.

## Pitfalls

- `simplify` can fail, be slow, or choose a non-useful form.
- Symbolic equality may depend on unstated domains or branch cuts.
- Floating-point inputs contaminate exact computations; use `Rational` for exact rationals.
- Solvers may return partial solution sets or miss domain restrictions.

## Example integration with the harness

```python
from math_harness.tools.sympy_runner import simplify_expression

result = simplify_expression("(x**2 - 1)/(x - 1) - (x + 1)", symbols=["x"])
assert str(result) == "0"
```

## Final-answer compliance notes

SymPy is allowed in research-time experiments. A final candidate may import SymPy only if the problem permits executable symbolic formulas; otherwise emit the explicit expression or construction found during research.
