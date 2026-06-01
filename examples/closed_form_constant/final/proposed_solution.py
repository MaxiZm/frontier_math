"""Final candidate: a closed form equal to the Basel constant zeta(2).

Self-contained and validator-clean: returns an explicit symbolic expression, no
numerical search.
"""

from sympy import pi


def solve():
    # zeta(2) = sum_{n>=1} 1/n^2 = pi^2 / 6  (Euler, 1734).
    return pi**2 / 6
