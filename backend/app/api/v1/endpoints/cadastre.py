# -*- coding: utf-8 -*-
"""
Endpoints for cadastral data ingestion (GUGiK ULDK).
"""

from fastapi import APIRouter, HTTPException
from backend.app.ingestion.uldk_connector import UldkConnector

router = APIRouter()

@router.get("/uldk/{teryt_id}")
async def get_parcel_from_uldk(teryt_id: str):
    """Retrieves cadastral parcel geometry directly from the GUGiK ULDK service."""
    res = UldkConnector.get_parcel_by_id(teryt_id)
    if res.get("status") == "ERROR":
        raise HTTPException(status_code=502, detail=res.get("message"))
    if res.get("status") == "NOT_FOUND":
        raise HTTPException(status_code=404, detail=res.get("message"))
    return res

@router.get("/uldk/by-xy/{x}/{y}")
async def get_parcel_by_coordinates(x: float, y: float, epsg: int = 2180):
    """Retrieves parcel identifier and geometry based on point coordinates (X, Y)."""
    res = UldkConnector.get_parcel_by_xy(x, y, epsg)
    return res
