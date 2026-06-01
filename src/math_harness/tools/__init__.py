"""Tool runners.

Pure-Python tools (sympy, mpmath, networkx) are wired for real. Heavy external
tools (Sage, PARI/GP, GAP, Z3, SAT, Lean) are stubs that raise
``ToolUnavailable`` with install guidance until the binary is present. See
``docs/02-tool-router.md`` for when to use each.
"""

from .availability import is_available, require, which

__all__ = ["is_available", "require", "which"]
