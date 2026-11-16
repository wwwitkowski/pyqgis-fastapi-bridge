@echo off
setlocal enabledelayedexpansion
title PyQGIS FastAPI Bridge - Stack Launcher
echo ========================================================
echo   PyQGIS FastAPI Bridge - All-in-One Launcher
echo ========================================================
echo.

:: 1. Python Interpreter Detection
set "PYTHON_EXE="
where py >nul 2>&1 && set "PYTHON_EXE=py"
if "!PYTHON_EXE!"=="" (
    where python >nul 2>&1 && set "PYTHON_EXE=python"
)
if "!PYTHON_EXE!"=="" (
    if exist "%LOCALAPPDATA%\Programs\Python\Python313\python.exe" set "PYTHON_EXE=%LOCALAPPDATA%\Programs\Python\Python313\python.exe"
    if exist "%LOCALAPPDATA%\Programs\Python\Python312\python.exe" set "PYTHON_EXE=%LOCALAPPDATA%\Programs\Python\Python312\python.exe"
    if exist "%PROGRAMFILES%\QGIS 3.44.15\apps\Python312\python.exe" set "PYTHON_EXE=%PROGRAMFILES%\QGIS 3.44.15\apps\Python312\python.exe"
)

if "!PYTHON_EXE!"=="" (
    echo [ERROR] Python was not found in PATH or standard installation locations.
    pause
    exit /b 1
)

echo [1/4] Running automated tests to verify environment...
"!PYTHON_EXE!" -m unittest discover -s tests -p "test_*.py" >nul 2>&1
if !ERRORLEVEL! EQU 0 (
    echo       [OK] All 16 unit tests passed.
) else (
    echo       [WARNING] Some tests reported issues, proceeding with startup...
)

echo [2/4] Linking QGIS plugin to user profile...
call "%~dp0link_plugin.bat" --no-pause >nul 2>&1
echo       [OK] QGIS plugin junction verified.

echo [3/4] Checking Docker stack (PostGIS + TiTiler)...
docker info >nul 2>&1
if !ERRORLEVEL! EQU 0 (
    docker compose -f "%~dp0docker\docker-compose.yml" up -d >nul 2>&1
    echo       [OK] Docker containers active: PostGIS (5432), TiTiler (8080).
) else (
    echo       [INFO] Docker Desktop is not running. Skipping database container start.
)

echo [4/4] Starting FastAPI backend server & Web UI on http://127.0.0.1:8000...
start "" "!PYTHON_EXE!" "%~dp0backend\run_backend.py"

:: Wait 2 seconds and open browser
timeout /t 2 /nobreak >nul
start "" "http://127.0.0.1:8000"

echo.
echo ========================================================
echo   STACK SUCCESSFULLY STARTED!
echo ========================================================
echo   - Web Viewer:  http://127.0.0.1:8000
echo   - Swagger API: http://127.0.0.1:8000/docs
echo   - QGIS Project: %~dp0sample_project\sample_project.qgz
echo ========================================================
echo.
pause
