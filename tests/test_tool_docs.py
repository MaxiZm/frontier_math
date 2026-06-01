from __future__ import annotations

import importlib
import re
from pathlib import Path

import pytest

from math_harness.core.exceptions import ToolUnavailable

ROOT = Path(__file__).resolve().parents[1]
TOOLS_DOCS = ROOT / "tools_docs"

TOOL_DOCS = [
    "sage.md",
    "sympy.md",
    "mpmath.md",
    "pari_gp.md",
    "gap.md",
    "z3.md",
    "sat_solvers.md",
    "networkx.md",
    "nauty_traces.md",
    "lean_mathlib.md",
    "oeis.md",
    "paper_search.md",
]

REQUIRED_SECTIONS = [
    "Use when",
    "Do not use when",
    "Availability check",
    "Minimal smoke test",
    "Agent protocol",
    "Pitfalls",
    "Final-answer compliance notes",
]

HEAVY_RUNNERS = [
    ("math_harness.tools.sage_runner", "tools_docs/sage.md"),
    ("math_harness.tools.pari_runner", "tools_docs/pari_gp.md"),
    ("math_harness.tools.gap_runner", "tools_docs/gap.md"),
    ("math_harness.tools.z3_runner", "tools_docs/z3.md"),
    ("math_harness.tools.sat_runner", "tools_docs/sat_solvers.md"),
    ("math_harness.tools.lean_search", "tools_docs/lean_mathlib.md"),
]


def test_tool_docs_readme_lists_existing_files() -> None:
    readme = (TOOLS_DOCS / "README.md").read_text(encoding="utf-8")
    assert (TOOLS_DOCS / "template_tool_doc.md").exists()
    for filename in TOOL_DOCS:
        assert filename in readme
        assert (TOOLS_DOCS / filename).exists()


@pytest.mark.parametrize("filename", TOOL_DOCS)
def test_tool_doc_contains_required_sections(filename: str) -> None:
    text = (TOOLS_DOCS / filename).read_text(encoding="utf-8")
    for section in REQUIRED_SECTIONS:
        assert re.search(rf"^## {re.escape(section)}$", text, re.MULTILINE), filename
    assert text.count("- ") >= 3, filename


@pytest.mark.parametrize(("module_name", "doc_path"), HEAVY_RUNNERS)
def test_heavy_runner_unavailable_error_mentions_docs(
    monkeypatch: pytest.MonkeyPatch, module_name: str, doc_path: str
) -> None:
    from math_harness.tools import availability

    module = importlib.import_module(module_name)
    monkeypatch.setattr(availability, "which", lambda _tool: None)

    with pytest.raises(ToolUnavailable) as exc_info:
        module.run("smoke")

    assert doc_path in str(exc_info.value)


def test_oeis_unavailable_error_mentions_docs() -> None:
    from math_harness.tools.oeis_client import lookup

    with pytest.raises(ToolUnavailable) as exc_info:
        lookup([1, 1, 2, 5, 14, 42])

    assert "tools_docs/oeis.md" in str(exc_info.value)
