# 🤖 Instructions for AI Agents: Backend Module (`backend/`)

> Before editing files in this directory, review the root [`/AGENTS.md`](../AGENTS.md) and [`/CONTRIBUTING.md`](../CONTRIBUTING.md).

---

## 🎯 Scope and Role of the Module
The `backend/` directory is the computational and communication core of the system (FastAPI). It is responsible for:
1. Exposing asynchronous REST API endpoints under the `/api/v1` prefix.
2. Ingesting raw spatial and environmental data via connector modules (`app/ingestion/`).
3. Performing geometric calculations and on-demand spatial metrics (`app/domain/`).
4. Providing interactive Swagger UI documentation at `/docs`.

---

## 📂 Directory Structure
```text
backend/
├── app/
│   ├── main.py                 # FastAPI initialization, CORS middleware, routers
│   ├── core/
│   │   └── config.py           # Environment variables, public API constants
│   ├── ingestion/              # DATA CONNECTORS (GUGiK ULDK, IMGW, etc.)
│   │   ├── uldk_connector.py   # GUGiK ULDK API client
│   │   └── imgw_connector.py   # IMGW-PIB data client
│   ├── domain/                 # ANALYTICAL & COMPUTATIONAL FUNCTIONS
│   │   └── geometry_metrics.py # Bounding box, area, spatial metric computations
│   └── api/v1/
│       ├── router.py           # Router registration under /api/v1
│       └── endpoints/          # Endpoint handlers (cadastre.py, analysis.py)
├── requirements.txt            # Minimal dependencies (FastAPI, uvicorn, pydantic)
└── run_backend.py              # Quick start script for local development
```

---

## 🛑 Backend-Specific Rules (`Hard Constraints`)

1. **Dependencies Controlled by Humans:**
   * Do not install additional libraries (`requests`, `httpx`, `aiohttp`, `geopandas`, `shapely`) without explicit direction from the user in that task.
   * Work with dependencies declared in `requirements.txt` or explain the requirement to the human user first.
2. **Strict Consistency with Pydantic Models:**
   * All endpoints in `api/v1/endpoints/` **must** utilize models from `shared/schemas/geo_models.py` as `response_model`.
   * Do not create duplicated local Pydantic models in the backend — schemas are shared with the QGIS plugin and web frontend.
3. **Robust Error Handling:**
   * External service queries (ULDK, IMGW) must be enclosed in `try-except` blocks with sensible timeouts (`timeout=5`) and descriptive HTTP statuses (`HTTPException`).
4. **Code Cleanliness:**
   * Maintain async function definitions (`async def`) for FastAPI endpoint handlers.
   * Do not introduce arbitrary domain heuristics into `app/domain/` that were not requested.
