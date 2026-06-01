"""Routing logic for the retrieval policy.

Do not read papers by default. Retrieve only when a trigger fires, and then walk
sources cheapest-first:

    topic card -> paper card -> theorem card -> paper section -> full paper
"""

from __future__ import annotations

from dataclasses import dataclass
from enum import Enum


class RetrievalTrigger(Enum):
    """The six triggers from docs/04-retrieval-policy.md."""

    UNFAMILIAR_TERM = "unfamiliar_term"
    PATTERN_SUGGESTS_LITERATURE = "pattern_suggests_literature"
    PROOF_NEEDS_EXTERNAL_THEOREM = "proof_needs_external_theorem"
    THREE_FAILED_ATTEMPTS = "three_failed_attempts"
    SPECIALIZED_AREA = "specialized_area"
    NEED_KNOWN_CONSTRUCTION = "need_known_construction"


# Cheapest-first source escalation order.
SOURCE_ORDER: tuple[str, ...] = (
    "topic_card",
    "paper_card",
    "theorem_card",
    "paper_section",
    "full_paper",
)


@dataclass(slots=True)
class RetrievalDecision:
    retrieve: bool
    triggers: list[RetrievalTrigger]
    sources: tuple[str, ...]
    reason: str


def should_retrieve(
    *,
    unfamiliar_term: bool = False,
    pattern_suggests_literature: bool = False,
    proof_needs_external_theorem: bool = False,
    consecutive_failures: int = 0,
    specialized_area: bool = False,
    need_known_construction: bool = False,
) -> list[RetrievalTrigger]:
    """Return the list of triggers that fired (empty => do not retrieve)."""
    fired: list[RetrievalTrigger] = []
    if unfamiliar_term:
        fired.append(RetrievalTrigger.UNFAMILIAR_TERM)
    if pattern_suggests_literature:
        fired.append(RetrievalTrigger.PATTERN_SUGGESTS_LITERATURE)
    if proof_needs_external_theorem:
        fired.append(RetrievalTrigger.PROOF_NEEDS_EXTERNAL_THEOREM)
    if consecutive_failures >= 3:
        fired.append(RetrievalTrigger.THREE_FAILED_ATTEMPTS)
    if specialized_area:
        fired.append(RetrievalTrigger.SPECIALIZED_AREA)
    if need_known_construction:
        fired.append(RetrievalTrigger.NEED_KNOWN_CONSTRUCTION)
    return fired


def source_order(max_depth: str = "full_paper") -> tuple[str, ...]:
    """Return the escalation order, truncated at ``max_depth`` (inclusive)."""
    if max_depth not in SOURCE_ORDER:
        return SOURCE_ORDER
    cut = SOURCE_ORDER.index(max_depth) + 1
    return SOURCE_ORDER[:cut]


def route(max_depth: str = "full_paper", **trigger_kwargs) -> RetrievalDecision:
    """Combine trigger detection + source ordering into a single decision."""
    triggers = should_retrieve(**trigger_kwargs)
    if not triggers:
        return RetrievalDecision(
            retrieve=False,
            triggers=[],
            sources=(),
            reason="no trigger fired; do not read papers by default",
        )
    return RetrievalDecision(
        retrieve=True,
        triggers=triggers,
        sources=source_order(max_depth),
        reason=f"triggers: {', '.join(t.value for t in triggers)}",
    )
