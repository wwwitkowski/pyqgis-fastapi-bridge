# Docker Guidelines (`docker/`)

Review root `AGENTS.md` and `CONTRIBUTING.md` before making modifications.

---

## Scope and Role
The `docker/` directory contains optional container orchestration files for deploying auxiliary spatial services:
1. **PostGIS** spatial database (`postgis/postgis:15-3.3` on port 5432).
2. **MinIO** S3-compatible object store for Cloud Optimized GeoTIFF (COG) rasters (ports 9000/9001).
3. **TiTiler** dynamic tile server (`ghcr.io/developmentseed/titiler` on port 8080).

---

## Directory Structure
```text
docker/
└── docker-compose.yml       # PostGIS, MinIO, and TiTiler service definitions
```

---

## Guidelines
1. **Strictly optional:** The baseline project (FastAPI backend, QGIS plugin, and web viewer) operates without Docker. Do not introduce hard runtime dependencies on running containers.
2. **Neutral naming:** Keep service and container names generic (`spatial_postgis`, `spatial_minio`, `titiler`).
3. **Configuration:** Keep credentials configurable via environment variables in `.env`.
