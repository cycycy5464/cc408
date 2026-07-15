@echo off
REM Hugo 本地开发优化启动脚本

echo ========================================
echo CC408 本地开发服务器 (优化版)
echo ========================================

REM 清理缓存
echo [1/3] 清理 Hugo 缓存...
if exist "resources\_gen" rd /s /q "resources\_gen"
if exist "public" rd /s /q "public"

REM 启动优化的开发服务器
echo [2/3] 启动开发服务器...
echo.
echo 优化配置:
echo   - 禁用 git 信息
echo   - 禁用 robots.txt  
echo   - 禁用 emoji 处理
echo   - 只生成 HTML 输出
echo   - 使用本地配置
echo.
echo 访问地址: http://localhost:1313/cc408/
echo 按 Ctrl+C 停止服务器
echo.

REM 使用优化配置启动
hugo server -D --gc --renderToDisk --disableLiveReload --config config/_default/hugo.yaml,config/local-dev.yaml

pause
