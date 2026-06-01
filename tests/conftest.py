"""Shared pytest fixtures."""

from __future__ import annotations

from pathlib import Path

import pytest

REPO_ROOT = Path(__file__).resolve().parents[1]
EXAMPLES = REPO_ROOT / "examples"


@pytest.fixture
def repo_root() -> Path:
    return REPO_ROOT


@pytest.fixture
def closed_form_dir() -> Path:
    return EXAMPLES / "closed_form_constant"


@pytest.fixture
def graph_dir() -> Path:
    return EXAMPLES / "graph_construction"


@pytest.fixture
def template_dir() -> Path:
    return REPO_ROOT / "problems" / "template_problem"


@pytest.fixture
def write_candidate(tmp_path):
    """Return a helper that writes a candidate file and returns its path."""

    def _write(name: str, source: str) -> Path:
        path = tmp_path / name
        path.write_text(source)
        return path

    return _write
