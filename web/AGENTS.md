# 🤖 Instructions for AI Agents: Web Module (`web/`)

> Before editing files in this directory, review the root [`/AGENTS.md`](../AGENTS.md) and [`/CONTRIBUTING.md`](../CONTRIBUTING.md).

---

## 🎯 Scope and Role of the Module
The `web/` directory provides a lightweight in-browser map viewer used to:
1. Visualize spatial data (GeoJSON vector layers and raster base maps) using **MapLibre GL JS**.
2. Demonstrate querying FastAPI backend endpoints (`/api/v1/analysis/...`) directly from a web browser.
3. Validate server-side CORS header configuration.

---

## 📂 Directory Structure
```text
web/
└── index.html              # Standalone map viewer (HTML5 + CSS + vanilla JS + MapLibre GL JS)
```

---

## 🛑 Web-Specific Rules (`Hard Constraints`)

1. **No Heavy Frontend Frameworks:**
   * Do not install or configure Next.js, React, Vue, Angular, Vite, or Webpack projects without explicit human direction.
   * This module must remain ultralightweight — openable directly from disk as `index.html` or served as static files.
2. **Map Visualization Standards:**
   * Use the open-source **MapLibre GL JS** library (not Mapbox GL, which requires paid token keys).
   * Use free OpenStreetMap tiles as default basemap (`https://tile.openstreetmap.org/{z}/{x}/{y}.png`).
3. **API Communication:**
   * Execute network requests via the standard browser `fetch()` API.
   * Always handle network errors (`try-catch`), providing users with clear status messages regarding local backend connectivity.
