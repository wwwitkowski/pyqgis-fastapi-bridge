# 🤝 Contributing Guide

Thank you for contributing to the **PyQGIS FastAPI Bridge** project!  
Whether you are working individually, in an engineering team, or collaborating with AI coding assistants, please follow the repository workflow, code quality standards, and commit conventions detailed below.

---

## 🧭 Philosophy: Human-First Development

This repository strictly adheres to the **Human-First** engineering principle:
* **Humans are Architects and Decision Makers.** All decisions regarding system architecture, data structures, technology selection, and domain logic are made by humans.
* **AI is an Execution Tool.** AI assistants (Copilot, Claude, Gemini, ChatGPT, Cursor, etc.) serve as precise executors of instructions — they never make architectural decisions on behalf of humans, never alter project scope, and never introduce dependencies without explicit instruction.

Detailed instructions for AI agents are specified in the [`AGENTS.md`](AGENTS.md) files across each directory.

---

## 🎯 Workflow: Issue-Driven Development

To maintain a transparent division of responsibilities, avoid code conflicts, and prevent bottlenecks from unnecessary bureaucracy:

1. **Every task begins with a GitHub Issue:**
   * Before writing code or prompting an AI agent, create a concise issue in the **Issues** tab.
   * Choose the **🚀 New Task / Feature** template or provide a concise description.
2. **Lightweight Issue Format:**
   Three concise elements are sufficient:
   * **Goal (1-2 sentences):** What is being built and why (e.g., *"Add an endpoint to retrieve parcel geometry in GeoJSON format from ULDK"*).
   * **Module and Assignee:** Target component (`backend`, `qgis_plugin`, `web`, `docs`).
   * **Definition of Done (Checklist):** 2-3 verification criteria (e.g., `- [ ] endpoint returns 200 OK`, `- [ ] unit tests pass`).
3. **Smooth Flow (Issue $\rightarrow$ Branch $\rightarrow$ Commit):**
   * Create a feature branch tied to the task: e.g., `feat/12-uldk-geojson` (where 12 is the issue number).
   * Closing commit: `feat(backend): add uldk geojson endpoint (closes #12)`.
   * This provides full team visibility into ongoing work without duplicated effort.

---

## 🌿 Git Workflow (GitHub Flow)

We use a simple, lightweight **GitHub Flow**:
1. The `master` (or `main`) branch is always stable and ready to run.
2. Every new feature, fix, or documentation update originates from a dedicated branch off `master`.
3. Branch naming convention:
   * `feat/<feature-name>` – new features (e.g., `feat/uldk-polygon-loader`)
   * `fix/<bug-description>` – bug fixes (e.g., `fix/crs-transformation-epsg2180`)
   * `docs/<topic>` – documentation changes (e.g., `docs/update-datasets-guide`)
   * `refactor/<scope>` – code refactoring without behavior modification
4. Upon completion, submit a Pull Request or merge into `master` after human review.

---

## 📝 Commit Conventions (Conventional Commits)

All commits in this repository **must** follow the [Conventional Commits v1.0.0](https://www.conventionalcommits.org/) specification:

```text
<type>(<optional-scope>): <concise description in imperative mood>

[optional body explaining motivation and context]
```

### Allowed types:
* **`feat`** – new feature (e.g., `feat(backend): add endpoint for parcel bounding box`)
* **`fix`** – bug fix (e.g., `fix(qgis): resolve task crash on empty polygon geometry`)
* **`docs`** – documentation only (e.g., `docs: add contributing guide and agent rules`)
* **`refactor`** – code refactoring (e.g., `refactor(shared): simplify geo response schema`)
* **`perf`** – performance improvement (e.g., `perf(backend): cache spatial index lookups`)
* **`test`** – adding or updating unit tests
* **`chore`** – maintenance, tooling, configuration (e.g., `chore: update gitignore`)

### Examples of valid commit messages:
* `feat(ingestion): add retry logic to uldk connector`
* `fix(plugin): prevent GUI freeze by offloading network request to QgsTask`
* `docs(datasets): register new LiDAR WCS endpoint from GUGiK`
* `refactor(backend): decouple router configuration from app instance`

---

## 💻 Code Quality Standards

### 1. Python (Backend & Shared)
* Conformance to **PEP 8** (clear naming, 4-space indentation, clean module boundaries).
* Mandatory **Type Hints** on all function and method signatures.
* Use **Pydantic** models for all API request and response validation.
* **Dependencies are controlled by humans:** AI agents do not autonomously install or add new dependencies. Choosing libraries (e.g., `httpx`, `requests`, `shapely`, `geopandas`) is directed by human developers.

### 2. PyQGIS (QGIS Plugin)
* **Multithreading:** I/O operations (network queries, heavy geometry computations) **must never** execute synchronously on the main GUI thread. The `QgsTask` pattern (`AsyncApiTask`) is mandatory.
* **UI Layouts:** Visual interface adjustments are made in Qt Designer via `dockwidget.ui`. Python code dynamically loads the UI via `PyQt5.uic.loadUiType` — do not precompile to `_ui.py`.
* **Clean Logging:** Direct user messages to the dock log widget or `iface.messageBar()` rather than raw console `print()`.

### 3. Web Frontend (`web/`)
* Lightweight, standards-based code (HTML5, CSS, vanilla JS) integrated with MapLibre GL JS.
* Do not introduce heavy web frameworks (Next.js, Vue, Angular) without explicit human direction.

---

## 🔒 Security & Data Hygiene
1. **Never commit API keys, secrets, or tokens!** Keep sensitive parameters in `.env` files (ignored by `.gitignore`).
2. **Clean State:** Keep the repository clean, avoid checking in temporary artifacts, and maintain universal boilerplate neutrality.
