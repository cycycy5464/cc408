@echo off
echo ========================================
echo CC408 Local Dev Server (Optimized)
echo ========================================

echo [1/3] Cleaning Hugo cache...
if exist "resources\_gen" rd /s /q "resources\_gen"
if exist "public" rd /s /q "public"

echo [2/3] Starting dev server...
echo.
echo Optimized config:
echo   - Disabled git info
echo   - Disabled robots.txt
echo   - Disabled emoji
echo   - HTML output only
echo   - Using local config
echo.
echo URL: http://localhost:1313/cc408/
echo Press Ctrl+C to stop
echo.

hugo server -D --gc --renderToDisk --disableLiveReload --config config/_default/hugo.yaml,config/local-dev.yaml

pause
