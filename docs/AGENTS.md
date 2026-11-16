# 🤖 Instructions for AI Agents: Documentation Module (`docs/`)

> Before editing files in this directory, review the root [`/AGENTS.md`](../AGENTS.md) and [`/CONTRIBUTING.md`](../CONTRIBUTING.md).

---

## 🎯 Scope and Role of the Module
The `docs/` directory is the central geospatial knowledge base for the project. It contains:
1. Catalog of open Polish and European spatial data services (WMS, WFS, WCS, STAC API, REST).
2. Technical specifications and access descriptions for official public datasets (GUGiK, IMGW, IUNG, GIOS, PIG, Copernicus).
3. Technical guidelines and integration specifications.

---

## 📂 Directory Structure
```text
docs/
├── polish_public_gis_registries.csv   # Structured data sources table (46 official services)
└── polish_public_gis_registries.md    # Detailed guide categorized by domain
```

---

## 🛑 Documentation-Specific Rules (`Hard Constraints`)

1. **Dual-Sync Consistency:**
   * Any change or addition of a data source **must** be mirrored in both files simultaneously:
     * In the machine-readable table `polish_public_gis_registries.csv` (semicolon delimited `;`),
     * In the human-readable guide `polish_public_gis_registries.md` (Markdown table).
2. **Technological Neutrality:**
   * Maintain a neutral, engineering, and geographic reference character as a universal GIS knowledge base.
3. **Link Authenticity:**
   * Only link to verified, official state and institutional portals (e.g. `.gov.pl`, `.imgw.pl`, `.europa.eu` domains).
