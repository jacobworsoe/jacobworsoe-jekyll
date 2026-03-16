@echo off
REM Export comments from MySQL. Jekyll build runs on GitHub Actions when you push.
REM Run from repo root: scripts\build.bat

cd /d "%~dp0\.."

echo Exporting comments from MySQL...
python scripts\export_wp_comments_mysql.py
if errorlevel 1 (
    echo MySQL export failed.
    exit /b 1
)

echo Done. Commit and push to trigger Jekyll build on GitHub.
