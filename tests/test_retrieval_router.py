from __future__ import annotations

from math_harness.retrieval.router import (
    RetrievalTrigger,
    SOURCE_ORDER,
    route,
    should_retrieve,
    source_order,
)


def test_no_retrieval_by_default():
    decision = route()
    assert decision.retrieve is False
    assert decision.sources == ()


def test_unfamiliar_term_triggers_retrieval():
    decision = route(unfamiliar_term=True)
    assert decision.retrieve is True
    assert RetrievalTrigger.UNFAMILIAR_TERM in decision.triggers


def test_three_failures_trigger():
    assert should_retrieve(consecutive_failures=3)
    assert not should_retrieve(consecutive_failures=2)


def test_source_order_is_cheapest_first():
    assert source_order()[0] == "topic_card"
    assert source_order()[-1] == "full_paper"
    assert source_order() == SOURCE_ORDER


def test_source_order_truncates_at_max_depth():
    assert source_order("theorem_card") == ("topic_card", "paper_card", "theorem_card")
