# Overview

`math-discovery-harness` is a **verifier-driven mathematical-discovery lab** for
LLM / Claude-Code agents. It is *not* a document dump. Every result an agent
produces is an **explicit Python candidate** that is **checked automatically** —
by numeric comparison, construction validation, or benchmark scoring — never a
prose proof that a human must trust.

## The core idea

> explicit candidate → automatic validation → improvement loop → logged reasoning

An agent does not "argue" that it solved a problem. It *submits a Python object*
(a number, a graph, a polynomial, a construction) and the harness runs a
validator that returns pass/fail and a score. Prose proofs **support** a
candidate; they never replace validation.

## The 4-stage loop

1. **Candidate.** Emit an explicit, runnable Python candidate that produces the
   required object in the required output format.
2. **Validation.** Run the problem's validator in a sandbox. Get pass/fail and a
   numeric score.
3. **Improvement.** If invalid or sub-optimal, refine: change parameters, swap
   methods, climb the task ladder, retrieve a paper, ask the skeptic.
4. **Logging.** Record reasoning, retrieved sources, failed paths, and the best
   candidate so the next attempt (or run) starts informed.

## Repo map

- `docs/` — protocols the agent follows (this loop, tool routing, retrieval,
  proofs, experiments, compliance, sandbox, benchmarking, integrity).
- `agent_instructions/` — role cards (researcher, skeptic, optimizer, literature
  scout, proof checker, verifier runner, final writer).
- `tools_docs/` — one-pager per external tool: what it's for, when to use it,
  how to call it, install notes.
- `topic_packs/` — per-area knowledge packs (definitions, methods, attack
  patterns, canonical/recent papers, tool recommendations).
- `mcp_servers/` — interface stubs for paper search, theorem search, OEIS,
  verifier and experiment runners (MCP tool contracts).
- `paper_index/` — local cards / theorem cards / citation graph / embeddings.
- `benchmarks/` — the four benchmark suites and their problems/validators.
- `runs/` — saved run artifacts and ablation results.
- `problems/` — problem folders (statement, ladder, candidates, validators,
  notes, final); `problems/template_problem/` is the canonical layout.
- `src/math_harness/` — the engine (owned elsewhere): core, ladder, memory,
  retrieval, runners, search, tools, validators, reporting.

## How an agent uses the harness

1. Read the problem's `statement.md`, `output_format.md`, and
   `compliance_rules.md`.
2. Build a 10-rung **task ladder** (`docs/03-task-ladder-protocol.md`).
3. Route work to the right tool (`docs/02-tool-router.md`); retrieve papers only
   under the **retrieval policy** (`docs/04-retrieval-policy.md`).
4. Run **experiments** (`docs/06-experiment-protocol.md`) to find candidates.
5. **Validate** every candidate in the sandbox (`docs/08-sandbox-security.md`).
6. Have the **skeptic** attack the best candidate before submitting.
7. Submit a **final answer** that passes the **compliance** rules
   (`docs/07-final-answer-compliance.md`) and write the final report.
