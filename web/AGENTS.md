# Web Viewer Guidelines (`web/`)

Review root `AGENTS.md` and `CONTRIBUTING.md` before making modifications.

---

## Scope and Role
The `web/` directory contains the in-browser map viewer used to:
1. Render GeoJSON vector overlays on OpenStreetMap raster tiles using **MapLibre GL JS**.
2. Query FastAPI backend endpoints directly from a browser.
3. Validate CORS and network connectivity across local machines or Tailscale.

---

## Directory Structure
```text
web/
└── index.html              # Standalone web map (HTML5 + vanilla JS + MapLibre GL JS)
```

---

## Guidelines
1. **Lightweight architecture:** Keep this module framework-free (plain HTML5, CSS, vanilla JavaScript). Do not introduce node build tools or frameworks unless requested.
2. **Map rendering:** Use MapLibre GL JS (open source, no API key required) and standard OpenStreetMap tiles (`https://tile.openstreetmap.org/{z}/{x}/{y}.png`).
3. **API communication:** Use standard browser `fetch()`. Always wrap requests in `try-catch` with clear status feedback and offline fallback representation.
