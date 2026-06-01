"""The :class:`Candidate` model: a proposed-solution file + its entrypoint.

Execution-path contract
------------------------
``Candidate.run()`` performs *trusted, in-process* execution and is intended for
tests and internal utilities only. **Official evaluation goes through**
``math_harness.validators.sandbox.run_candidate`` so untrusted candidate code is
isolated in a subprocess with a timeout. Do not bypass the sandbox in runners.
"""

from __future__ import annotations

import hashlib
import importlib.util
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any, Callable

from .exceptions import CandidateExecutionError, EntrypointNotFoundError
from .problem import Problem


@dataclass(slots=True)
class Candidate:
    path: Path
    function_name: str = "solve"
    source: str = field(default="", repr=False)

    @classmethod
    def from_problem(
        cls, problem: Problem, override_path: str | Path | None = None
    ) -> "Candidate":
        path = Path(override_path) if override_path else problem.entrypoint_path()
        return cls(path=Path(path), function_name=problem.entrypoint.function_name)

    @classmethod
    def from_file(cls, path: str | Path, function_name: str = "solve") -> "Candidate":
        return cls(path=Path(path), function_name=function_name)

    def read_source(self) -> str:
        """Read and cache the candidate source (used for compliance AST checks)."""
        if not self.source:
            if not self.path.is_file():
                raise CandidateExecutionError(f"Candidate file not found: {self.path}")
            self.source = self.path.read_text()
        return self.source

    def load_callable(self) -> Callable[..., Any]:
        """Import the candidate module by file path and return the entrypoint.

        Uses a content-hashed module name so repeated loads of distinct files do
        not collide in ``sys.modules``.
        """
        if not self.path.is_file():
            raise CandidateExecutionError(f"Candidate file not found: {self.path}")

        digest = hashlib.sha1(str(self.path.resolve()).encode()).hexdigest()[:12]
        mod_name = f"mh_candidate_{digest}"
        spec = importlib.util.spec_from_file_location(mod_name, self.path)
        if spec is None or spec.loader is None:  # pragma: no cover - defensive
            raise CandidateExecutionError(f"Cannot create import spec for {self.path}")

        module = importlib.util.module_from_spec(spec)
        try:
            spec.loader.exec_module(module)
        except Exception as exc:  # noqa: BLE001 - surface as harness error
            raise CandidateExecutionError(
                f"Error importing candidate {self.path}: {exc}"
            ) from exc

        fn = getattr(module, self.function_name, None)
        if fn is None or not callable(fn):
            raise EntrypointNotFoundError(
                f"Candidate {self.path} has no callable entrypoint "
                f"{self.function_name!r}."
            )
        return fn

    def run(self, *args: Any, **kwargs: Any) -> Any:
        """Trusted in-process execution. Use the sandbox for untrusted candidates."""
        fn = self.load_callable()
        try:
            return fn(*args, **kwargs)
        except Exception as exc:  # noqa: BLE001
            raise CandidateExecutionError(
                f"Candidate entrypoint {self.function_name!r} raised: {exc}"
            ) from exc
