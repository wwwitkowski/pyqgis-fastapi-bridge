# Backend Guidelines (`backend/`)

Review root `AGENTS.md` and `CONTRIBUTING.md` before making modifications.

---

## Scope and Role
The `backend/` directory contains the FastAPI spatial analytics engine and REST API. It handles:
1. Asynchronous REST API endpoints under `/api/v1`.
2. Public data ingestion via connectors in `app/ingestion/` (GUGiK ULDK, IMGW-PIB).
3. Geometric calculations and spatial metric computations in `app/domain/`.
4. Serving interactive Swagger UI docs at `/docs` and the static web map at `/`.

---

## Directory Structure
```text
backend/
├── app/
│   ├── main.py                 # FastAPI initialization, CORS, static routes
│   ├── core/
│   │   └── config.py           # Configuration and environment variables
│   ├── ingestion/              # Data connectors (GUGiK ULDK, IMGW)
│   │   ├── uldk_connector.py   # GUGiK ULDK API client
│   │   └── imgw_connector.py   # IMGW-PIB telemetry client
│   ├── domain/                 # Analytical & geometry functions
│   │   └── geometry_metrics.py # Bounding box, area, perimeter calculations
│   └── api/v1/
│       ├── router.py           # Router registration under /api/v1
│       └── endpoints/          # Endpoints (cadastre.py, analysis.py)
├── requirements.txt            # Python dependencies
└── run_backend.py              # Server launcher
```

---

## Guidelines
1. **Dependencies:** Do not add third-party packages without explicit user request. Work with dependencies in `requirements.txt`.
2. **Schema consistency:** All endpoints must use schemas from `shared/schemas/geo_models.py` as their `response_model`. Do not duplicate schemas locally.
3. **Error handling:** External queries to GUGiK and IMGW must include appropriate timeouts (`timeout=5`) and HTTP exception handling.
4. **Async endpoints:** Use `async def` for FastAPI handlers.
