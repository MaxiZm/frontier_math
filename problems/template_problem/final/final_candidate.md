# Final Candidate

> Template. The submitted answer and how it constructs the object. Written by the
> final writer (`agent_instructions/final_writer.md`) once the best candidate is
> skeptic-cleared.

## Submitted file
<path to the submitted candidate file, e.g. `final/solution.py`>

## What it returns
<The exact object, matching `output_format.md`. For large objects, summarize and
point to the file.>

## How it constructs the object
<Plain-language description of the construction. It must be a deterministic finite
construction or an explicit literal — no hidden search at scoring time.>

## Compliance check
Confirm against `compliance_rules.md` (`docs/07-final-answer-compliance.md`):
- [ ] Deterministic finite construction or explicit literal
- [ ] No hidden numerical search / root-finding / numerical integration
- [ ] No randomness
- [ ] No optimization loop at scoring time
- [ ] No network / subprocess / file I/O
- [ ] Only allowed imports
- [ ] Matches `output_format.md` exactly

## Research-time vs. final
<If the object was found by search/optimization at research time, note how it was
converted into this compliant deterministic/literal final form.>
