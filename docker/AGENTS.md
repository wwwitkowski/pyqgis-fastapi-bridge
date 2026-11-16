# 🤖 Instructions for AI Agents: Container Module (`docker/`)

> Before editing files in this directory, review the root [`/AGENTS.md`](../AGENTS.md) and [`/CONTRIBUTING.md`](../CONTRIBUTING.md).

---

## 🎯 Scope and Role of the Module
The `docker/` directory contains optional container definitions for developers deploying spatial databases and auxiliary services via `docker compose`. It includes:
1. **PostGIS** spatial database (`postgis/postgis:15-3.3`).
2. **MinIO** local S3-compatible object storage for Cloud Optimized GeoTIFF (COG) rasters.
3. **TiTiler** dynamic tile server (`ghcr.io/developmentseed/titiler`).

---

## 📂 Directory Structure
```text
docker/
└── docker-compose.yml       # Service definitions: postgis (5432), minio (9000/9001), titiler (8080)
```

---

## 🛑 Docker-Specific Rules (`Hard Constraints`)

1. **Strictly Optional Status:**
   * Docker tooling is **completely optional**. The QGIS plugin and FastAPI server (`run_backend.py`) must operate cleanly without requiring running Docker containers.
   * Do not introduce hard runtime dependencies in Python code requiring a running PostGIS instance for baseline operations.
2. **Neutral Naming and Security:**
   * Container and database service names must remain neutral (`spatial_postgis`, `spatial_db`, `spatial_minio`).
   * Configuration variables should be easily overridden via a `.env` file.
