@echo off
setlocal
echo ========================================================
echo   Linking QGIS Plugin (PyQGIS FastAPI Bridge)
echo ========================================================

set "TARGET_DIR=%APPDATA%\QGIS\QGIS3\profiles\default\python\plugins\pyqgis_fastapi_bridge"
set "SOURCE_DIR=%~dp0qgis_plugin\pyqgis_fastapi_bridge"

if not exist "%APPDATA%\QGIS\QGIS3\profiles\default\python\plugins" (
    mkdir "%APPDATA%\QGIS\QGIS3\profiles\default\python\plugins"
)

if exist "%TARGET_DIR%" (
    echo Removing existing link...
    rmdir "%TARGET_DIR%"
)

echo Creating directory junction:
echo   Source: %SOURCE_DIR%
echo   Target: %TARGET_DIR%

mklink /J "%TARGET_DIR%" "%SOURCE_DIR%"

if %ERRORLEVEL% EQU 0 (
    echo.
    echo [SUCCESS] PyQGIS FastAPI Bridge plugin linked successfully!
    echo Open QGIS and enable the plugin in: Plugins -^> Manage and Install Plugins.
) else (
    echo.
    echo [ERROR] Failed to create plugin junction.
)

if "%~1"=="" pause
