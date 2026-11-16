# 🌉 PyQGIS FastAPI Bridge

> **Asynchronous Developer Boilerplate** bridging the **QGIS (PyQGIS)** desktop workstation, **FastAPI** analytical server, and **MapLibre GL JS** interactive web map.

Designed as a general-purpose geospatial developer toolkit for spatial analytics, urban planning, land administration, transport modeling, hydrology, and environmental management. Features a non-blocking multithreaded communication pipeline, ready-to-use integrations with official public GIS APIs (**GUGiK ULDK, IMGW**), and native coordinate reference system conversions for **EPSG:2180 (PUWG 1992)**.

---

## 🏗️ Architecture and Data Flow

```text
                   ┌──────────────────────────────────────────────┐
                   │             BACKEND (FASTAPI)                │
                   │   Async REST API + ULDK GUGiK + IMGW         │
                   └──────────────────────┬───────────────────────┘
                                          │  REST API (Pydantic / GeoJSON)
                  ┌───────────────────────┴───────────────────────┐
                  ▼                                               ▼
     🖥️ QGIS PLUGIN                                  🌐 WEB VIEWER
     (PyQGIS + background QgsTask)                   (MapLibre GL JS)
     Zero UI freezing during network                 Lightweight in-browser map
     requests and spatial computation                with GeoJSON vector layers
```

---

## ⚡ Key Infrastructure Features

1. **Non-blocking Multithreading in QGIS (`QgsTask`):**
   * API requests and spatial processing run asynchronously in a dedicated worker thread via `QgsTask`.
   * The QGIS user interface **never freezes** – users can pan, zoom, inspect, and select map features uninterrupted while calculations process in the background.

2. **National and Public Registry Integrations (`backend/app/ingestion/`):**
   * **ULDK GUGiK (`uldk_connector.py`):** Real-time cadastre parcel geometry retrieval in EPSG:2180 by TERYT cadastral identifier or clicked XY map coordinates.
   * **IMGW-PIB (`imgw_connector.py`):** Live telemetry and synoptic weather observation data across Poland.
   * **Open Geospatial Registry:** Catalog of 40+ official geospatial data services (WMS, WFS, WCS, STAC API) documented in [`docs/polish_public_gis_registries.md`](docs/polish_public_gis_registries.md).

3. **Coordinate Reference System Transforms (`shared/constants/poland_crs.py`):**
   * Pre-configured definitions and bounding boxes for the metric **EPSG:2180 (Poland CS92)**, global **EPSG:4326 (WGS 84)**, and web standard **EPSG:3857 (Web Mercator)**.

4. **Shared Pydantic Schemas (`shared/schemas/geo_models.py`):**
   * `GeoFeatureRequest`, `SpatialMetric`, and `GeoAnalysisResponse` serve as a single source of truth for API contracts, QGIS plugin data structures, and web clients.

---

## 🚀 Quick Start

### 1. QGIS Plugin
The plugin can be linked directly into your active QGIS user profile:
1. Open the sample project: **[`sample_project/sample_project.qgs`](sample_project/sample_project.qgs)**.
2. Go to **Plugins $\rightarrow$ Manage and Install Plugins...** $\rightarrow$ **Installed** tab and enable:  
   ☑️ **`PyQGIS FastAPI Bridge`**.
3. Click the bridge icon on the toolbar to open the dock widget panel.
4. Click **`▶ Run Analysis (FastAPI)`** – processing tasks dispatch to the QGIS task manager (`QgsTask`), with results streaming into the dock log without UI interruption.

### 2. FastAPI Backend
Start the analytical server with a single command:
```bash
python backend/run_backend.py
```
* **API Base URL:** `http://127.0.0.1:8000`
* **Interactive Swagger UI:** `http://127.0.0.1:8000/docs`
* **Health Check Endpoint:** `http://127.0.0.1:8000/health`

### 3. Automated Testing
Run the comprehensive test suite (16 tests covering API endpoints, Pydantic schemas, CRS constants, ULDK/IMGW connectors, and QGIS plugin structure):
* **Windows (one-click):** Double-click `run_tests.bat`
* **Linux / macOS:** `./run_tests.sh`
* **Direct command:** `python -m unittest discover -s tests -p "test_*.py" -v`
* **GitHub Actions:** Automated CI runs on every push and pull request (`.github/workflows/test.yml`).

### 4. Interactive Web Viewer
Open the viewer in any modern web browser:  
👉 **[`web/index.html`](web/index.html)**

### 5. Tailscale Team Collaboration (Live P2P without GitHub Sync)
Team members on the same **Tailscale** mesh network (tailnet) can interact with services running on each other's workstations directly without needing continuous Git commits or GitHub pulls:
1. **Host Backend:** Start `python backend/run_backend.py` (binds to `0.0.0.0:8000` across all interfaces).
2. **Obtain Node Address:** Retrieve the host machine's Tailscale IP (`100.x.y.z`) or MagicDNS name (e.g., `gis-station`).
3. **Connect from QGIS:** Teammates enter `http://<tailscale-ip>:8000` directly into the **API Server URL** field of the QGIS dock panel.
4. **Connect from Web:** Open [`web/index.html`](web/index.html) and type the Tailscale host URL into the backend input field.
5. **Environment Variable:** Set `PYQGIS_BRIDGE_API_URL=http://<tailscale-ip>:8000/api/v1` (or use `.env.example`) to preconfigure teammate clients.

---

## 🎨 UI Customization in Qt Designer
1. Run **`open_designer.bat`** (or launch Qt Designer with QGIS custom widgets loaded).
2. UI definition file: `qgis_plugin/pyqgis_fastapi_bridge/gui/dockwidget.ui`.
3. Through dynamic UI loading (`PyQt5.uic.loadUiType`), interface adjustments apply immediately upon reloading the plugin in QGIS.

---

## 📜 License & Open Data

### 1. Open Source License
Distributed under the **MIT License** (see [`LICENSE`](LICENSE)). Code may be freely adapted, integrated, and deployed for commercial and research applications.

### 2. Official Open Spatial Data Sources
The boilerplate integrates with legal, public, and open spatial data registries:
* **GUGiK ULDK / PRG / NMT / BDOT10k:** Cadastral parcel locator, national administrative boundaries, digital elevation models (LiDAR), and topographic databases.
* **IMGW-PIB:** Public synoptic observations, precipitation, and hydrological telemetry.
* **Copernicus Data Space Ecosystem (ESA/EU):** Open Sentinel-1, Sentinel-2 multispectral and radar imagery.
* Complete catalog with official WMS/WFS/REST endpoints is listed in [`docs/polish_public_gis_registries.md`](docs/polish_public_gis_registries.md).
