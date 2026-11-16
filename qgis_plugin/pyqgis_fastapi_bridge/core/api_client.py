# -*- coding: utf-8 -*-
"""
HTTP client for communicating with the FastAPI backend.
Supports local, Tailscale, and custom remote endpoint URLs.
Executed asynchronously in the background via QgsTask.
"""

import os
import json
import urllib.request
import urllib.error
import urllib.parse

class BackendApiClient:
    DEFAULT_BASE_URL = "http://127.0.0.1:8000/api/v1"

    @classmethod
    def get_base_url(cls, custom_url: str = None) -> str:
        """Resolves API base URL with priority: parameter > env var > default."""
        url = custom_url or os.environ.get("PYQGIS_BRIDGE_API_URL") or os.environ.get("API_BASE_URL")
        if url and url.strip():
            cleaned = url.strip().rstrip("/")
            if not cleaned.endswith("/api/v1"):
                cleaned += "/api/v1"
            return cleaned
        return cls.DEFAULT_BASE_URL

    @classmethod
    def analyze_parcel(cls, parcel_id: str, teryt_id: str = None, lat: float = 52.18, lon: float = 20.76, base_url: str = None):
        """Dispatches an analytical query to the backend."""
        active_url = cls.get_base_url(base_url)
        params = f"?lat={lat:.4f}&lon={lon:.4f}"
        if teryt_id:
            params += f"&teryt_id={urllib.parse.quote(teryt_id)}"

        url = f"{active_url}/analysis/{parcel_id}{params}"
        req = urllib.request.Request(url, headers={"User-Agent": "PyQgisFastApiBridge/1.0"})

        try:
            with urllib.request.urlopen(req, timeout=5) as res:
                return json.loads(res.read().decode("utf-8"))
        except Exception as e:
            return {
                "parcel_id": parcel_id,
                "status": "OFFLINE_FALLBACK",
                "message": f"Cannot connect to API at {active_url}. Verify server is running on Tailscale or locally. Error: {e}",
                "metrics": {
                    "calculated_area_ha": 10.0,
                    "sample_metric": 1.0
                }
            }
