#!/usr/bin/env bash
# Set up the local Python environment for the math-discovery-harness.
set -euo pipefail
cd "$(dirname "$0")/.."
if command -v uv >/dev/null 2>&1; then
  uv sync
else
  python -m venv .venv
  . .venv/bin/activate
  pip install -e ".[dev]"
fi
echo "Environment ready. Run: pytest -q"
