#!/usr/bin/env bash
set -e
echo "=== OQubit Benchmarks ==="
REPO_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$REPO_ROOT"
if ! command -v python >/dev/null 2>&1; then
    echo "Error: Python 3 was not found in PATH."
    exit 1
fi
if ! python -m pytest --version >/dev/null 2>&1; then
    echo "Error: pytest is not installed."
    echo "Install it with: python3 -m pip install pytest"
    exit 1
fi
echo
echo "Running OQubit benchmarks..."
echo
python -m pytest benchmarks/ --benchmark-only -v
echo
echo "OQubit benchmarks completed."