#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Script to start the FastAPI development server.
Binds to 0.0.0.0 by default so services are reachable over Tailscale among team members.
Usage: python backend/run_backend.py
"""

import sys
import os

# Add project root directory to PYTHONPATH
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if BASE_DIR not in sys.path:
    sys.path.insert(0, BASE_DIR)

from backend.app.core.config import BACKEND_HOST, BACKEND_PORT

if __name__ == "__main__":
    import uvicorn
    print("=" * 65)
    print(f" Starting Backend API on host '{BACKEND_HOST}', port {BACKEND_PORT}")
    print(f" Local URL:       http://127.0.0.1:{BACKEND_PORT}")
    print(f" Tailscale/LAN:   http://<tailscale-ip-or-magicdns>:{BACKEND_PORT}")
    print(f" Documentation:   http://127.0.0.1:{BACKEND_PORT}/docs")
    print(f" Health Check:    http://127.0.0.1:{BACKEND_PORT}/health")
    print("=" * 65)
    uvicorn.run("backend.app.main:app", host=BACKEND_HOST, port=BACKEND_PORT, reload=True)
