@echo off
setlocal enabledelayedexpansion
echo ========================================================
echo   Launching Qt Designer with QGIS widgets
echo ========================================================

set "UI_FILE=%~dp0qgis_plugin\pyqgis_fastapi_bridge\gui\dockwidget.ui"
set "DESIGNER_BAT="

:: 1. Check if QGIS_DESIGNER_BAT is explicitly set in environment
if defined QGIS_DESIGNER_BAT (
    if exist "%QGIS_DESIGNER_BAT%" set "DESIGNER_BAT=%QGIS_DESIGNER_BAT%"
)

:: 2. Check if qgis-designer.bat is in PATH
if "!DESIGNER_BAT!"=="" (
    where qgis-designer.bat >nul 2>&1
    if !ERRORLEVEL! EQU 0 (
        for /f "delims=" %%I in ('where qgis-designer.bat 2^>nul') do (
            if "!DESIGNER_BAT!"=="" set "DESIGNER_BAT=%%I"
        )
    )
)

:: 3. Check OSGeo4W installations dynamically
if "!DESIGNER_BAT!"=="" (
    for %%D in ("%SystemDrive%\OSGeo4W" "%SystemDrive%\OSGeo4W64" "%PROGRAMFILES%\OSGeo4W" "%PROGRAMFILES%\OSGeo4W64") do (
        if exist "%%~fD\bin\qgis-designer.bat" (
            set "DESIGNER_BAT=%%~fD\bin\qgis-designer.bat"
        )
    )
)

:: 4. Search dynamically for any installed QGIS 3.x version in Program Files
if "!DESIGNER_BAT!"=="" (
    for /d %%G in ("%PROGRAMFILES%\QGIS*" "%PROGRAMFILES(X86)%\QGIS*" "%LOCALAPPDATA%\Programs\QGIS*") do (
        if exist "%%~fG\bin\qgis-designer.bat" (
            set "DESIGNER_BAT=%%~fG\bin\qgis-designer.bat"
        )
    )
)

if "!DESIGNER_BAT!"=="" (
    echo [ERROR] qgis-designer.bat was not found in PATH or standard QGIS installation directories.
    echo Please ensure QGIS is installed or set the QGIS_DESIGNER_BAT environment variable.
    pause
    exit /b 1
)

echo Found QGIS Designer: "!DESIGNER_BAT!"
echo Opening UI file: "!UI_FILE!"
start "" "!DESIGNER_BAT!" "!UI_FILE!"
