# -*- coding: utf-8 -*-
"""
FastAPI backend configuration (PyQGIS FastAPI Bridge).
Tailscale and peer-to-peer ready configuration.
"""

import os

PROJECT_NAME = "PyQGIS FastAPI Bridge API"
API_V1_STR = "/api/v1"

# Server host & port binding
# Binding to 0.0.0.0 allows incoming connections across Tailscale mesh network (100.x.y.z) and local interfaces
BACKEND_HOST = os.environ.get("HOST", "0.0.0.0")
BACKEND_PORT = int(os.environ.get("PORT", "8000"))

# Base API URL used for client and team connectivity (e.g. http://<tailscale-ip>:8000/api/v1)
API_BASE_URL = os.environ.get("API_BASE_URL", f"http://{BACKEND_HOST}:{BACKEND_PORT}{API_V1_STR}")

# Polish public geodetic and meteorological services (open public data)
ULDK_API_URL = os.environ.get("GUGIK_ULDK_URL", "https://uldk.gugik.gov.pl/")
IMGW_SYNOP_URL = os.environ.get("IMGW_SYNOP_URL", "https://danepubliczne.imgw.pl/api/data/synop")
IMGW_WARNINGS_URL = os.environ.get("IMGW_WARNINGS_URL", "https://danepubliczne.imgw.pl/api/data/warnings/meteo")

# Allowed CORS origins (allows team members connecting over Tailscale, MagicDNS, or web preview)
CORS_ORIGINS = ["*"]
