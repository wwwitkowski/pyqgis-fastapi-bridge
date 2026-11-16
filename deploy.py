#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Cross-platform deployment script for the QGIS plugin (PyQGIS FastAPI Bridge).
Works on Windows, macOS, and Linux.
"""

import os
import sys
import platform
import subprocess

PLUGIN_NAME = "pyqgis_fastapi_bridge"
PROFILE_NAME = "default"

def get_qgis_plugin_dir():
    system = platform.system()
    home = os.path.expanduser("~")

    if system == "Windows":
        appdata = os.environ.get("APPDATA")
        if not appdata:
            appdata = os.path.join(home, "AppData", "Roaming")
        return os.path.join(appdata, "QGIS", "QGIS3", "profiles", PROFILE_NAME, "python", "plugins")
    elif system == "Darwin":
        return os.path.join(home, "Library", "Application Support", "QGIS", "QGIS3", "profiles", PROFILE_NAME, "python", "plugins")
    else:
        return os.path.join(home, ".local", "share", "QGIS", "QGIS3", "profiles", PROFILE_NAME, "python", "plugins")

def link_plugin():
    script_dir = os.path.dirname(os.path.abspath(__file__))
    source_dir = os.path.join(script_dir, "qgis_plugin", PLUGIN_NAME)
    target_dir = os.path.join(get_qgis_plugin_dir(), PLUGIN_NAME)

    print("=" * 60)
    print(f" Deploying QGIS plugin: {PLUGIN_NAME}")
    print(f" Operating system: {platform.system()} ({platform.release()})")
    print(f" Source: {source_dir}")
    print(f" Target (QGIS): {target_dir}")
    print("=" * 60)

    if not os.path.exists(source_dir):
        print(f"[ERROR] Plugin source directory does not exist: {source_dir}")
        sys.exit(1)

    plugins_parent = os.path.dirname(target_dir)
    os.makedirs(plugins_parent, exist_ok=True)

    if os.path.lexists(target_dir):
        print(f"Removing existing link at: {target_dir}")
        if os.path.islink(target_dir):
            os.unlink(target_dir)
        elif os.path.isdir(target_dir):
            if platform.system() == "Windows":
                try:
                    os.rmdir(target_dir)
                except OSError:
                    import shutil
                    shutil.rmtree(target_dir)
            else:
                import shutil
                shutil.rmtree(target_dir)

    try:
        if platform.system() == "Windows":
            cmd = f'mklink /J "{target_dir}" "{source_dir}"'
            ret = subprocess.run(cmd, shell=True, capture_output=True, text=True)
            if ret.returncode != 0:
                os.symlink(source_dir, target_dir, target_is_directory=True)
        else:
            os.symlink(source_dir, target_dir, target_is_directory=True)

        print("\n[SUCCESS] Plugin successfully linked to QGIS!")
        print("Launch QGIS and enable the plugin: Plugins -> Manage and Install Plugins -> PyQGIS FastAPI Bridge.")
    except Exception as e:
        print(f"\n[ERROR] Failed to link plugin: {e}")
        sys.exit(1)

if __name__ == "__main__":
    link_plugin()
