# -*- coding: utf-8 -*-
"""
Polish coordinate reference system constants and geographic bounding boxes.
Principle: metric calculations in Poland are executed in EPSG:2180 (distortion-free area measurements).
"""

EPSG_POLAND_1992 = 2180   # Poland CS92 (metric, official national spatial reference system)
EPSG_WGS84 = 4326         # WGS 84 (decimal degrees, GPS, global API standard)
EPSG_WEB_MERCATOR = 3857  # Web Mercator (raster tiles, MapLibre, OpenStreetMap)

# Bounding box of Poland in EPSG:4326 [min_lon, min_lat, max_lon, max_lat]
BBOX_POLAND_4326 = [14.12, 49.00, 24.15, 54.84]

# Bounding box of Poland in EPSG:2180 [min_x, min_y, max_x, max_y]
BBOX_POLAND_2180 = [170000.0, 130000.0, 860000.0, 780000.0]
