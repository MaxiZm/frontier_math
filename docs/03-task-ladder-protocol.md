# Task Ladder Protocol
For every hard problem, construct 10 progressively harder tasks.
Default ladder:
P0: Restate definitions and output format.
P1: Produce any syntactically valid candidate.
P2: Solve the smallest parameter case.
P3: Solve a relaxed version.
P4: Solve a symmetric/special case.
P5: Generate computational examples.
P6: Infer a reusable pattern.
P7: Prove or validate the pattern in a restricted setting.
P8: Scale to near-original parameters.
P9: Beat a weak or approximate baseline.
P10: Solve the original problem.
If stuck for 3 attempts at level k:
- create level k-0.5,
- relax exactly one constraint,
- solve that,
- extract a lemma/search heuristic,
- return to level k.
