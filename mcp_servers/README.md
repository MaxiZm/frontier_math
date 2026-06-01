# MCP Servers

This directory holds the **Model Context Protocol (MCP) servers** the harness
exposes to the agent: paper/theorem/sequence search, plus the verifier and
experiment runners. They are how the agent reaches the outside world and the
sandbox under a uniform tool contract.

> **Status: interface stubs.** Each server here is an **interface stub**. It
> documents the intended MCP tool contract (tool names, inputs, outputs) but does
> not yet have its backing API or executor wired up. Until then, calls return a
> stub/`ToolUnavailable`-style response. Each subdirectory's `README.md` is the
> contract to implement against.

## Servers

Search / retrieval (serve the retrieval policy, `docs/04-retrieval-policy.md`):

- `arxiv_search/` — search arXiv preprints.
- `semantic_scholar_search/` — citation-aware scholarly search.
- `openalex_search/` — open scholarly metadata.
- `local_paper_index/` — query the curated `paper_index/` cards (check first).
- `theorem_search/` — search named/formalized theorems.
- `oeis_search/` — identify integer sequences (OEIS).

Execution (serve the research/validation loop):

- `verifier_runner/` — run a candidate against a problem validator in the sandbox.
- `experiment_runner/` — run an experiment script in the sandbox and capture
  results.

## Conventions

- **JSON-only I/O.** All tool inputs and outputs are JSON; execution servers use
  the sandbox (`docs/08-sandbox-security.md`) — no `pickle`, no `eval`.
- **Honesty.** Search servers must not fabricate identifiers; unknown arXiv
  IDs / DOIs are returned as `unknown` (`docs/11-evaluation-integrity.md`).
- **Logging.** Retrieval results go to a problem's `retrieved_context.md`;
  execution results go to `tool_calls.jsonl` / `validator_calls.jsonl`.
