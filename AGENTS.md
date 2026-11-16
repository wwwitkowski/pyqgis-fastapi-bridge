# 🤖 Instructions for AI Agents (AGENTS.md) — Human-First Development

> **FOR EVERY AI AGENT AND CODING ASSISTANT (Copilot, Claude, Gemini, Cursor, ChatGPT, etc.):**  
> Read this entire document before attempting any modifications to the codebase in this repository.

---

## 🛑 MANIFESTO: HUMAN-FIRST DEVELOPMENT

This project operates under the absolute primacy of human decision-making. You are an **execution tool**, not the system architect. Humans define goals, technical requirements, and architecture. Your role is precise execution within the assigned scope without unauthorized deviation.

### 🚫 HARD CONSTRAINTS (Zero Tolerance):
1. **NO UNAUTHORIZED DEPENDENCIES OR LIBRARIES:**
   * You may not install or append new libraries to `requirements.txt`, `package.json`, or the environment (`pip install ...`, `npm install ...`) without explicit prior human approval.
   * Work with existing libraries and tools already configured in the project.
2. **NO WORK OUTSIDE DEFINED SCOPE (Issue-Driven AI Execution):**
   * Do not make speculative or unsolicited additions. Your work must correspond strictly to a specific issue or goal defined by the human user.
   * If provided an Issue or task description, adhere strictly to the acceptance criteria (Definition of Done) in that task.
3. **NO AUTONOMOUS ARCHITECTURAL OR DOMAIN DECISIONS:**
   * Do not restructure directories, redesign data models, change database technologies, or modify data contracts in `shared/schemas/`.
   * Do not invent domain heuristics, business rules, or arbitrary assumptions not requested by the human user.
4. **NO DESTRUCTIVE REWRITES OR ACCIDENTAL DELETIONS:**
   * Maintain a **minimal diff** — edit only lines necessary to accomplish the requested task.
   * Never remove existing functions, comments, tests, or documentation as a side effect.
5. **NO HALLUCINATED IMPORTS OR PATHS:**
   * Only import modules that physically exist in the project or Python standard library. Verify paths on disk before referencing them.
6. **DUTY TO CLARIFY UNCERTAINTIES:**
   * If an instruction is ambiguous, incomplete, or contradictory, **stop and ask the user for clarification** rather than guessing.

---

## 🌍 Spatial Standards & CRS Rules (Null Island Prevention)

1. **Standard Project & Analytical CRS: `EPSG:2180 (PUWG 1992 / ETRF2000-PL)`**
   * Official Polish national projected metric coordinate system.
   * All Polish public registries (GUGiK ULDK, Geoportal, cadastral parcels) operate under EPSG:2180.
   * All distance, perimeter, and surface area calculations ($m^2$, hectares) must be performed in EPSG:2180.
2. **Standard Exchange & GeoJSON CRS: `EPSG:4326 (WGS 84 Lon/Lat)`**
   * Standard GeoJSON files and Pydantic API response coordinates are formatted as `[longitude, latitude]`.
3. **Null Island (São Tomé / Gulf of Guinea) Prevention:**
   * Never create or export QGIS project files with an empty/unassigned project CRS (`projectCrs`). Without an explicit CRS, degrees (`20.75°E, 52.18°N`) are interpreted as metric meters (`20m, 52m`), landing features off the coast of West Africa (Null Island).
   * Always enforce relative project paths (`<projectflags><flags><relativePaths>1</relativePaths></flags></projectflags>`) in `.qgs`/`.qgz` files so projects resolve data files relative to the project directory across different developer workstations.

---

## 🗺️ Module Map & Subordinate AGENTS.md Files

This repository follows a modular layout. Each submodule maintains its own specialized `AGENTS.md` specifying rules for that component:

| Module | Path | Role in System | Dedicated Guidelines |
| :--- | :--- | :--- | :--- |
| **Shared** | [`shared/`](shared/AGENTS.md) | Single Source of Truth: Pydantic schemas, CRS constants | [shared/AGENTS.md](shared/AGENTS.md) |
| **Backend** | [`backend/`](backend/AGENTS.md) | FastAPI server, `/api/v1` routing, open API connectors (ULDK, IMGW) | [backend/AGENTS.md](backend/AGENTS.md) |
| **QGIS Plugin** | [`qgis_plugin/`](qgis_plugin/AGENTS.md) | PyQGIS dock widget plugin with `QgsTask` multithreading | [qgis_plugin/AGENTS.md](qgis_plugin/AGENTS.md) |
| **Web** | [`web/`](web/AGENTS.md) | Lightweight MapLibre GL JS in-browser map viewer | [web/AGENTS.md](web/AGENTS.md) |
| **Docs** | [`docs/`](docs/AGENTS.md) | Public spatial data registries and technical specifications | [docs/AGENTS.md](docs/AGENTS.md) |
| **Docker** | [`docker/`](docker/AGENTS.md) | Optional service containerization (PostGIS, MinIO, TiTiler) | [docker/AGENTS.md](docker/AGENTS.md) |
| **Tests** | [`tests/`](tests/AGENTS.md) | Automated unit tests and Human-First testing rules | [tests/AGENTS.md](tests/AGENTS.md) |

---

## 📋 Code Quality Standards for AI Agents

Before reporting task completion:
1. **Ensure code runs cleanly without syntax errors (`SyntaxError`) or import failures (`ImportError`).**
2. **Follow naming conventions and Conventional Commits described in [`CONTRIBUTING.md`](CONTRIBUTING.md).**
3. **Include type hints and clear English docstrings on all functions and classes.**
4. **All file paths must be relative or constructed using `os.path.join()` / `pathlib.Path` to preserve operating system portability (Windows, macOS, Linux). Never hardcode local absolute paths (such as `C:\` or home directories).**

---

## 🧪 Testing Standards (Human-First Testing)

This project follows **Human-First Testing** — test suites protect actual system contracts rather than padding artificial code metrics:
1. **Humans decide what to test:** AI agents must not autonomously add new test files or bloated test suites without human review.
2. **Zero Test Bloat:** Do not write tests verifying language primitives, basic attribute assignments, or empty constructors.
3. **Focus on real risks:** Unit tests cover data schemas (`Pydantic`), API degradation resilience (mock/offline mode), coordinate transformations (`EPSG:2180`), and QGIS plugin metadata integrity.
4. **Further details:** Refer to [`tests/AGENTS.md`](tests/AGENTS.md).
