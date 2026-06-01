# Verification Report

> Template. The validator's verdict on the submitted final candidate, recorded
> verbatim by the verifier runner / final writer
> (`agent_instructions/verifier_runner.md`). Report only what validation
> confirms; do not overclaim.

## Submission
- **Problem id:** <…>
- **Candidate file:** <final/…>
- **Validator:** <problem `validator.py` / proxy validator + which suite>

## Result
- **Verdict:** <pass | fail | timeout | error>
- **Score:** <value or n/a>
- **Diagnostics:** <validator output>

## Budget used
- **Runtime:** <s> / budget <s>
- **Memory:** <MB> / budget <MB>

## Run accounting (integrity, `docs/11-evaluation-integrity.md`)
- **Model:** <id/version>
- **Ablation level:** <raw_model … full_harness>
- **Seed:** <…>
- **Time budget:** <…>
- **Tool availability:** <…>
- **Validator calls this run:** <count>

## Caveats
<Proxy-validator caveat if applicable; any known gap between what was validated
and the full problem claim.>
