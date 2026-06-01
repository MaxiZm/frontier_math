"""Discover external tool binaries and gate stubbed runners behind a clear error."""

from __future__ import annotations

import os
import shutil

from ..core.exceptions import ToolUnavailable

# Logical tool name -> (env var override, binary name, install guidance).
TOOL_BINARIES: dict[str, tuple[str, str, str]] = {
    "sage": ("SAGE_BIN", "sage", "Install SageMath (https://www.sagemath.org)."),
    "gap": ("GAP_BIN", "gap", "Install GAP (https://www.gap-system.org)."),
    "pari": ("PARI_BIN", "gp", "Install PARI/GP (https://pari.math.u-bordeaux.fr)."),
    "z3": ("Z3_BIN", "z3", "Install Z3 (pip install z3-solver, or the z3 binary)."),
    "lean": ("LEAN_BIN", "lean", "Install Lean + mathlib (https://leanprover.github.io)."),
    "nauty": ("NAUTY_BIN", "geng", "Install nauty/traces (https://pallini.di.uniroma1.it)."),
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
