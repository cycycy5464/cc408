# Test the regex replacement on one file (no special chars)
$file = "E:\programcc408\cc408\content\docs\computer-org\ch01-data-representation\integers.md"
$content = Get-Content $file -Raw -Encoding UTF8

# Build replacement
$prevTitles = @("概论", "计算机性能指标", "计算机系统层次结构")
$quoted = $prevTitles -join '", "'
$replacement = 'prerequisites: ["' + $quoted + '"]'
Write-Host ("Replacement: " + $replacement)

# Apply regex
$newContent = $content -replace '(?m)^prerequisites:\s*\[\s*\]', $replacement

if ($newContent -ne $content) {
    Write-Host ("OK - Match found, file would be modified")
    $oldLines = $content -split "`r`n"
    $newLines = $newContent -split "`r`n"
    for ($i = 0; $i -lt $oldLines.Count; $i++) {
        if ($oldLines[$i] -ne $newLines[$i]) {
            Write-Host ("Line " + $i + ": OLD=[" + $oldLines[$i] + "]")
            Write-Host ("         NEW=[" + $newLines[$i] + "]")
        }
    }
} else {
    Write-Host ("FAIL - No match")
}
