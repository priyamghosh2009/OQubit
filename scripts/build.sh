#!/usr/bin/env bash
set -e
SCRIPT_DIR="$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")" && pwd)"
PROJECT_ROOT="$(cd -- "$SCRIPT_DIR/.." && pwd)"
cd "$PROJECT_ROOT"
echo "Building wheel file for OQubit Library..."
python setup.py sdist bdist_wheel
echo "Build completed."
echo "Now run scripts/installation.sh to install OQubit Library."