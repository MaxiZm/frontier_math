"""mpmath: high-precision numerical exploration (docs/02)."""

from __future__ import annotations

import mpmath


def evalf(expr: str, dps: int = 50) -> str:
    mpmath.mp.dps = dps
    from sympy import sympify

    return str(mpmath.mpf(sympify(expr).evalf(dps)))


def identify(value: float, constants: list[str] | None = None, dps: int = 50) -> str | None:
    """Try to recognize a numeric value as a closed form (mpmath.identify)."""
    mpmath.mp.dps = dps
    return mpmath.identify(mpmath.mpf(value), constants or [])
