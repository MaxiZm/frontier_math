from __future__ import annotations

import pytest

from math_harness.core.candidate import Candidate
from math_harness.core.exceptions import EntrypointNotFoundError
from math_harness.core.problem import Problem
from math_harness.validators.sandbox import run_candidate


def test_load_callable_and_run(write_candidate):
    path = write_candidate("c.py", "def solve():\n    return 41 + 1\n")
    cand = Candidate.from_file(path, "solve")
    assert cand.run() == 42


def test_missing_entrypoint_raises(write_candidate):
    path = write_candidate("c.py", "def other():\n    return 1\n")
    cand = Candidate.from_file(path, "solve")
    with pytest.raises(EntrypointNotFoundError):
        cand.load_callable()


def test_distinct_files_do_not_collide(write_candidate):
    a = write_candidate("a.py", "def solve():\n    return 'a'\n")
    b = write_candidate("b.py", "def solve():\n    return 'b'\n")
    assert Candidate.from_file(a).run() == "a"
    assert Candidate.from_file(b).run() == "b"


def test_sandbox_runs_candidate(write_candidate):
    path = write_candidate("c.py", "def solve():\n    return [1, 2, 3]\n")
    cand = Candidate.from_file(path, "solve")
    result = run_candidate(cand, timeout_s=10)
    assert result.ok
    assert result.output == [1, 2, 3]


def test_sandbox_timeout(write_candidate):
    path = write_candidate(
        "slow.py", "import time\n\ndef solve():\n    time.sleep(5)\n    return 1\n"
    )
    cand = Candidate.from_file(path, "solve")
    result = run_candidate(cand, timeout_s=1)
    assert result.timed_out
    assert not result.ok


def test_sandbox_captures_crash(write_candidate):
    path = write_candidate("boom.py", "def solve():\n    raise ValueError('boom')\n")
    cand = Candidate.from_file(path, "solve")
    result = run_candidate(cand, timeout_s=10)
    assert not result.ok
    assert "boom" in result.error
