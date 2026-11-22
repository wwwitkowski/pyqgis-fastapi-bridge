# Registry of Polish and European Public Spatial Data (GIS)

> Comprehensive reference of official, open state registries, web services (WMS, WFS, WCS, REST API), and remote sensing sources for spatial, environmental, infrastructure, and hydrological analytics in Poland.  
> Source tabular file: [`polish_public_gis_registries.csv`](polish_public_gis_registries.csv).

---

## Table of Contents and Service Categories

1. [Cadastre, Administrative Boundaries & Land Registry](#1-cadastre-administrative-boundaries--land-registry)
2. [Digital Elevation Models, LiDAR & Photogrammetry](#2-digital-elevation-models-lidar--photogrammetry)
3. [Topography, Networks & Infrastructure](#3-topography-networks--infrastructure)
4. [Meteorology, Climate & Weather Radar](#4-meteorology-climate--weather-radar)
5. [Water Bodies, Hydrography & Flood Hazards](#5-water-bodies-hydrography--flood-hazards)
6. [Soil Science, Geology & Mass Movements](#6-soil-science-geology--mass-movements)
7. [Environmental Protection & Air Quality Monitoring](#7-environmental-protection--air-quality-monitoring)
8. [Satellite Remote Sensing (Copernicus & Landsat)](#8-satellite-remote-sensing-copernicus--landsat)
9. [Socioeconomic Statistics (Statistics Poland BDL)](#9-socioeconomic-statistics-statistics-poland-bdl)

---

## 1. Cadastre, Administrative Boundaries & Land Registry

| Registry / Service | Protocol & Format | Endpoint / Source | GIS Analytical Application |
| :--- | :--- | :--- | :--- |
| **ULDK GUGiK** *(Cadastral Parcel Locator)* | REST API (WKT, GeoJSON, GML) | `https://uldk.gugik.gov.pl/` | Real-time retrieval of cadastral parcel geometries and boundaries in EPSG:2180 by TERYT ID or clicked XY point. |
| **KIEG** *(National Cadastre Integration)* | WMS, WFS | `https://integracja.gugik.gov.pl/.../KrajowaIntegracjaEwidencjiGruntow` | Aggregated parcel boundaries, cadastral identifiers, soil classification contours, and land use across all counties in Poland. |
| **PRG** *(State Register of Boundaries)* | WFS, GML, SHP, GeoPackage | `https://geoportal.gov.pl`, WFS GUGiK | Official territorial division of Poland: state, voivodeships, counties, communes, and cadastral districts. |
| **EMUiA** *(Addresses and Streets)* | WMS, WFS, CSV | `https://integracja.gugik.gov.pl/.../KrajowaIntegracjaNumeracjiAdresowej` | Point-level location of address numbers and street centerlines in Poland (geocoding). |
| **PRNG** *(National Register of Geographical Names)* | GML, SHP, GeoPackage, CSV | `https://dane.gov.pl` | Standardized names of settlements, physiographic objects, rivers, peaks, and forests. |
| **BDOO** *(General Geographic Database)* | Shapefile, GeoPackage | `https://dane.gov.pl` | Vector base map at 1:250 000 scale covering the entire country. |
| **LPIS / Reference Parcels ARiMR** | WMS, WFS, SHP, GPKG | `https://geoportal.gov.pl`, `https://dane.gov.pl` | Agricultural parcel reference blocks for direct payments and agricultural parcel identification. |
| **Corine Land Cover (CLC 2018/2024)** | GeoPackage, SHP, GeoTIFF | `https://clc.gios.gov.pl` | Standard European land cover and land use inventory (44 classes) for all of Poland. |
| **Urban Atlas (Copernicus CLMS)** | Shapefile, GeoPackage | `https://land.copernicus.eu` | High-resolution land use classification for Functional Urban Areas (FUA). |

---

## 2. Digital Elevation Models, LiDAR & Photogrammetry

| Registry / Service | Protocol & Format | Endpoint / Source | GIS Analytical Application |
| :--- | :--- | :--- | :--- |
| **NMT GUGiK (1 m Grid DTM)** | WCS, WMS, GeoTIFF, ASCII GRID | `https://mapy.geoportal.gov.pl/.../DigitalTerrainModel` | High-resolution terrain elevation model from airborne laser scanning (LiDAR 1x1 m): slope, aspect, terrain depressions, Topographic Wetness Index (TWI). |
| **NMPT GUGiK (Digital Surface Model - DSM)** | WCS, WMS, GeoTIFF | `https://mapy.geoportal.gov.pl/.../DigitalSurfaceModel` | Elevation model including objects above ground: buildings, forests, trees (wind barrier analysis, shading, ventilation corridors). |
| **Airborne LiDAR Point Clouds (LAS/LAZ)** | LAS, LAZ | `https://geoportal.gov.pl` (PZGiK indexes) | Raw classified airborne laser scanning point clouds (4–12 pts/m²) classifying ground, buildings, and vegetation strata. |
| **Copernicus DEM (GLO-30)** | Cloud Optimized GeoTIFF (COG) | AWS Open Data, Copernicus Space Data | Seamless 30 m digital elevation raster across Europe for macro-regional analytics. |
| **GUGiK Aerial Orthophotomap (RGB/CIR)** | WMS, WMTS, WCS, GeoTIFF | `https://mapy.geoportal.gov.pl/.../StandardResolution` | Aerial photogrammetry with 5–25 cm resolution in true color (RGB) and color infrared (CIR). |

---

## 3. Topography, Networks & Infrastructure

| Registry / Service | Protocol & Format | Endpoint / Source | GIS Analytical Application |
| :--- | :--- | :--- | :--- |
| **BDOT10k (Topographic Database)** | WFS, GML, GeoPackage, SHP | `https://geoportal.gov.pl`, WFS GUGiK | Vector equivalent of 1:10 000 topographic maps: road networks, waterways, buildings, drainage ditches, fences. |
| **GESUT (Utility Networks Integration)** | WMS | `https://integracja.gugik.gov.pl/.../KrajowaIntegracjaUzbrojeniaTerenu` | Underground and aboveground utility networks (water, sewage, gas, power, telecommunications). |
| **OpenStreetMap Poland (Geofabrik)** | PBF, Shapefile (SHP) | `https://download.geofabrik.de/europe/poland.html` | Full OpenStreetMap vector dataset for Poland with daily updates. |
| **GDDKiA (National Road Traffic Census)** | Shapefile, WMS, CSV | `https://www.gov.pl/web/gddkia` | Geometry of national roads and motorways with traffic volume statistics (General Traffic Census). |

---

## 4. Meteorology, Climate & Weather Radar

| Registry / Service | Protocol & Format | Endpoint / Source | GIS Analytical Application |
| :--- | :--- | :--- | :--- |
| **IMGW-PIB Synoptic Observations** | REST API (JSON, CSV, XML) | `https://danepubliczne.imgw.pl/api/data/synop` | Hourly observations from synoptic stations: temperature, precipitation, humidity, wind speed, pressure. |
| **IMGW-PIB Meteorological Telemetry** | REST API (JSON, CSV) | `https://danepubliczne.imgw.pl/api/data/meteo` | 10-minute automated station telemetry: 5 cm soil temperature, 10-minute rainfall sums. |
| **IMGW-PIB Weather Warnings** | REST API (JSON, GeoJSON) | `https://danepubliczne.imgw.pl/api/data/warnings/meteo` | Active meteorological warning alerts by county (frost, thunderstorms, hail, heatwaves, gales). |
| **IMGW-PIB Historical Climate Archives** | CSV (ZIP archives) | `https://danepubliczne.imgw.pl/data/dane_pomiarowo_obserwacyjne/` | Multi-decade historical daily and interval archives for climate model calibration and trend analytics. |
| **POLRAD IMGW (Radar Network)** | WMS, GeoTIFF, HDF5 | `https://danepubliczne.imgw.pl`, WMS IMGW | Radar reflectivity and precipitation intensity maps every 5–10 minutes (storm cell and hail detection). |
| **Open-Meteo Weather & Soil API** | REST API (JSON, CSV) | `https://api.open-meteo.com/v1/forecast` | Free hourly forecasts at 2 km resolution: temperature, wind, soil profile moisture (0–54 cm). |
| **ERA5-Land Reanalysis (ECMWF)** | NetCDF, GRIB | `https://cds.climate.copernicus.eu` | Global land-surface and hydrometeorological reanalysis on a 9 km grid from 1950 to present. |

---

## 5. Water Bodies, Hydrography & Flood Hazards

| Registry / Service | Protocol & Format | Endpoint / Source | GIS Analytical Application |
| :--- | :--- | :--- | :--- |
| **MPHP (Hydrographic Division Map)** | WFS, Shapefile, GeoPackage | `https://dane.gov.pl`, Wody Polskie | Fundamental hydrographic division of Poland: catchment boundaries, watersheds, river centerlines, lakes. |
| **Hydroportal / ISOK (Flood Hazard Maps)** | WMS, WFS, Shapefile | `https://wody.isok.gov.pl` | Flood inundation hazard zones for flood return periods of 10% (1-in-10 years), 1% (1-in-100 years), and 0.2%. |
| **IMGW-PIB Hydrological Data** | REST API (JSON, CSV) | `https://danepubliczne.imgw.pl/api/data/hydro` | Real-time river water stages and discharge rates across river gauges in Poland. |
| **GIOS Water Quality Monitoring** | REST API, CSV, Shapefile | `https://wody.gios.gov.pl` | Physicochemical and biological ecological measurements for surface and groundwater bodies. |

---

## 6. Soil Science, Geology & Mass Movements

| Registry / Service | Protocol & Format | Endpoint / Source | GIS Analytical Application |
| :--- | :--- | :--- | :--- |
| **SMSR IUNG-PIB (Agricultural Drought Monitoring)** | WMS, CSV, Tables | `https://susza.iung.pulawy.pl/` | Decadal Climatic Water Balance (CWB) and agricultural water deficit indicators by commune. |
| **Soil-Agricultural Maps (IUNG/WODGiK)** | WMS, WFS, SHP, GPKG | `https://geoportal.gov.pl` | Soil agricultural suitability complexes (1:25 000 / 1:100 000), genetic soil types, texture, and retention. |
| **Arable Soil Chemistry Monitoring (GIOS)** | CSV, XLS, Shapefile | `https://www.gios.gov.pl/chemizm_gleb/` | Soil pH, organic carbon content, humus, macro- and micro-elements across 216 benchmark monitoring sites. |
| **SMGP & Hydrogeological Map (PIG-PIB)** | WMS, WFS, Shapefile | `https://geologia.pgi.gov.pl` | Detailed Geological Map of Poland (1:50 000), depth to groundwater water table, and permeability. |
| **MIDAS (Mineral Deposits Database PIG-PIB)** | WMS, WFS, Shapefile | `http://midas.pgi.gov.pl` | Locations of mineral deposits, mining areas, and extraction concessions in Poland. |
| **SOPO (Landslide Counteraction System PIG)** | WMS, WFS, Shapefile | `https://osuwiska.pgi.gov.pl` | National inventory of active and dormant landslides and terrain susceptible to mass movements. |
| **SoilGrids 2.0 (ISRIC / ESDAC)** | WCS, COG (GeoTIFF) | `https://rest.isric.org` | Global 250 m soil property rasters (sand, clay, silt fractions, organic carbon, bulk density). |

---

## 7. Environmental Protection & Air Quality Monitoring

| Registry / Service | Protocol & Format | Endpoint / Source | GIS Analytical Application |
| :--- | :--- | :--- | :--- |
| **CRFOP GDOS (Protected Nature Areas)** | WFS, WMS, SHP, GPKG | `https://sdi.gdos.gov.pl/wfs` | Boundaries of Natura 2000 sites, national parks, nature reserves, and landscape parks (buffer analysis). |
| **GIOS Air Quality Portal** | REST API (JSON) | `https://powietrze.gios.gov.pl/pjp/current/api` | Real-time automated air quality monitoring station telemetry (PM10, PM2.5, NO₂, SO₂, O₃, AQI index). |

---

## 8. Satellite Remote Sensing (Copernicus & Landsat)

| Registry / Service | Protocol & Format | Endpoint / Source | GIS Analytical Application |
| :--- | :--- | :--- | :--- |
| **Sentinel-2 L2A (Copernicus CDSE)** | STAC API, COG, S3 | `https://catalogue.dataspace.copernicus.eu/stac` | Multispectral imagery (10–20 m every 2–5 days): Red-Edge, NIR, SWIR bands (NDVI, NDRE, NDMI, moisture). |
| **Sentinel-1 SAR (Copernicus CDSE)** | STAC API, GeoTIFF, S3 | `https://catalogue.dataspace.copernicus.eu/stac` | Synthetic Aperture Radar (SAR): weather-independent surface roughness, soil surface moisture, deformation. |
| **Sentinel-3 SLSTR / OLCI (CDSE)** | STAC API, NetCDF, GeoTIFF | `https://catalogue.dataspace.copernicus.eu/stac` | Daily Land Surface Temperature (LST, 1 km) measurements for detecting urban heat islands and anomalies. |
| **Landsat 8/9 Collection 2** | STAC API, COG (GeoTIFF) | `https://earth-search.aws.element84.com/v1` | Optical (30 m) and thermal TIRS (100 m) multispectral measurements for surface radiation balance. |
| **CLMS High Resolution Vegetation (HR-VPP)** | COG, WMS | `https://land.copernicus.eu` | 10 m vegetation phenology rasters: start, peak, and season length of biomass productivity. |
| **CLMS Soil Water Index (SWI)** | NetCDF, GeoTIFF | `https://land.copernicus.eu` | Daily soil moisture profile index computed from satellite radar observations. |

---

## 9. Socioeconomic Statistics (Statistics Poland BDL)

| Registry / Service | Protocol & Format | Endpoint / Source | GIS Analytical Application |
| :--- | :--- | :--- | :--- |
| **GUS BDL (Local Data Bank)** | REST API (JSON, XML, CSV) | `https://bdl.stat.gov.pl/api/v1/` | Largest official statistical database for communes, counties, and voivodeships (demography, economy, environment). |
