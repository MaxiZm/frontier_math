"""Tiny append-only JSONL-backed store shared by the memory modules."""

from __future__ import annotations

import json
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Iterator


class JsonlStore:
    def __init__(self, path: str | Path) -> None:
        self.path = Path(path)

    def append(self, record: dict[str, Any]) -> dict[str, Any]:
        record = {"ts": datetime.now(timezone.utc).isoformat(), **record}
        self.path.parent.mkdir(parents=True, exist_ok=True)
        with self.path.open("a", encoding="utf-8") as fh:
            fh.write(json.dumps(record, default=str) + "\n")
        return record

    def __iter__(self) -> Iterator[dict[str, Any]]:
        if not self.path.is_file():
            return iter(())
        return (json.loads(line) for line in self.path.read_text().splitlines() if line.strip())

    def all(self) -> list[dict[str, Any]]:
        return list(self)
