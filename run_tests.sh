#!/usr/bin/env bash
set -e

echo "=========================================================="
echo " Running Unit Test Suite (PyQGIS Bridge)"
echo "=========================================================="

python3 -m unittest discover -s tests -p "test_*.py" -v

echo ""
echo "[SUCCESS] All tests passed successfully!"
