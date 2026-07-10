# Populate prerequisites based on chapter sequence
$contentDir = "E:\programcc408\cc408\content\docs"
$subjects = @{}

# Phase 1: Collect all files with titles
Write-Host "📖 Scanning all docs files..." -ForegroundColor Cyan
Get-ChildItem -Path $contentDir -Recurse -Filter "*.md" | Where-Object { $_.Name -ne "_index.md" } | ForEach-Object {
    $relPath = $_.FullName.Substring($contentDir.Length + 1)
    $parts = $relPath -split "\\"
    if ($parts.Count -lt 2) { return }

    $subject = $parts[0]
    $chapter = $parts[1]
    if ($chapter -notmatch '^ch(\d+)') { return }
    $chNum = [int]$matches[1]

    $content = Get-Content $_.FullName -Raw -Encoding UTF8
    $titleMatch = [regex]::Match($content, '(?m)^title:\s*"?(.+?)"?\s*$')
    $title = if ($titleMatch.Success) { $titleMatch.Groups[1].Value.Trim().Trim('"', "'") } else { $_.BaseName }

    if (-not $subjects.ContainsKey($subject)) { $subjects[$subject] = @{} }
    if (-not $subjects[$subject].ContainsKey($chNum)) { $subjects[$subject][$chNum] = @() }
    $subjects[$subject][$chNum] += @{File = $_.FullName; Title = $title}
}

# Phase 2: Populate prerequisites
Write-Host "🔗 Populating prerequisites..." -ForegroundColor Cyan
$totalFilesModified = 0

foreach ($sub in ($subjects.Keys | Sort-Object)) {
    $chs = $subjects[$sub]
    $sortedCh = $chs.Keys | Sort-Object

    for ($i = 1; $i -lt $sortedCh.Count; $i++) {
        $ch = $sortedCh[$i]
        $prevCh = $sortedCh[$i-1]
        $prevTitles = $chs[$prevCh] | ForEach-Object { $_.Title }

        foreach ($item in $chs[$ch]) {
            $content = Get-Content $item.File -Raw -Encoding UTF8
            $prereqStr = 'prerequisites: ["' + ($prevTitles -join '", "') + '"]'

            # Match prerequisites: [] (possibly with whitespace) and replace
            $newContent = $content -replace '(?m)^prerequisites:\s*\[\s*\]', $prereqStr

            if ($newContent -ne $content) {
                [System.IO.File]::WriteAllText($item.File, $newContent, [System.Text.Encoding]::UTF8)
                $totalFilesModified++
                Write-Host "  ✅ $($item.File) ← $($prevTitles -join ', ')" -ForegroundColor Green
            }
        }
    }
}

Write-Host "`n🎉 Done! Modified $totalFilesModified files." -ForegroundColor Green
