# Analyze docs content structure and show prerequisites mapping
$contentDir = "E:\programcc408\cc408\content\docs"
$subjects = @{}

# Walk through all files
Get-ChildItem -Path $contentDir -Recurse -Filter "*.md" | Where-Object { $_.Name -ne "_index.md" } | ForEach-Object {
    $relPath = $_.FullName.Substring($contentDir.Length + 1)
    $parts = $relPath -split "\\"
    if ($parts.Count -lt 2) { return }

    $subject = $parts[0]
    $chapter = $parts[1]

    if ($chapter -notmatch '^ch(\d+)') { return }
    $chNum = [int]$matches[1]

    # Extract title from frontmatter (multiline: (?m) makes ^/$ match per line)
    $content = Get-Content $_.FullName -Raw -Encoding UTF8
    $titleMatch = [regex]::Match($content, '(?m)^title:\s*"?(.+?)"?\s*$')
    if ($titleMatch.Success) {
        $title = $titleMatch.Groups[1].Value.Trim().Trim('"', "'")
    } else {
        $title = $_.BaseName
    }

    if (-not $subjects.ContainsKey($subject)) {
        $subjects[$subject] = @{}
    }
    if (-not $subjects[$subject].ContainsKey($chNum)) {
        $subjects[$subject][$chNum] = @()
    }
    $subjects[$subject][$chNum] += @{File = $_.FullName; Title = $title; Name = $_.Name}
}

# Display structure
$totalNodes = 0
$totalEdges = 0

Write-Host "Subjects: $($subjects.Keys -join ', ')" -ForegroundColor Green

foreach ($sub in ($subjects.Keys | Sort-Object)) {
    $chs = $subjects[$sub]
    $sortedCh = $chs.Keys | Sort-Object
    $counts = ($sortedCh | ForEach-Object { $chs[$_].Count })
    $total = ($counts | Measure-Object -Sum).Sum
    Write-Host "`n=== $sub ($total files, $($sortedCh.Count) chapters) ===" -ForegroundColor Cyan

    for ($i = 0; $i -lt $sortedCh.Count; $i++) {
        $ch = $sortedCh[$i]
        $titles = $chs[$ch] | ForEach-Object { $_.Title }
        Write-Host "  ch$("{0:D2}" -f $ch): $($titles -join ', ')"

        if ($i -gt 0) {
            $prevCh = $sortedCh[$i-1]
            $nPrev = $chs[$prevCh].Count
            $nCur = $chs[$ch].Count
            $edges = $nPrev * $nCur
            $totalEdges += $edges
            Write-Host "         <= $nPrev prereqs x $nCur files = $edges edges" -ForegroundColor DarkYellow
        }
    }
    $totalNodes += $total
}

Write-Host "`n--- Total: $totalNodes nodes, ~$totalEdges edges ---" -ForegroundColor Green
