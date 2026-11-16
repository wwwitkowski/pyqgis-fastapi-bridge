#!/usr/bin/env bash
set -e

PLUGIN_NAME="pyqgis_fastapi_bridge"
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
SOURCE_DIR="${SCRIPT_DIR}/qgis_plugin/${PLUGIN_NAME}"

if [[ "$OSTYPE" == "darwin"* ]]; then
    TARGET_DIR="${HOME}/Library/Application Support/QGIS/QGIS3/profiles/default/python/plugins/${PLUGIN_NAME}"
else
    TARGET_DIR="${HOME}/.local/share/QGIS/QGIS3/profiles/default/python/plugins/${PLUGIN_NAME}"
fi

echo "=========================================================="
echo " Linking QGIS Plugin (${OSTYPE})"
echo " Source: ${SOURCE_DIR}"
echo " Target: ${TARGET_DIR}"
echo "=========================================================="

mkdir -p "$(dirname "${TARGET_DIR}")"

if [ -L "${TARGET_DIR}" ] || [ -e "${TARGET_DIR}" ]; then
    rm -rf "${TARGET_DIR}"
fi

ln -s "${SOURCE_DIR}" "${TARGET_DIR}"

echo ""
echo "[SUCCESS] PyQGIS FastAPI Bridge plugin linked successfully!"
echo "Enable the plugin in QGIS: Plugins -> Manage and Install Plugins."
