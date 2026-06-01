# SymPy

## What it's for
Symbolic mathematics in pure Python: algebraic manipulation, simplification,
solving equations, calculus (derivatives, integrals, limits, series), and quick
expression testing.

## When to use it
- Symbolic manipulation and quick expression testing.
- Simplifying or factoring an expression, checking an identity.
- Series expansions, closed-form integrals/sums where a CAS suffices.
- Light number theory and polynomial work (for heavier exact algebra, finite
  fields, or lattices, prefer Sage — `tools_docs/sage.md`).

## How to call it
Pure-Python package, imported directly:

```python
import sympy as sp
x = sp.symbols('x')
expr = sp.sin(x)**2 + sp.cos(x)**2
sp.simplify(expr)                # -> 1
sp.integrate(sp.exp(-x**2), (x, -sp.oo, sp.oo))  # -> sqrt(pi)
sp.series(sp.exp(x), x, 0, 5)
```

## Install
`pip install sympy`. Pure Python; no external binary. Available in the harness by
default.
