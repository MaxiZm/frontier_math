# Experiment Protocol

Experiments are the agent's scratch lab. They live under each problem's
`experiments/` directory and are where ideas become data before they become
candidates. Research-time experiment code is **not** held to final-answer
compliance rules (`docs/07-final-answer-compliance.md`) — explore freely.

## Layout

```
problems/<problem>/experiments/
  000_smallest_case.py
  001_brute_force_enumeration.py
  002_pattern_from_oeis.py
  ...
  results/
    000_smallest_case.json
    001_brute_force_enumeration.json
    ...
```

## Naming

- Zero-padded, monotonically increasing prefix: `000_`, `001_`, `002_`, … so the
  order of exploration is preserved and auditable.
- A short, descriptive slug after the prefix: `003_relaxed_lp_bound.py`.
- One experiment = one question. Do not retrofit an old file to a new idea;
  create the next number.

## Each experiment should

1. Print or emit a **JSON result** to `results/<same-name>.json` (parameters
   tried, values found, timing). JSON only — see `docs/08-sandbox-security.md`.
2. Be **reproducible**: fix and record any random seed; record tool versions if
   relevant; avoid hidden global state.
3. Record which **tool** it used and why (`docs/02-tool-router.md`).
4. Reference the **ladder rung** it serves (e.g. "for P5: generate examples").

## After an experiment

- Promising result → distill into an explicit candidate under `candidates/` and
  validate it.
- Dead end → record in `notes/failed_paths.md` with the reason (so it is not
  re-run) and move on.
- Useful regularity → record in `notes/lemmas.md` or `notes/conjectures.md`.

## Reproducibility checklist

- Seed set and logged for any stochastic search.
- Inputs and parameters echoed in the JSON output.
- No dependence on machine-specific paths or wall-clock except where logged.
- The experiment can be re-run from a clean checkout and reproduce its JSON.
