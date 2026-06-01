"""Discover external tool binaries and gate stubbed runners behind a clear error."""

from __future__ import annotations

import os
import shutil

from ..core.exceptions import ToolUnavailable

# Logical tool name -> (env var override, binary name, install guidance).
TOOL_BINARIES: dict[str, tuple[str, str, str]] = {
    "sage": (
        "SAGE_BIN",
        "sage",
        "Install SageMath and see tools_docs/sage.md for setup, smoke tests, and usage patterns.",
    ),
    "gap": (
        "GAP_BIN",
        "gap",
        "Install GAP and see tools_docs/gap.md for setup, smoke tests, and usage patterns.",
    ),
    "pari": (
        "PARI_BIN",
        "gp",
        "Install PARI/GP and see tools_docs/pari_gp.md for setup, smoke tests, and usage patterns.",
    ),
    "z3": (
        "Z3_BIN",
        "z3",
        "Install z3-solver or the z3 binary and see tools_docs/z3.md for setup, smoke tests, and usage patterns.",
    ),
    "sat": (
        "SAT_BIN",
        "kissat",
        "Install a SAT solver and see tools_docs/sat_solvers.md for setup, smoke tests, and usage patterns.",
    ),
    "lean": (
        "LEAN_BIN",
        "lean",
        "Install Lean + mathlib and see tools_docs/lean_mathlib.md for setup, smoke tests, and usage patterns.",
    ),
    "nauty": (
        "NAUTY_BIN",
        "geng",
        "Install nauty/traces and see tools_docs/nauty_traces.md for setup, smoke tests, and usage patterns.",
    ),
}


def which(tool: str) -> str | None:
    """Return the resolved binary path for a logical tool, or None."""
    env_var, binary, _ = TOOL_BINARIES.get(tool, ("", tool, ""))
    override = os.environ.get(env_var) if env_var else None
    if override and shutil.which(override):
        return shutil.which(override)
    return shutil.which(binary)


def is_available(tool: str) -> bool:
    return which(tool) is not None


def require(tool: str) -> str:
    """Return the binary path or raise :class:`ToolUnavailable` with guidance."""
    path = which(tool)
    if path is None:
        guidance = TOOL_BINARIES.get(tool, ("", "", ""))[2]
        raise ToolUnavailable(tool, guidance)
    return path
