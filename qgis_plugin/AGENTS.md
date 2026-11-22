# QGIS Plugin Guidelines (`qgis_plugin/`)

Review root `AGENTS.md` and `CONTRIBUTING.md` before making modifications.

---

## Scope and Role
The `qgis_plugin/` directory contains the PyQGIS desktop plugin for QGIS 3 (tested with QGIS 3.44.15 LTR). It handles:
1. Registering toolbar actions and menus in QGIS (`plugin.py`, `metadata.txt`).
2. Managing the dock widget panel layout (`gui/dockwidget.ui`).
3. Asynchronous background communication with FastAPI via `QgsTask` (`AsyncApiTask`).
4. Canvas interaction, layer selection, coordinate transformation, and metric logging.

---

## Directory Structure
```text
qgis_plugin/
└── pyqgis_fastapi_bridge/
    ├── __init__.py           # classFactory(iface) - QGIS plugin entry point
    ├── metadata.txt          # QGIS Plugin Manager metadata
    ├── plugin.py             # Action, menu, and dock widget lifecycle
    ├── icon.png              # Plugin toolbar icon
    ├── gui/
    │   ├── dockwidget.py     # Dock logic, QgsTask dispatch, signal handling
    │   └── dockwidget.ui     # Qt Designer XML layout
    ├── core/
    │   └── api_client.py     # HTTP client querying backend with offline fallback
    └── styles/
        └── categorized_style.qml # Sample QGIS layer style templates
```

---

## Guidelines
1. **Never block the main GUI thread:** Network calls and heavy geometry processing must run inside `QgsTask`. The `AsyncApiTask` implementation performs HTTP requests in `run()` and applies UI updates in `finished()`.
2. **Dynamic UI loading:** Edit `dockwidget.ui` using Qt Designer. Do not precompile `.ui` files to Python code; the plugin loads the layout at runtime using `PyQt5.uic.loadUiType()`.
3. **Relative paths:** Always construct asset paths relatively with `os.path.join(os.path.dirname(__file__), ...)`.
4. **CRS standards:**
   - Analytical & project display CRS: `EPSG:2180 (PUWG 1992)`.
   - Data exchange & GeoJSON storage: `EPSG:4326 (WGS 84 Lon/Lat)`.
   - Web tiles: `EPSG:3857 (Web Mercator)`.
   - Always ensure project CRS is explicitly assigned to prevent degree coordinates being treated as meters.
5. **Geometry checks:** Verify `layer.isValid()` and `not geom.isEmpty()` before calculating centroids or running transformations.
