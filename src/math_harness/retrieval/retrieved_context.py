"""Append entries to a problem's retrieved_context.md log (retrieval policy rule)."""

from __future__ import annotations

from datetime import datetime, timezone
from pathlib import Path


def log_source(problem_dir: str | Path, title: str, source_type: str, note: str = "") -> None:
    """Every retrieved source MUST be logged here (docs/04)."""
    path = Path(problem_dir) / "retrieved_context.md"
    ts = datetime.now(timezone.utc).isoformat()
    with path.open("a", encoding="utf-8") as fh:
        fh.write(f"\n- [{ts}] ({source_type}) **{title}** -- {note}")
