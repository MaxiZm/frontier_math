"""Load/validate paper cards from paper_index/cards/."""

from __future__ import annotations

import json
from pathlib import Path

_REPO_ROOT = Path(__file__).resolve().parents[3]
_CARDS = _REPO_ROOT / "paper_index" / "cards"


def list_paper_cards() -> list[Path]:
    if not _CARDS.is_dir():
        return []
    return sorted(_CARDS.rglob("*.json")) + sorted(_CARDS.rglob("*.yaml"))


def load_paper_card(path: str | Path) -> dict:
    path = Path(path)
    if path.suffix == ".json":
        return json.loads(path.read_text())
    import yaml

    return yaml.safe_load(path.read_text())
