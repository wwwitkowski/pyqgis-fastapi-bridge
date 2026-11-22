# Documentation Guidelines (`docs/`)

Review root `AGENTS.md` and `CONTRIBUTING.md` before making modifications.

---

## Scope and Role
The `docs/` directory maintains the geospatial knowledge base for the project:
1. Catalog of open Polish and European spatial data services (WMS, WFS, WCS, STAC API, REST).
2. Technical specifications for public datasets (GUGiK, IMGW, IUNG, GIOŚ, PIG, Copernicus).
3. Screenshot assets for visual documentation (`docs/images/`).

---

## Directory Structure
```text
docs/
├── images/                            # System screenshots for README and documentation
├── polish_public_gis_registries.csv   # Machine-readable registry catalog
└── polish_public_gis_registries.md    # Detailed reference guide categorized by domain
```

---

## Guidelines
1. **Sync consistency:** Any added or updated spatial data source must be reflected in both the CSV table (`polish_public_gis_registries.csv`) and the Markdown guide (`polish_public_gis_registries.md`).
2. **Verified endpoints:** Only reference verified, official public portals (`.gov.pl`, `.imgw.pl`, `.europa.eu`).
3. **Screenshot organization:** Keep visual assets inside `docs/images/`.
