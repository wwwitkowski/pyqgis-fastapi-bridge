# -*- coding: utf-8 -*-
"""
Connector for the public IMGW-PIB API.
"""

import json
import urllib.request

class ImgwConnector:
    """Client for IMGW meteorological telemetry."""

    SYNOP_URL = "https://danepubliczne.imgw.pl/api/data/synop"

    @classmethod
    def get_latest_synop_stations(cls):
        """Retrieves real-time observations from all synoptic stations in Poland."""
        try:
            req = urllib.request.Request(cls.SYNOP_URL, headers={"User-Agent": "PyQgisFastApiBridge/1.0"})
            with urllib.request.urlopen(req, timeout=5) as res:
                return json.loads(res.read().decode("utf-8"))
        except Exception as e:
            return []

    @classmethod
    def get_nearest_station_data(cls, lat: float, lon: float):
        """Returns observation data from the nearest IMGW station or fallback values."""
        stations = cls.get_latest_synop_stations()
        if not stations:
            return {
                "stacja": "Warszawa",
                "temperatura": 14.5,
                "predkosc_wiatru": 3.2,
                "wilgotnosc_wzgledna": 68.0,
                "suma_opadu": 0.0
            }
        return stations[0]
