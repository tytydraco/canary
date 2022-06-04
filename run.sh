#!/usr/bin/env bash

SCRIPT_DIR="$(cd -- "$(dirname -- "${BASH_SOURCE[0]:-$0}")" &> /dev/null && pwd 2> /dev/null)"
PY_ENTRY="src/main.py"
PYTHON="python3"
PYTHONPATH="$SCRIPT_DIR" "$PYTHON" "$SCRIPT_DIR/$PY_ENTRY"