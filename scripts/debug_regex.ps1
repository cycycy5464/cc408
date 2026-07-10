# Debug script - test regex on one file
$file = "E:\programcc408\cc408\content\docs\computer-org\ch01-data-representation\integers.md"
$content = Get-Content $file -Raw -Encoding UTF8

Write-Host "=== File content (first 12 lines) ===" -ForegroundColor Cyan
$lines = $content -split "`r`n"
for ($idx = 0; $idx -le 12 -and $idx -lt $lines.Count; $idx++) {
    Write-Host "Line $idx: ["$lines[$idx]"]"
}

Write-Host "`n=== Regex tests ===" -ForegroundColor Cyan

# Pattern 1: multiline
$m = $content -match '(?m)^prerequisites:\s*\[\s*\]'
Write-Host "1) (?m)^prerequisites:\s*\[\s*\]  → $m"
if ($m) { Write-Host "   Matched: [$($matches[0])]" }

# Pattern 2: without multiline
$m = $content -match 'prerequisites:\s*\[\s*\]'
Write-Host "2) prerequisites:\s*\[\s*\]  → $m"
if ($m) { Write-Host "   Matched: [$($matches[0])]" }

# Pattern 3: with explicit [regex]::Match
$m2 = [regex]::Match($content, '(?m)^prerequisites:\s*\[\s*\]')
Write-Host "3) [regex]::Match → Success=$($m2.Success) Value=[$($m2.Value)]"

# Pattern 4: try to find the exact string
$targetLine = $lines | Where-Object { $_ -match 'prerequisites' }
Write-Host "4) Line containing 'prerequisites': [$targetLine]"
