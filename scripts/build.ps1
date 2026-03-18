# Export posts, pages, and comments from MySQL. Jekyll build runs on GitHub Actions when you push.
# Run from repo root: .\scripts\build.ps1

$ErrorActionPreference = "Stop"
$repoRoot = (Get-Item $PSScriptRoot).Parent.FullName
Push-Location $repoRoot

try {
    Write-Host "MySQL export (posts, pages, comments)..." -ForegroundColor Cyan
    python scripts/export_all.py
    if ($LASTEXITCODE -ne 0) { throw "Export failed with exit code $LASTEXITCODE" }
    Write-Host "Done. Commit and push to trigger Jekyll build on GitHub." -ForegroundColor Green
} finally {
    Pop-Location
}
