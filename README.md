# math-discovery-harness

A **verifier-driven mathematical-discovery harness** for LLM / Claude Code agents.

The harness is built around a single loop:

```
explicit candidate  →  automatic validation  →  improvement loop  →  logged reasoning
```

It targets HorizonMath-style problems, whose answers are concrete, Python-formulated outputs checked
automatically — by numerical comparison, benchmark scoring, or construction validation — rather than
by prose proof review.

This repo is a **research lab, not a document dump**:

```
protocols + tool routing + paper retrieval + task ladder
+ validators + experiment memory + candidate search + skeptic checking
```

## Install

With [uv](https://docs.astral.sh/uv/) (recommended):

```bash
uv sync                 # creates the venv and (if network allows) writes uv.lock
uv run pytest -q
```

> `uv.lock` is **not** committed by hand. Run `uv lock` / `uv sync` to generate it. If the
> environment has no network access, it is left absent — the package still installs from
> `pyproject.toml`.

Or with pip:

```bash
python -m venv .venv && . .venv/bin/activate
pip install -e ".[dev]"
pytest -q
```

## Try the end-to-end example

```bash
# Numeric closed-form example (target = pi^2/6 = zeta(2))
python scripts/evaluate_candidate.py \
  --problem examples/closed_form_constant \
  --candidate examples/closed_form_constant/final/proposed_solution.py

# Construction example (triangle-free graph)
python scripts/evaluate_candidate.py \
  --problem examples/graph_construction \
  --candidate examples/graph_construction/final/proposed_solution.py
```

Both print a green `ValidationResult` and write artifacts under `runs/local/<id>/`.

## Core workflow

```bash
python scripts/create_problem.py --benchmark toy_discovery --id my_problem
# ... agent writes statement / validator / task ladder / final/proposed_solution.py ...
python scripts/run_ladder.py --problem benchmarks/toy_discovery/problems/my_problem --max-level 10
python scripts/evaluate_candidate.py --problem <dir> --candidate <dir>/final/proposed_solution.py
python scripts/summarize_run.py --run runs/local/my_problem
python scripts/export_solution_pack.py --problem <dir>
```

## Repository map

| Path | What it is |
|------|------------|
| `CLAUDE.md` | The constitution the agent reads automatically. |
| `docs/` | Protocols: research loop, tool router, task ladder, retrieval, compliance, sandbox, benchmarking, evaluation integrity. |
| `agent_instructions/` | Role cards (researcher, skeptic, optimizer, …). |
| `tools_docs/` | When/how to use each math tool. |
| `topic_packs/` | Domain knowledge packs. |
| `src/math_harness/` | The deterministic harness package (core, validators, runners, ladder, search, memory, reporting, tool stubs). |
| `paper_index/` | Paper / theorem cards, schemas, citation graph, embeddings. |
| `mcp_servers/` | MCP server interface stubs for retrieval and execution. |
| `problems/` | Problem template + working problems. |
| `benchmarks/` | HorizonMath / FrontierMath-open / toy / custom suites. |
| `examples/` | Runnable end-to-end examples. |
| `runs/` | Per-run artifacts and ablations. |
| `scripts/` | Thin CLI wrappers over the package. |
| `tests/` | Pytest suite. |

## What is real vs. stubbed

- **Real, tested:** problem loading + schema validation, the subprocess sandbox, numeric /
  construction / optimization / compliance validators, the run/bookkeeping loop, ladder schema,
  pure-Python tool runners (sympy, mpmath, networkx), seeded local search, and both examples.
- **Stubbed with documented interfaces:** heavy external tools (Sage, GAP, PARI/GP, Z3, SAT, Lean)
  raise `ToolUnavailable` with install guidance via `is_available()`; MCP servers ship interface
  READMEs; benchmark dataset importers are documented stubs (no private data bundled).

See `docs/11-evaluation-integrity.md` for the no-data-leakage policy.
