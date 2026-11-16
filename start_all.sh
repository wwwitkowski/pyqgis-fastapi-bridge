#!/usr/bin/env bash
set -e

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
echo "========================================================"
echo "  PyQGIS FastAPI Bridge - All-in-One Launcher (Linux/macOS)"
echo "========================================================"

# 1. Detect Python
if command -v python3 &>/dev/null; then
    PYTHON_CMD="python3"
elif command -v python &>/dev/null; then
    PYTHON_CMD="python"
else
    echo "[ERROR] Python 3 was not found."
    exit 1
fi

echo "[1/4] Running automated tests..."
$PYTHON_CMD -m unittest discover -s tests -p "test_*.py" || true

echo "[2/4] Linking QGIS plugin..."
bash "$SCRIPT_DIR/link_plugin.sh" || true

echo "[3/4] Checking Docker stack..."
if docker info &>/dev/null; then
    docker compose -f "$SCRIPT_DIR/docker/docker-compose.yml" up -d
    echo "[OK] Docker containers active."
else
    echo "[INFO] Docker daemon not running. Skipping container startup."
fi

echo "[4/4] Starting FastAPI backend on http://127.0.0.1:8000..."
$PYTHON_CMD "$SCRIPT_DIR/backend/run_backend.py" &
BACKEND_PID=$!

sleep 2

# Open browser
if command -v xdg-open &>/dev/null; then
    xdg-open "http://127.0.0.1:8000"
elif command -v open &>/dev/null; then
    open "http://127.0.0.1:8000"
fi

echo "Backend running with PID: $BACKEND_PID"
echo "Press Ctrl+C to terminate."
wait $BACKEND_PID
