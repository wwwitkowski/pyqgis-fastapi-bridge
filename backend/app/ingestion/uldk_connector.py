# -*- coding: utf-8 -*-
"""
Connector for GUGiK ULDK (Cadastral Parcel Locator Service).
Retrieves geometry of cadastral parcels in Poland (WKT in EPSG:2180).
"""

import urllib.request
import urllib.parse

class UldkConnector:
    """Client for the public GUGiK ULDK API."""

    BASE_URL = "https://uldk.gugik.gov.pl/"

    @classmethod
    def get_parcel_by_id(cls, teryt_id: str):
        """Retrieves parcel geometry by TERYT cadastral identifier."""
        params = {
            "request": "GetParcelById",
            "id": teryt_id,
            "result": "geom,region,commune,county"
        }
        url = f"{cls.BASE_URL}?{urllib.parse.urlencode(params)}"
        req = urllib.request.Request(url, headers={"User-Agent": "PyQgisFastApiBridge/1.0"})

        try:
            with urllib.request.urlopen(req, timeout=5) as res:
                content = res.read().decode("utf-8").strip()
                lines = content.split("\n")
                status = lines[0].strip()
                if status == "0" and len(lines) > 1:
                    parts = lines[1].split(";")
                    wkt = parts[0] if len(parts) > 0 else ""
                    return {
                        "status": "OK",
                        "teryt_id": teryt_id,
                        "wkt_2180": wkt,
                        "raw_info": lines[1:]
                    }
                return {"status": "NOT_FOUND", "message": f"Parcel {teryt_id} was not found in ULDK."}
        except Exception as e:
            return {"status": "ERROR", "message": str(e)}

    @classmethod
    def get_parcel_by_xy(cls, x: float, y: float, epsg: int = 2180):
        """Retrieves parcel identifier and geometry based on point coordinates."""
        params = {
            "request": "GetParcelByXY",
            "xy": f"{x},{y},{epsg}",
            "result": "id,geom"
        }
        url = f"{cls.BASE_URL}?{urllib.parse.urlencode(params)}"
        req = urllib.request.Request(url, headers={"User-Agent": "PyQgisFastApiBridge/1.0"})

        try:
            with urllib.request.urlopen(req, timeout=5) as res:
                content = res.read().decode("utf-8").strip()
                lines = content.split("\n")
                if lines[0].strip() == "0" and len(lines) > 1:
                    parts = lines[1].split(";")
                    return {
                        "status": "OK",
                        "teryt_id": parts[0] if len(parts) > 0 else "",
                        "wkt": parts[1] if len(parts) > 1 else ""
                    }
                return {"status": "NOT_FOUND"}
        except Exception as e:
            return {"status": "ERROR", "message": str(e)}
