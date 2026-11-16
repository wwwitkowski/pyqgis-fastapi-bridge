# 🧭 Architecture and Getting Started Guide: What, Where & How?

> **PyQGIS FastAPI Bridge** — an asynchronous developer starter bridging the **Python / FastAPI** spatial engine, the **QGIS** desktop GIS workstation, and an interactive **Web (MapLibre GL JS)** viewer.

---

## ⚡ 1. How to Launch Everything in 1 Click?

* **Windows:** Double-click **`start_all.bat`**.
* **Linux / macOS:** Execute `./start_all.sh` in the terminal.

### What does the `start_all` script do?
1. Detects Python and runs all 16 automated unit tests.
2. Automatically symlinks/junctions the QGIS plugin directly into your active QGIS user profile (`link_plugin.bat`).
3. Checks if Docker Desktop is running — if active, starts the PostGIS spatial database (port 5432) and the TiTiler raster tile engine (port 8080).
4. Launches the FastAPI backend server on `0.0.0.0:8000` and automatically opens the interactive map viewer in your default web browser at **`http://127.0.0.1:8000`**.

---

## 🗺️ 2. Repository Structure: What is Where?

```text
pyqgis-fastapi-bridge/
│
├── 🚀 start_all.bat / .sh          # One-click startup script for the entire environment
├── 🔗 link_plugin.bat / .sh        # Links the plugin directory directly to QGIS python plugins
├── 🧪 run_tests.bat / .sh          # Runs the complete 16-test unit test suite
├── 🎨 open_designer.bat           # Launches Qt Designer loaded with native QGIS widgets
├── 📦 pyproject.toml               # Python package configuration (pip install -e .)
├── 📋 requirements.txt             # Project Python dependencies
│
├── 🧠 backend/                     # ANALYTICAL ENGINE & REST API (FastAPI)
│   ├── run_backend.py              # Server entry point (port 8000)
│   ├── app/main.py                 # FastAPI app, CORS, routing, and embedded web UI static serving
│   ├── app/api/v1/router.py        # Central API routing hub (/api/v1)
│   ├── app/api/v1/endpoints/       # API routes: /analysis, /cadastre (ULDK)
│   └── app/ingestion/              # Public API connectors: GUGiK ULDK (cadastre), IMGW (weather)
│
├── 🖥️ qgis_plugin/                 # DESKTOP GIS WORKSTATION (PyQGIS)
│   └── pyqgis_fastapi_bridge/
│       ├── plugin.py               # Plugin lifecycle, QGIS menu, and toolbar actions
│       ├── metadata.txt            # Plugin metadata for QGIS 3.44.15 LTR
│       ├── gui/dockwidget.ui       # Qt Designer XML dock panel layout
│       ├── gui/dockwidget.py       # Event handling and non-blocking QgsTask multithreading
│       └── core/api_client.py      # HTTP client communicating with FastAPI (with offline fallback)
│
├── 📐 sample_project/              # READY-TO-USE QGIS TEST PROJECT
│   ├── sample_project.qgz / .qgs   # Native QGIS project configured with EPSG:2180 and OSM basemap
│   └── sample_polygons.geojson     # Sample test polygons in Moszna village area (WGS 84 / EPSG:4326)
│
├── 🌐 web/                         # INTERACTIVE IN-BROWSER MAP VIEWER
│   └── index.html                  # MapLibre GL JS + OpenStreetMap client (served directly via FastAPI)
│
├── 🔄 shared/                      # SHARED DATA CONTRACTS (Single Source of Truth)
│   ├── schemas/geo_models.py       # Pydantic models: GeoFeatureRequest, SpatialMetric, GeoAnalysisResponse
│   └── constants/poland_crs.py     # CRS constants and bounding boxes: EPSG:2180, EPSG:4326, EPSG:3857
│
├── 🐳 docker/                      # CONTAINERIZED SERVICES (Optional)
│   └── docker-compose.yml          # PostGIS (5432) and dynamic COG raster tile server TiTiler (8080)
│
├── 📚 docs/                        # GEOSPATIAL REGISTRY & KNOWLEDGE BASE
│   ├── polish_public_gis_registries.md   # Catalog of 40+ Polish and European public GIS services
│   └── polish_public_gis_registries.csv  # Machine-readable registry endpoint catalog
│
└── 🤖 AGENTS.md / CONTRIBUTING.md  # Human-First AI manifest, Issue-Driven development, and code standards
```

---

## 🔄 3. System Data Flow

```text
1. User clicks a parcel in QGIS or inputs a feature / TERYT ID
                          │
                          ▼
2. QGIS Plugin (PyQGIS) dispatches a background task (QgsTask)
   [The QGIS desktop interface stays completely responsive and smooth!]
                          │
                          ▼  (HTTP / JSON request over local network or Tailscale mesh)
3. FastAPI Backend receives the request
   ├── Queries GUGiK ULDK (fetches official cadastral parcel geometry in EPSG:2180)
   ├── Queries IMGW telemetry (fetches latest temperature, precipitation, wind speed)
   └── Computes surface area (ha/m²), perimeter, and risk/suitability metrics
                          │
                          ▼  (Returns GeoAnalysisResponse matching shared Pydantic contract)
4. Results stream simultaneously to TWO SCREENS:
   ├── QGIS Desktop: plugin visualizes geometry, updates styles, and logs calculated metrics
   └── Web Viewer: http://127.0.0.1:8000 renders the polygon on top of OpenStreetMap
```

---

## 🌍 4. Spatial Coordinate Reference System (CRS) Standards

* **Analytical and Project Display CRS: `EPSG:2180 (PUWG 1992 / ETRF2000-PL)`**  
  The official Polish national projected metric coordinate system. Used for real-world distance, perimeter, and surface area calculations ($m^2$, hectares), as well as national cadastre services.
* **Data Exchange CRS: `EPSG:4326 (WGS 84 Lon/Lat)`**  
  Standard format for `.geojson` files and REST API payload coordinates (`[longitude, latitude]`).
* **Web Basemap Tiles: `EPSG:3857 (Web Mercator)`**  
  Standard projection for OpenStreetMap tiles. QGIS transforms it on-the-fly to EPSG:2180.

---

## 👥 5. Team Collaboration over Tailscale (Peer-to-Peer)

Team members do not need to deploy the backend to public cloud servers during development:
1. Install **Tailscale** on team laptops.
2. The team member hosting the backend executes `start_all.bat`.
3. Other teammates enter the host's Tailscale IP address (e.g., `http://100.85.12.34:8000`) into their QGIS plugin dock panel or browser.
4. The entire team collaborates in real time against the shared analytical engine!
