from __future__ import annotations

from math_harness.ladder.generate_ladder import default_ladder
from math_harness.ladder.stuck_detector import consecutive_failures, is_stuck


def test_default_ladder_has_p0_through_p10():
    ladder = default_ladder("demo")
    assert len(ladder) == 11
    assert ladder.levels[0].label == "P0"
    assert ladder.levels[-1].label == "P10"
    assert "original" in ladder.levels[-1].goal.lower()


def test_ladder_get_and_markdown():
    ladder = default_ladder("demo")
    assert ladder.get(2).index == 2
    assert ladder.get(99) is None
    assert "Task Ladder" in ladder.to_markdown()


def test_is_stuck_after_three_failures():
    assert is_stuck([False, False, False])
    assert is_stuck([True, False, False, False])
    assert not is_stuck([False, False])
    assert not is_stuck([True, True, False])


def test_consecutive_failures():
    assert consecutive_failures([True, False, False]) == 2
    assert consecutive_failures([False, True]) == 0
