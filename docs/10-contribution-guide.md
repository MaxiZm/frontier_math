# Contribution Guide

This guide covers adding **problems**, **validators**, and **topic packs**, plus
coding conventions and how to run the tests. (The engine under `src/` is owned by
the harness maintainers; coordinate before changing it.)

## Adding a problem

1. Copy `problems/template_problem/` to `problems/<your_problem>/`.
2. Fill in the docs: `statement.md`, `output_format.md`, `compliance_rules.md`,
   `task_ladder.md`, `tool_plan.md`. Start `retrieved_context.md` empty.
3. Write `problem.yaml` (problem id, parameters, scoring, time/memory budget,
   compliance flags) and `validator.py` (see below).
4. Leave `candidates/`, `experiments/`, `notes/`, `proofs/`, `final/` for the
   solving agent to populate.

## Adding a validator

- A validator takes the candidate's JSON output and returns a verdict + score.
- It runs **sandboxed** (`docs/08-sandbox-security.md`): JSON-only I/O, no
  `pickle`, no `eval` of candidate strings; defend against malformed input.
- Validate the output **shape** first, then correctness, then score/optimality.
- Make it **deterministic** and as cheap as possible; it may be called many times
  per run.
- Where feasible, accept a *certificate* the candidate supplies and check it,
  rather than re-deriving the answer.

## Adding a topic pack

A topic pack is a directory under `topic_packs/<area>/` with the 7 files
described in `topic_packs/README.md`. Use **real, honest** content:

- Cite well-known real theorems, methods, and papers.
- In `canonical_papers.yaml` / `recent_papers.yaml`, do **not** fabricate arXiv
  IDs or DOIs — omit identifiers you are unsure of or mark them `unknown`.

## Coding conventions

- Python, type hints where practical, small focused functions.
- Final candidates and validators: standard library + explicitly allowed
  scientific packages only (per the problem's compliance rules).
- JSON-serializable I/O for anything crossing the sandbox boundary; return big
  numbers / high-precision reals as strings.
- Deterministic by default; log any seed.

## Running the tests

From the repo root:

```
pytest
```

Run the full suite before submitting a contribution; add tests for new
validators (at least: a known-good candidate passes, a known-bad candidate
fails, malformed input is rejected).
