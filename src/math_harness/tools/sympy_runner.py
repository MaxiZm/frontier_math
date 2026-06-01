"""SymPy: symbolic manipulation and quick expression testing (docs/02)."""

from __future__ import annotations

from typing import Any

import sympy as sp


def simplify(expr: str) -> str:
    return str(sp.simplify(sp.sympify(expr)))


def evaluate(expr: str, subs: dict[str, Any] | None = None) -> str:
    e = sp.sympify(expr)
    if subs:
        e = e.subs({sp.Symbol(k): v for k, v in subs.items()})
    return str(e)


def solve(equation: str, symbol: str) -> list[str]:
    sols = sp.solve(sp.sympify(equation), sp.Symbol(symbol))
    return [str(s) for s in sols]
