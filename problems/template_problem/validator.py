"""Template validator. Expose `validate(output) -> dict` OR a `Validator` subclass.

The harness runs the candidate entrypoint in the sandbox and passes its return
value to `validate`. Return a dict with at least `passed` (bool); optionally
`score`, `objective_value`, `baseline`, `improved`, `messages`, `details`.
"""

from __future__ import annotations


def validate(output) -> dict:
    # TODO: replace with the real check for this problem.
    return {
        "passed": False,
        "messages": ["validator not implemented yet for template_problem"],
        "details": {"output": str(output)},
    }
