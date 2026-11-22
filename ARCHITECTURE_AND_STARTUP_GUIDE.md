# Architecture and Startup Guide

PyQGIS FastAPI Bridge connects desktop QGIS, an asynchronous FastAPI spatial backend, and a MapLibre GL JS web viewer.

---

## 1. Quick Startup

- **Windows:** Run `start_all.bat`.
- **Linux / macOS:** Run `./start_all.sh`.

### What the startup script does:
1. Verifies Python and executes the 16 unit tests.
2. Symlinks the QGIS plugin directory into your active QGIS user profile via `link_plugin.bat`.
3. Detects if Docker Desktop is running — if available, spins up PostGIS (port 5432) and the TiTiler raster engine (port 8080).
4. Starts the FastAPI server on `0.0.0.0:8000` and opens the web viewer at `http://127.0.0.1:8000`.

---

## 2. Repository Layout

```text
pyqgis-fastapi-bridge/
├── start_all.bat / .sh          # One-click startup script
├── link_plugin.bat / .sh        # Symlink plugin to QGIS user profile
├── run_tests.bat / .sh          # Run the unit test suite
├── open_designer.bat           # Launch Qt Designer with QGIS custom widgets
├── pyproject.toml               # Python package config (pip install -e .)
├── requirements.txt             # Project dependencies
│
├── backend/                     # Analytical engine and REST API (FastAPI)
│   ├── run_backend.py          # Server entry point (port 8000)
│   ├── app/main.py             # App initialization, CORS, static routes
│   ├── app/api/v1/router.py    # Main API router (/api/v1)
│   ├── app/api/v1/endpoints/   # Endpoints: /analysis, /cadastre
│   └── app/ingestion/          # Public API connectors: GUGiK ULDK, IMGW
│
├── qgis_plugin/                 # Desktop GIS plugin (PyQGIS)
│   └── pyqgis_fastapi_bridge/
│       ├── plugin.py           # Plugin lifecycle, menu, and toolbar actions
│       ├── metadata.txt        # Plugin metadata
│       ├── gui/dockwidget.ui   # Qt Designer dock panel layout
│       ├── gui/dockwidget.py   # Event handling and QgsTask background threads
│       └── core/api_client.py  # HTTP client communicating with FastAPI
│
├── sample_project/              # Sample QGIS project and test datasets
│   ├── sample_project.qgz      # QGIS project configured for EPSG:2180 + OSM
│   └── sample_polygons.geojson # Sample polygons in Moszna area (EPSG:4326)
│
├── web/                         # In-browser map viewer
│   └── index.html              # MapLibre GL JS + OSM client (served by FastAPI)
│
├── shared/                      # Shared models and constants
│   ├── schemas/geo_models.py   # Pydantic models: GeoFeatureRequest, SpatialMetric, GeoAnalysisResponse
│   └── constants/poland_crs.py # CRS constants: EPSG:2180, EPSG:4326, EPSG:3857
│
├── docker/                      # Optional containerized services
│   └── docker-compose.yml      # PostGIS (5432) and TiTiler raster server (8080)
│
├── docs/                        # Public registries and screenshots
│   ├── images/                 # Visual documentation screenshots
│   ├── polish_public_gis_registries.md
│   └── polish_public_gis_registries.csv
│
└── AGENTS.md / CONTRIBUTING.md  # Engineering guidelines and contribution rules
```

---

## 3. Data Flow

```text
1. User selects a feature in QGIS or provides a TERYT / parcel ID
                          │
                          ▼
2. QGIS Plugin dispatches an asynchronous background task (QgsTask)
   [The QGIS desktop interface remains fully responsive]
                          │
                          ▼  (HTTP / JSON request)
3. FastAPI Backend processes the request
   ├── Queries GUGiK ULDK for official parcel geometry (EPSG:2180)
   ├── Queries IMGW for current weather and hydrological telemetry
   └── Computes spatial metrics (area in ha, perimeter in meters)
                          │
                          ▼  (Returns GeoAnalysisResponse matching shared schema)
4. Results display across both clients:
   ├── QGIS Desktop: plugin updates layer geometries and logs metrics
   └── Web Viewer: renders the polygon overlay on OpenStreetMap tiles
```

---

## 4. Coordinate Reference Systems (CRS)

- **Analytical CRS: `EPSG:2180 (PUWG 1992 / ETRF2000-PL)`**  
  Official metric coordinate system used for Polish national cadastre and real-world distance/area measurements ($m^2$, hectares).
- **Exchange CRS: `EPSG:4326 (WGS 84 Lon/Lat)`**  
  Standard format for `.geojson` files and REST API payload coordinates (`[longitude, latitude]`).
- **Web Basemap Tiles: `EPSG:3857 (Web Mercator)`**  
  Standard projection for OpenStreetMap tiles. QGIS transforms it on-the-fly to match EPSG:2180.
