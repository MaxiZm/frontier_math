# Proof Protocol

Proofs in this harness are **second-class**: they support and explain a validated
candidate, they do not replace validation. A beautiful proof with no passing
candidate is worth nothing here; a passing candidate with no proof still counts.

## When to write a proof

- The problem explicitly asks for a closed form, an exactness claim, or an
  optimality claim that validation alone cannot establish (e.g. "prove your
  construction is extremal", "show the constant equals this expression").
- A task-ladder rung is "prove or validate the pattern in a restricted setting"
  (P7), or you need a lemma to scale to larger parameters (P8).
- The skeptic flags that a candidate passes validation only because the test is
  too weak (small cases, finite precision) and a structural argument is needed.

## When NOT to write a proof

- Before you have any passing candidate. Get a candidate first.
- As a substitute for running the validator.
- To "explain" a numerical coincidence you have not pinned down with an exact
  tool (use PARI `algdep` / Sage / mpmath `identify` first).

## What counts as a proof artifact

Prefer **machine-checkable certificates** over prose whenever possible:

- **Exact certificate** — an explicit object whose validity is checkable by a
  finite computation (a dual solution / LP certificate, an explicit factor, a
  resolvent, a covering design verified by enumeration).
- **Formal proof** — a Lean/mathlib term or `#check` of a known theorem used as a
  black box (`tools_docs/lean_mathlib.md`).
- **Proof sketch** — a structured argument with each step either elementary,
  citing a logged theorem card, or backed by a sub-computation. Use this when a
  full certificate is impractical.

## How to write a proof sketch

1. State the claim precisely (the same object the validator checks).
2. List assumptions and any external theorems (with theorem-card references).
3. Give the argument as numbered steps; mark each step as
   `[elementary] / [computed in experiment NNN] / [theorem card X] / [assumed]`.
4. Flag every `[assumed]` step explicitly — these are the skeptic's targets.
5. Save to `proofs/` and summarize in `final/proof_or_explanation.md`.

A proof is "done" when no step is `[assumed]` and the claim matches what the
validator tests.
