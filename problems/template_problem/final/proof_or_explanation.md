# Proof or Explanation

> Template. The argument or certificate that **supports** the validated final
> candidate (`docs/05-proof-protocol.md`). A proof justifies correctness /
> optimality; it never replaces validation (see `verification_report.md`).
> Written/checked by the proof checker (`agent_instructions/proof_checker.md`).

## Claim
<State the claim precisely — it must match exactly what the validator checks.>

## Type of justification
<one of: machine-checkable certificate / formal (Lean) proof / structured proof
sketch / numeric-then-recognized closed form>

## Certificate (preferred, if applicable)
<The explicit checkable object: a dual/LP certificate, an explicit factor, an
enumeration witness — and how to verify it.>

## Argument (if a sketch)
Numbered steps; tag each:
1. <step> — `[elementary]`
2. <step> — `[computed in experiment NNN]`
3. <step> — `[theorem card X]`
4. <step> — `[assumed]`  ← target for the skeptic; drive these to zero

## Remaining assumptions
<List every `[assumed]` step still open, or state "none".>

## Skeptic sign-off
<blocked: reason | cleared by skeptic on date>
