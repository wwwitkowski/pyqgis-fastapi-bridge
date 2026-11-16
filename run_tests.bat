@echo off
setlocal enabledelayedexpansion
echo ========================================================
echo   Running Unit Test Suite (PyQGIS Bridge)
echo ========================================================

:: Detect functional Python interpreter
set "PYTHON_EXE="

:: 1. Check if 'python' in PATH works
python --version >nul 2>&1
if !ERRORLEVEL! EQU 0 set "PYTHON_EXE=python"

:: 2. Check Python Launcher 'py'
if "!PYTHON_EXE!"=="" (
    py --version >nul 2>&1
    if !ERRORLEVEL! EQU 0 set "PYTHON_EXE=py"
)

:: 3. Check standard Python versions in LOCALAPPDATA
if "!PYTHON_EXE!"=="" (
    for /d %%P in ("%LOCALAPPDATA%\Programs\Python\Python3*") do (
        if exist "%%~fP\python.exe" set "PYTHON_EXE=%%~fP\python.exe"
    )
)

:: 4. Check QGIS bundled Python dynamically across all installed versions
if "!PYTHON_EXE!"=="" (
    for /d %%Q in ("%PROGRAMFILES%\QGIS*") do (
        for /d %%P in ("%%~fQ\apps\Python3*") do (
            if exist "%%~fP\python.exe" set "PYTHON_EXE=%%~fP\python.exe"
        )
    )
)

if "!PYTHON_EXE!"=="" (
    echo [ERROR] Python interpreter not found in PATH or standard locations.
    echo Please install Python or run tests inside a virtual environment.
    pause
    exit /b 1
)

echo Using Python interpreter: "!PYTHON_EXE!"
echo.

"!PYTHON_EXE!" -m unittest discover -s tests -p "test_*.py" -v

if !ERRORLEVEL! EQU 0 (
    echo.
    echo [SUCCESS] All tests passed successfully!
) else (
    echo.
    echo [ERROR] Some tests failed.
)

if "%~1"=="" pause
