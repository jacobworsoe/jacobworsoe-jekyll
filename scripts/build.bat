@echo off
REM Export posts, pages, and comments from MySQL. Jekyll build runs on GitHub Actions when you push.
REM Run from repo root: scripts\build.bat

cd /d "%~dp0\.."

echo Exporting posts and pages from MySQL...
python scripts\export_wp_posts_pages_mysql.py
if errorlevel 1 (
    echo Posts/pages export failed.
    exit /b 1
)

echo Exporting comments from MySQL...
python scripts\export_wp_comments_mysql.py
if errorlevel 1 (
    echo Comments export failed.
    exit /b 1
)

echo Done. Commit and push to trigger Jekyll build on GitHub.
