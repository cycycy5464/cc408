$simulateDir = "E:\programcc408\cc408\content\exam\simulate"
$outputDir = "E:\programcc408\cc408\content\question"

$subjectAbbr = @{
    "数据结构" = "ds"
    "计算机组成原理" = "co"
    "操作系统" = "os"
    "计算机网络" = "cn"
}

$date = "2026-07-08"

for ($setNum = 1; $setNum -le 8; $setNum++) {
    $file = Join-Path $simulateDir "set-$setNum.md"
    if (-not (Test-Path $file)) { Write-Host "MISSING: $file"; continue }

    $lines = Get-Content $file
    $inFrontmatter = $false
    $currentSubject = ""
    $currentQnum = ""
    $currentContent = @()
    $totalSaved = 0

    foreach ($line in $lines) {
        # skip frontmatter
        if ($line -match '^---$') { $inFrontmatter = -not $inFrontmatter; continue }
        if ($inFrontmatter) { continue }

        # subject heading
        if ($line -match '^####\s+(.+?)\s*$') {
            $currentSubject = $matches[1].Trim()
            continue
        }

        # question number heading
        if ($line -match '^#####\s+(\d+)') {
            # save previous question
            if ($currentQnum -ne "" -and $currentSubject -ne "") {
                Save-Question
            }
            $currentQnum = $matches[1]
            $currentContent = @()
            continue
        }

        if ($currentQnum -ne "") {
            $currentContent += $line
        }
    }

    # save last question
    if ($currentQnum -ne "" -and $currentSubject -ne "") {
        Save-Question
    }

    Write-Host "Set $setNum`: $totalSaved questions saved"
}

function Save-Question {
    $num = [int]$currentQnum
    $isComprehensive = $num -ge 41
    $qtype = if ($isComprehensive) { "comprehensive" } else { "choice" }
    $difficulty = if ($isComprehensive) { 4 } else { 3 }

    $abbr = $subjectAbbr[$currentSubject]
    $numPadded = $num.ToString("D3")
    $filename = "simulate-$setNum-$abbr-$numPadded.md"
    $filepath = Join-Path $outputDir $filename

    $title = "模拟卷$setNum $currentSubject 第${num}题"

    # Build frontmatter
    $fm = @(
        "---",
        "title: `"$title`"",
        "date: $date",
        "type: question",
        "source: `"模拟题`"",
        "set: $setNum",
        "subjects:",
        "  - `"$currentSubject`"",
        "knowledge_points:",
        "  - `"$currentSubject`"",
        "question_type: `"$qtype`"",
        "difficulty: $difficulty",
        "number: $num",
        "---"
    )

    # Clean content: remove leading blank lines, keep trailing structure
    $content = $currentContent -join "`n"
    $content = $content.TrimStart()

    $fullContent = ($fm -join "`n") + "`n`n" + $content + "`n"
    [System.IO.File]::WriteAllText($filepath, $fullContent, [System.Text.Encoding]::UTF8)
    $script:totalSaved++
}
