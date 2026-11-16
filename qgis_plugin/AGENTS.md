# 🤖 Instructions for AI Agents: QGIS Plugin Module (`qgis_plugin/`)

> Before editing files in this directory, review the root [`/AGENTS.md`](../AGENTS.md) and [`/CONTRIBUTING.md`](../CONTRIBUTING.md).

---

## 🎯 Scope and Role of the Module
The `qgis_plugin/` directory contains the plugin code for the **QGIS 3** desktop workstation (`PyQGIS`). It is responsible for:
1. Registering actions, menu items, and toolbar buttons in the QGIS interface (`plugin.py`, `metadata.txt`).
2. Displaying the side dock widget (**QDockWidget**) designed in Qt Designer.
3. **Asynchronous communication with the FastAPI backend** in a background worker thread via `QgsTask` (`AsyncApiTask`).
4. Safe interaction with the QGIS map canvas (layer feature reading, coordinate transformation to EPSG:4326/EPSG:2180, result rendering).

---

## 📂 Directory Structure
```text
qgis_plugin/
└── pyqgis_fastapi_bridge/
    ├── __init__.py           # classFactory(iface) - QGIS plugin entry point
    ├── metadata.txt          # QGIS Plugin Manager metadata
    ├── plugin.py             # Action, menu, and dock widget lifecycle management
    ├── icon.png              # Plugin toolbar icon
    ├── gui/
    │   ├── dockwidget.py     # Dock widget logic: QgsTask, event and signal handling
    │   └── dockwidget.ui     # Qt Designer XML layout
    ├── core/
    │   └── api_client.py     # HTTP client querying backend with offline fallback mode
    └── styles/
        └── categorized_style.qml # Sample QGIS layer style templates
```

---

## 🛑 PyQGIS-Specific Rules (`Hard Constraints`)

1. **NEVER BLOCK THE MAIN GUI THREAD:**
   * No network I/O (`urllib.request`, `http`) or heavy geometry computation may run directly inside button click handlers.
   * Always employ the `QgsTask` multithreading pattern (as implemented in `AsyncApiTask`). Perform network queries in `run()` and GUI updates in `finished()`.
2. **Dynamic UI Loading (`loadUiType`):**
   * Edit `dockwidget.ui` using Qt Designer (launchable via `open_designer.bat`).
   * **Never compile `.ui` files to `.py`** using `pyuic5`. The UI is loaded dynamically at runtime via `PyQt5.uic.loadUiType()`.
3. **Relative Paths and Symbolic Linking:**
   * All file references (e.g., `dockwidget.ui`, `icon.png`) must be constructed relatively using `os.path.join(os.path.dirname(__file__), ...)`.
   * The plugin is linked to the active QGIS profile via directory junction / symlink (`deploy.py`). Do not hardcode paths to `%APPDATA%` or drive letters.
4. **Coordinate Reference System (CRS) Standards & Null Island Prevention:**
   * The project standard display and analytical CRS is **`EPSG:2180 (PUWG 1992 / ETRF2000-PL)`** — all Polish cadastre (ULDK), GUGiK, and field metrics are in meters/hectares under this system.
   * GeoJSON standard storage is strictly **`EPSG:4326 (WGS84 Lon/Lat)`**.
   * Web tile backends (e.g., OpenStreetMap) operate in **`EPSG:3857 (Web Mercator)`**.
   * When creating, exporting, or modifying QGIS projects or vector layers:
     * Never leave project CRS unassigned (`None`), as degrees will be interpreted as meters, throwing coordinates into Null Island (Gulf of Guinea / São Tomé).
     * Always enforce `<projectflags><flags><relativePaths>1</relativePaths></flags></projectflags>` in `.qgs`/`.qgz` project files so datasets load seamlessly across teammate machines.
5. **Geometry Validity Checks:**
   * Always verify that layers are valid (`layer.isValid()`) and geometries are non-empty (`not geom.isEmpty()`) before calculating centroids or performing coordinate transforms.
