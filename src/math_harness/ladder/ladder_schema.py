"""Dataclasses describing a task ladder."""

from __future__ import annotations

from dataclasses import dataclass, field


@dataclass(slots=True)
class LadderLevel:
    index: int  # 0..10 (half-levels use e.g. 25 for P2.5 -> store as float-able)
    name: str
    goal: str
    relaxation: str = ""

    @property
    def label(self) -> str:
        return f"P{self.index}"


@dataclass(slots=True)
class Ladder:
    problem_id: str
    levels: list[LadderLevel] = field(default_factory=list)

    def __iter__(self):
        return iter(self.levels)

    def __len__(self) -> int:
        return len(self.levels)

    def get(self, index: int) -> LadderLevel | None:
        for level in self.levels:
            if level.index == index:
                return level
        return None

    def to_markdown(self) -> str:
        lines = [f"# Task Ladder: {self.problem_id}", ""]
        for level in self.levels:
            lines.append(f"- **{level.label}** {level.name}: {level.goal}")
        return "\n".join(lines) + "\n"
