# Shared Module Guidelines (`shared/`)

Review root `AGENTS.md` and `CONTRIBUTING.md` before making modifications.

---

## Scope and Role
The `shared/` directory serves as the single source of truth for contracts across the stack:
1. Pydantic schemas (`schemas/geo_models.py`) used by FastAPI endpoints, the QGIS plugin client, and web JSON responses.
2. Coordinate reference system constants and extents (`constants/poland_crs.py`).

---

## Directory Structure
```text
shared/
├── constants/
│   ├── poland_crs.py       # EPSG:2180, EPSG:4326, EPSG:3857 and bounding boxes
│   └── __init__.py
└── schemas/
    ├── geo_models.py       # GeoFeatureRequest, SpatialMetric, GeoAnalysisResponse
    └── __init__.py
```

---

## Guidelines
1. **Contract stability:** Models in `geo_models.py` define the communication contract between backend, desktop plugin, and web clients. Do not modify or remove fields without explicit agreement.
2. **Framework independence:** `shared/` must remain decoupled from both `qgis.core` and FastAPI. It relies solely on `pydantic` and the standard library.
3. **Backward compatibility:** Any new optional fields must include defaults (`None`, `[]`, or `{}`) to prevent serialization mismatches across clients.
