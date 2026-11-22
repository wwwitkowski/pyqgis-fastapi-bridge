# AI Assistant Instructions (AGENTS.md)

Guidelines for AI coding assistants (Copilot, Claude, Gemini, Cursor, ChatGPT, etc.) working on this codebase.

---

## Engineering Rules: Human-First Development

This repository adheres strictly to human-first development:
- **Developers define architecture and goals:** Technology choices, data structures, external dependencies, and business logic are determined by human developers.
- **AI operates within specified scope:** Execute requested tasks precisely without unauthorized refactoring or scope creep.

### Constraints:
1. **No unauthorized dependencies:**
   Do not install or add packages to `requirements.txt`, `pyproject.toml`, or the environment (`pip install ...`) without prior approval.
2. **Adhere to task scope:**
   Keep modifications strictly bounded to the requested issue or feature. Do not make speculative or unrelated changes.
3. **Preserve data contracts:**
   Do not modify schemas in `shared/schemas/` without explicit instruction, as they are shared across backend, QGIS plugin, and frontend.
4. **Minimal diffs:**
   Change only the lines necessary to complete the task. Never remove existing tests, comments, or documentation as a side effect.
5. **No hallucinated imports:**
   Verify that modules physically exist before importing them.
6. **Ask for clarification:**
   When an instruction is ambiguous or contradictory, ask the user before proceeding.

---

## Spatial Standards & CRS Rules

1. **Analytical CRS: `EPSG:2180 (PUWG 1992 / ETRF2000-PL)`**
   - Official Polish national metric coordinate system.
   - All spatial calculations (area in hectares/$m^2$, perimeter in meters) and Polish cadastre queries (GUGiK ULDK) must use EPSG:2180.
2. **Exchange CRS: `EPSG:4326 (WGS 84 Lon/Lat)`**
   - GeoJSON exports and REST API payload coordinates use `[longitude, latitude]`.
3. **Null Island Prevention:**
   - Always ensure QGIS project files have an explicitly defined `projectCrs` (EPSG:2180). An unassigned CRS can cause degree coordinates to be misinterpreted as meters.
   - Use relative project paths (`<relativePaths>1</relativePaths>`) in `.qgs`/`.qgz` files so they open reliably across different workstations.

---

## Submodule Documentation

| Module | Path | Description |
| :--- | :--- | :--- |
| **Shared** | `shared/` | Pydantic data schemas and CRS constants |
| **Backend** | `backend/` | FastAPI application, routes, and ingestion connectors |
| **QGIS Plugin** | `qgis_plugin/` | PyQGIS dock widget plugin with `QgsTask` workers |
| **Web** | `web/` | MapLibre GL JS web client |
| **Docs** | `docs/` | Public spatial data registry catalog |
| **Docker** | `docker/` | Docker Compose configuration (PostGIS, TiTiler) |
| **Tests** | `tests/` | Automated unit test suite |
