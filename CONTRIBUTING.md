# Contributing to PyQGIS FastAPI Bridge

Thank you for contributing to PyQGIS FastAPI Bridge. Whether you are working individually, in an engineering team, or using AI coding assistants, please follow the repository workflow, code quality standards, and commit conventions described below.

---

## Development Philosophy: Human-First

This repository follows a human-first engineering principle:
- **Humans make architectural decisions:** System architecture, data contracts, dependencies, and business logic are decided by developers.
- **AI assistants execute bounded tasks:** Tools such as Copilot, Claude, Gemini, ChatGPT, or Cursor serve as precise executors of specific instructions. They do not alter system scope, introduce unapproved dependencies, or redesign components independently.

Directory-level guidelines for AI assistants are documented in `AGENTS.md`.

---

## Issue-Driven Development

To keep work clear and avoid duplicated effort:

1. **Start with a GitHub issue:**
   Before writing code or prompting an assistant, open a short issue outlining what is being built and why.
2. **Keep issues simple:**
   - **Goal:** 1-2 sentences (e.g. *"Add an endpoint to retrieve parcel geometry in GeoJSON format from ULDK"*).
   - **Scope:** Target module (`backend`, `qgis_plugin`, `web`, `docs`, `shared`).
   - **Definition of Done:** 2-3 checklist items (e.g. `- [ ] endpoint returns 200 OK`, `- [ ] unit tests pass`).
3. **Link branches to issues:**
   - Feature branches: `feat/12-uldk-geojson` (where 12 is the issue number).
   - Commits: `feat(backend): add uldk geojson endpoint (closes #12)`.

---

## Git Workflow

We use standard GitHub Flow:
1. `master` is always stable and passes all tests.
2. Create a feature branch from `master` for any change.
3. Branch naming:
   - `feat/<name>` — new features
   - `fix/<name>` — bug fixes
   - `docs/<name>` — documentation
   - `refactor/<name>` — code refactoring without functional changes
4. Open a Pull Request into `master` for review.

---

## Commit Conventions

All commits follow [Conventional Commits v1.0.0](https://www.conventionalcommits.org/):

```text
<type>(<scope>): <short imperative description>

[optional body]
```

### Allowed types:
- `feat` — new feature
- `fix` — bug fix
- `docs` — documentation updates
- `refactor` — code refactoring
- `perf` — performance improvements
- `test` — adding or fixing tests
- `chore` — tooling, maintenance, configuration

### Examples:
- `feat(ingestion): add retry logic to uldk connector`
- `fix(plugin): prevent GUI freeze by offloading request to QgsTask`
- `docs(registries): add LiDAR WCS endpoint from GUGiK`
- `refactor(backend): decouple router configuration from app instance`

---

## Code Quality Standards

### Python (Backend & Shared)
- Follow **PEP 8** standards (4 spaces, descriptive naming, clean module boundaries).
- Include **type hints** on all function signatures.
- Use **Pydantic** models for request/response serialization and validation.
- Do not add new third-party dependencies without explicit approval.

### PyQGIS (QGIS Plugin)
- **Background tasks (`QgsTask`):** Network calls and geometry computations must run off the main GUI thread. The `AsyncApiTask` pattern is required.
- **UI layout:** Edit `qgis_plugin/pyqgis_fastapi_bridge/gui/dockwidget.ui` directly in Qt Designer. Python loads the `.ui` dynamically via `PyQt5.uic.loadUiType` — do not precompile to `_ui.py`.
- **Logging:** Output to the dock log widget or `iface.messageBar()` instead of `print()`.

### Web Frontend (`web/`)
- Pure HTML5, CSS, and vanilla JavaScript integrating MapLibre GL JS.
- Avoid introducing front-end build tools or frameworks unless requested.

---

## Security & Data Hygiene
- **Never commit secrets or API tokens.** Use `.env` files (ignored by `.gitignore`).
- Keep the repository clean and avoid committing temporary data files or test artifacts.
