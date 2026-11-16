# 🤖 Instructions for AI Agents: Shared Module (`shared/`)

> Before editing files in this directory, review the root [`/AGENTS.md`](../AGENTS.md) and [`/CONTRIBUTING.md`](../CONTRIBUTING.md).

---

## 🎯 Scope and Role of the Module
The `shared/` directory is the **Single Source of Truth** for the entire repository. It contains:
1. Shared **Pydantic** data models (`schemas/geo_models.py`) used simultaneously by:
   * FastAPI backend (as request validators and `response_model` schemas),
   * QGIS plugin (as typed return structures for the API client),
   * Web frontend (as canonical JSON contract specifications).
2. Spatial reference system constants and bounding boxes (`constants/poland_crs.py`).

---

## 📂 Directory Structure
```text
shared/
├── constants/
│   ├── poland_crs.py       # EPSG codes (2180, 4326, 3857) and Poland BBOX
│   └── __init__.py
└── schemas/
    ├── geo_models.py       # Models: GeoFeatureRequest, SpatialMetric, GeoAnalysisResponse
    └── __init__.py
```

---

## 🛑 Shared-Specific Rules (`Hard Constraints`)

1. **STRICT PROHIBITION ON UNILATERAL CONTRACT MODIFICATIONS:**
   * Modifying fields in `geo_models.py` instantly impacts the backend, QGIS plugin, and frontend.
   * **You may not add, remove, or rename any field** in Pydantic models without explicit instruction from the human user.
2. **Dependency Cleanliness:**
   * The `shared/` module must remain completely decoupled from the QGIS desktop runtime (`qgis.core`) and the FastAPI framework.
   * It must depend solely on Python standard libraries and `pydantic`.
3. **Backward Compatibility:**
   * All new optional fields in Pydantic models must specify default values (`= None`, `= {}`, `= []`) to avoid deserialization errors in other components.
