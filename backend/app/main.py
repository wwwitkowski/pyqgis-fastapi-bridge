# -*- coding: utf-8 -*-
"""
FastAPI application entry point.
Clean communication bridge between FastAPI and the QGIS environment.
"""

import os
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from backend.app.core.config import PROJECT_NAME, API_V1_STR, CORS_ORIGINS
from backend.app.api.v1.router import api_router

app = FastAPI(
    title=PROJECT_NAME,
    openapi_url=f"{API_V1_STR}/openapi.json",
    docs_url="/docs",
    description="Asynchronous spatial analytics backend for the QGIS plugin and web viewer."
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=CORS_ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(api_router, prefix=API_V1_STR)

# Serve web frontend directly from FastAPI
WEB_DIR = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))), "web")
if os.path.exists(WEB_DIR):
    app.mount("/static", StaticFiles(directory=WEB_DIR), name="static")

@app.get("/", include_in_schema=False)
async def serve_index():
    index_file = os.path.join(WEB_DIR, "index.html")
    if os.path.exists(index_file):
        return FileResponse(index_file)
    return {"message": "Web viewer directory not found"}

@app.get("/health", tags=["Status"])
async def health_check():
    return {
        "status": "online",
        "service": PROJECT_NAME,
        "docs_url": "/docs"
    }
