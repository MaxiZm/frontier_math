"""The :class:`Problem` model, loaded and schema-validated from ``problem.yaml``."""

from __future__ import annotations

import json
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any

import yaml

from .exceptions import ProblemLoadError

_SCHEMA_PATH = (
    Path(__file__).resolve().parents[3]
    / "paper_index"
    / "schema"
    / "problem.schema.json"
)


@dataclass(frozen=True, slots=True)
class Objective:
    direction: str | None = None  # "minimize" | "maximize"
    metric: str | None = None
    baseline: float | None = None


@dataclass(frozen=True, slots=True)
class Entrypoint:
    function_name: str = "solve"
    file: str = "final/proposed_solution.py"


@dataclass(frozen=True, slots=True)
class ValidatorSpec:
    file: str = "validator.py"
    timeout_seconds: float = 30.0
    deterministic: bool = True


@dataclass(frozen=True, slots=True)
class Compliance:
    allow_floats: bool = True
    allow_search_inside_final_solution: bool = False
    allow_hardcoded_candidate: bool = True
    require_deterministic: bool = True
    forbidden_imports: tuple[str, ...] = ()
    forbidden_calls: tuple[str, ...] = ()
    notes: str = ""


def _as_tuple(value: Any) -> tuple[str, ...]:
    if value is None:
        return ()
    if isinstance(value, (list, tuple)):
        return tuple(str(v) for v in value)
    return (str(value),)


@dataclass(frozen=True, slots=True)
class Problem:
    id: str
    benchmark: str
    output_type: str
    evaluation_mode: str
    domain: tuple[str, ...] = ()
    compliance_style: str | None = None
    objective: Objective = field(default_factory=Objective)
    entrypoint: Entrypoint = field(default_factory=Entrypoint)
    validator: ValidatorSpec = field(default_factory=ValidatorSpec)
    compliance: Compliance = field(default_factory=Compliance)
    retrieval: dict[str, Any] = field(default_factory=dict)
    tools: dict[str, Any] = field(default_factory=dict)
    root: Path = field(default=Path("."))
    raw: dict[str, Any] = field(default_factory=dict, repr=False)

    # -- loading ---------------------------------------------------------------

    @classmethod
    def load(cls, path: str | Path) -> "Problem":
        """Load a problem from a directory or a ``problem.yaml`` path.

        Validates against ``paper_index/schema/problem.schema.json`` and raises
        :class:`ProblemLoadError` with a clear message on any failure.
        """
        p = Path(path)
        if p.is_dir():
            root = p
            yaml_path = p / "problem.yaml"
        else:
            root = p.parent
            yaml_path = p

        if not yaml_path.is_file():
            raise ProblemLoadError(f"problem.yaml not found at {yaml_path}")

        try:
            raw = yaml.safe_load(yaml_path.read_text()) or {}
        except yaml.YAMLError as exc:  # pragma: no cover - defensive
            raise ProblemLoadError(f"Malformed YAML in {yaml_path}: {exc}") from exc

        if not isinstance(raw, dict):
            raise ProblemLoadError(f"{yaml_path} must contain a mapping at top level.")

        _validate_schema(raw, yaml_path)

        obj = raw.get("objective") or {}
        ep = raw.get("entrypoint") or {}
        val = raw.get("validator") or {}
        comp = raw.get("compliance") or {}

        return cls(
            id=str(raw["id"]),
            benchmark=str(raw["benchmark"]),
            output_type=str(raw["output_type"]),
            evaluation_mode=str(raw["evaluation_mode"]),
            domain=_as_tuple(raw.get("domain")),
            compliance_style=raw.get("compliance_style"),
            objective=Objective(
                direction=obj.get("direction"),
                metric=obj.get("metric"),
                baseline=obj.get("baseline"),
            ),
            entrypoint=Entrypoint(
                function_name=str(ep.get("function_name", "solve")),
                file=str(ep.get("file", "final/proposed_solution.py")),
            ),
            validator=ValidatorSpec(
                file=str(val.get("file", "validator.py")),
                timeout_seconds=float(val.get("timeout_seconds", 30.0)),
                deterministic=bool(val.get("deterministic", True)),
            ),
            compliance=Compliance(
                allow_floats=bool(comp.get("allow_floats", True)),
                allow_search_inside_final_solution=bool(
                    comp.get("allow_search_inside_final_solution", False)
                ),
                allow_hardcoded_candidate=bool(comp.get("allow_hardcoded_candidate", True)),
                require_deterministic=bool(comp.get("require_deterministic", True)),
                forbidden_imports=_as_tuple(comp.get("forbidden_imports")),
                forbidden_calls=_as_tuple(comp.get("forbidden_calls")),
                notes=str(comp.get("notes", "")),
            ),
            retrieval=dict(raw.get("retrieval") or {}),
            tools=dict(raw.get("tools") or {}),
            root=root.resolve(),
            raw=raw,
        )

    # -- path helpers ----------------------------------------------------------

    def entrypoint_path(self) -> Path:
        return self.root / self.entrypoint.file

    def validator_path(self) -> Path:
        return self.root / self.validator.file


def _validate_schema(raw: dict[str, Any], yaml_path: Path) -> None:
    """Validate against the JSON schema if jsonschema + the schema file exist.

    Falls back to a minimal required-field check so the harness still works if
    ``jsonschema`` is unavailable.
    """
    required = ["id", "benchmark", "output_type", "evaluation_mode", "entrypoint", "validator"]
    missing = [k for k in required if k not in raw]
    if missing:
        raise ProblemLoadError(
            f"{yaml_path} is missing required field(s): {', '.join(missing)}"
        )

    try:
        import jsonschema  # type: ignore
    except ImportError:  # pragma: no cover - jsonschema is a declared dependency
        return

    if not _SCHEMA_PATH.is_file():  # pragma: no cover - schema ships with the repo
        return

    schema = json.loads(_SCHEMA_PATH.read_text())
    try:
        jsonschema.validate(instance=raw, schema=schema)
    except jsonschema.ValidationError as exc:
        loc = "/".join(str(x) for x in exc.absolute_path) or "<root>"
        raise ProblemLoadError(
            f"{yaml_path} failed schema validation at {loc}: {exc.message}"
        ) from exc
