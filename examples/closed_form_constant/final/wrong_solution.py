"""A wrong candidate (pi^2/5 != pi^2/6) used to exercise failing validation."""

from sympy import pi


def solve():
    return pi**2 / 5
