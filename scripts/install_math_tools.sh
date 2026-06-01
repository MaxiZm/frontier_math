#!/usr/bin/env bash
# Best-effort installer for the heavy external math tools (optional).
# These are NOT required for pytest or the bundled examples; the harness
# degrades gracefully (tool stubs raise ToolUnavailable). Edit per your OS.
set -euo pipefail
echo "This script documents how to install the optional heavy tools."
echo "  SageMath : https://www.sagemath.org/download.html"
echo "  GAP      : https://www.gap-system.org/Download/"
echo "  PARI/GP  : sudo apt-get install pari-gp   (or https://pari.math.u-bordeaux.fr)"
echo "  Z3       : pip install z3-solver"
echo "  Lean     : https://leanprover-community.github.io/get_started.html"
echo "  nauty    : sudo apt-get install nauty"
