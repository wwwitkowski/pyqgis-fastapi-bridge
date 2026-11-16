# 🤖 Instructions for AI Agents: Testing Module (`tests/`)

> **FOR EVERY AI AGENT AND CODING ASSISTANT:**  
> Read this document before authoring, modifying, or proposing tests in this repository.

---

## 🛑 TESTING PRINCIPLES (HUMAN-FIRST TESTING)

This project strictly adheres to **Human-First Testing**. Humans determine test architecture, verification goals, and acceptance criteria. AI agents are executors and have no authority to arbitrarily expand test suites.

### 🚫 STRICT PROHIBITIONS (Zero Tolerance):
1. **NO TRIVIAL OR SUPERFLUOUS TESTS (Zero Test Bloat):**
   * Do not write tests verifying Python language semantics (e.g. testing whether `1 + 1 == 2`, whether `list.append()` appends, or whether dictionary keys persist).
   * Do not test plain getters/setters, empty constructors, or trivial assignments lacking validation logic.
   * Do not generate vanity tests solely to artificially increase code coverage.
2. **NO UNAUTHORIZED TEST SUITES OR FILES:**
   * AI agents **must not create new test files** without explicit human direction defining the scope and purpose.
   * If you spot an unhandled edge case, ask the human user: *"Would you like me to add a test verifying scenario X?"*.
3. **NO DIRECT EXTERNAL NETWORK CALLS (Zero Live Network in Tests):**
   * No unit test may dispatch real HTTP requests to external servers (ULDK, IMGW, Open-Meteo, etc.).
   * All external integrations must use mocks (`unittest.mock`), stubs, or offline fallback validation (`test_ingestion_offline.py`).
4. **NO FLAKY OR UNSTABLE TESTS:**
   * No `time.sleep()`, unseeded pseudorandom values, or assumptions dependent on local timezone or location.

---

## 🎯 WHAT AI AGENTS SHOULD TEST (When Instructed):

1. **Data Contracts & Pydantic Schemas (`test_schemas.py`):**
   * Ensure malformed coordinates and invalid types trigger appropriate validation exceptions (`ValidationError`).
   * Verify GeoJSON serialization and deserialization conform to RFC 7946 specifications.
2. **Coordinate Transformations & Metric Calculations (`test_crs_and_geometry.py`):**
   * Validate that conversions between EPSG:2180 and EPSG:4326/EPSG:3857 remain within precision tolerances.
   * Verify polygon area calculations in $m^2$ and hectares handle boundaries correctly and reject degenerated geometries.
3. **Error Handling & Graceful Degradation (Fallback):**
   * Verify behavior under empty API payloads, HTTP 500 errors, timeouts, and malformed JSON or WKT.
4. **QGIS Plugin Structure & Environment Isolation (`test_qgis_plugin.py`):**
   * Verify `metadata.txt` validity, import cleanliness, and absence of GUI exceptions in headless test environments.

---

## 🛠️ TECHNICAL TESTING STANDARDS

* **Framework:** Standard Python standard library `unittest`.
* **Zero new dependencies:** Tests must run in a vanilla Python environment without requiring mandatory third-party test runners (e.g. `pytest`, unless requested).
* **Path Isolation:** Every test file dynamically resolves repository root via `sys.path.insert(0, ...)`.
* **Conditional Skipping:** For optional dependencies (such as `fastapi` or `pydantic`), tests must use `@unittest.skipIf(not MODULE_AVAILABLE, "Reason for skip")` to ensure test execution passes in any environment.
