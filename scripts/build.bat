@echo off
REM Export posts, pages, and comments from MySQL. Jekyll build runs on GitHub Actions when you push.
REM Run from repo root: scripts\build.bat

cd /d "%~dp0\.."

echo MySQL export (posts, pages, comments)...
python scripts\export_all.py
if errorlevel 1 (
    echo Export failed.
    exit /b 1
)

echo Done. Commit and push to trigger Jekyll build on GitHub.
