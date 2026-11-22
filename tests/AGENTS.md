# Testing Guidelines (`tests/`)

Review root `AGENTS.md` and `CONTRIBUTING.md` before making modifications.

---

## Testing Principles

1. **Focused coverage:** Test domain boundaries, coordinate conversions, schema contracts, and error handling. Avoid superficial tests written purely to inflate coverage.
2. **No live network requests:** Unit tests must never query live external endpoints (GUGiK, IMGW, etc.). Use mocks (`unittest.mock`), stubs, or offline fixture validation.
3. **Deterministic execution:** No timing-dependent assertions (`time.sleep`), unseeded random values, or timezone-sensitive logic.
4. **Standard library runner:** Use standard Python `unittest`. Tests must run out-of-the-box without requiring specialized test runners.

---

## Test Suite Structure

```text
tests/
├── test_api.py                 # FastAPI endpoints (/health, /api/v1/analysis)
├── test_crs_and_geometry.py    # EPSG:2180 / EPSG:4326 transforms and bounds
├── test_ingestion_offline.py   # ULDK and IMGW connectors (offline / mocked)
├── test_qgis_plugin.py         # Plugin metadata, layout, and client fallback
└── test_schemas.py             # Pydantic schemas and serialization
```

---

## Running Tests

```bash
# Windows
run_tests.bat

# Linux / macOS
./run_tests.sh

# Python CLI
python -m unittest discover -s tests -p "test_*.py" -v
```
