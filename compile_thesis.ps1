<#
.SYNOPSIS
    Automated XeLaTeX/XePersian build and verification script for the doctoral dissertation.

.DESCRIPTION
    Compiles thesis_full_toc_persian_v3.tex (or any specified target or single chapter) using XeLaTeX and BibTeX,
    validates the build log against zero-defect criteria (verify_build.py),
    and enforces post-compilation cleanup (clean_build.py).
    By default, all chapters are compiled as part of the complete dissertation.
    When -Chapter <N> is specified, only that specific chapter is compiled.

.PARAMETER Target
    The root LaTeX file to compile. Default: 'thesis_full_toc_persian_v3.tex'.

.PARAMETER Chapter
    Optional chapter number (1, 2, 3, 4, 5, 6), 'appendices', or comma-separated list of chapters (e.g. '4,5') to compile single or combined chapters.
    When omitted, compiles all chapters.

.PARAMETER Fast
    Runs a single XeLaTeX pass without BibTeX or extra passes (for quick draft preview).

.PARAMETER NoBib
    Skips the BibTeX execution pass.

.PARAMETER NoClean
    Retains intermediate and auxiliary build artifacts (.aux, .log, .toc, etc.) for debugging.

.PARAMETER NoVerify
    Skips the Python log verification check.

.PARAMETER Open
    Opens the resulting PDF in the default system viewer upon successful compilation.

.EXAMPLE
    .\compile_thesis.ps1
    Full end-to-end build of all chapters (XeLaTeX -> BibTeX -> XeLaTeX x2 -> Verify -> Clean).

.EXAMPLE
    .\compile_thesis.ps1 -Chapter 4
    Compiles only Chapter 4 with full multi-pass and chapter verification.

.EXAMPLE
    .\compile_thesis.ps1 -Chapter 4,5
    Compiles a unified PDF of Chapters 4 and 5 (chapter4_5.pdf).

.EXAMPLE
    .\compile_thesis.ps1 -Chapter 5 -Fast -Open
    Fast single-pass compilation of Chapter 5 and opens the resulting chapter5.pdf.
#>

[CmdletBinding()]
param(
    [string]$Target = "thesis_full_toc_persian_v3.tex",
    [string[]]$Chapter = @(),
    [switch]$Fast,
    [switch]$NoBib,
    [switch]$NoClean,
    [switch]$NoVerify,
    [switch]$Open
)

$ErrorActionPreference = "Stop"

function Write-Banner([string]$Message, [System.ConsoleColor]$Color = [System.ConsoleColor]::Cyan) {
    $line = "=" * 70
    Write-Host ""
    Write-Host $line -ForegroundColor $Color
    Write-Host "  $Message" -ForegroundColor $Color
    Write-Host $line -ForegroundColor $Color
    Write-Host ""
}

function Write-Step([string]$StepName, [string]$Details) {
    Write-Host "[STEP] " -ForegroundColor Yellow -NoNewline
    Write-Host "$($StepName): " -ForegroundColor White -NoNewline
    Write-Host $Details -ForegroundColor Gray
}

function Write-Success([string]$Message) {
    Write-Host "[SUCCESS] " -ForegroundColor Green -NoNewline
    Write-Host $Message -ForegroundColor White
}

function Write-Failure([string]$Message) {
    Write-Host "[ERROR] " -ForegroundColor Red -NoNewline
    Write-Host $Message -ForegroundColor White
}

# 1. Resolve paths
$ScriptDir = Split-Path -Parent $MyInvocation.MyCommand.Path
Set-Location $ScriptDir

# Chapter resolution map
$ChapterMap = @{
    "1" = "chapters\chapter1.tex"
    "2" = "chapters\chapter2.tex"
    "3" = "chapters\chapter3.tex"
    "4" = "chapters\chapter4.tex"
    "5" = "chapters\chapter5.tex"
    "6" = "chapters\chapter6.tex"
    "ch1" = "chapters\chapter1.tex"
    "ch2" = "chapters\chapter2.tex"
    "ch3" = "chapters\chapter3.tex"
    "ch4" = "chapters\chapter4.tex"
    "ch5" = "chapters\chapter5.tex"
    "ch6" = "chapters\chapter6.tex"
    "appendices" = "chapters\appendices.tex"
    "appendix" = "chapters\appendices.tex"
    "app" = "chapters\appendices.tex"
}

$IsSingleChapter = $false
$IsMultiChapter = $false
$cleanNums = @()

$ChapterTokens = @()
if ($Chapter -and $Chapter.Count -gt 0) {
    foreach ($item in $Chapter) {
        if (-not [string]::IsNullOrWhiteSpace($item)) {
            $parts = $item -split '[,+\s]+' | Where-Object { -not [string]::IsNullOrWhiteSpace($_) }
            $ChapterTokens += $parts
        }
    }
}

if ($ChapterTokens.Count -eq 1) {
    $chapKey = $ChapterTokens[0].Trim().ToLower()
    if ($ChapterMap.ContainsKey($chapKey)) {
        $Target = $ChapterMap[$chapKey]
        $IsSingleChapter = $true
    } else {
        Write-Failure "Invalid chapter specified: '$($ChapterTokens[0])'. Valid values: 1, 2, 3, 4, 5, 6, appendices, or combinations like 4,5"
        exit 1
    }
} elseif ($ChapterTokens.Count -gt 1) {
    $validKeys = @()
    foreach ($token in $ChapterTokens) {
        $k = $token.Trim().ToLower()
        if (-not $ChapterMap.ContainsKey($k)) {
            Write-Failure "Invalid chapter in combination: '$token'. Valid values: 1, 2, 3, 4, 5, 6, appendices"
            exit 1
        }
        $validKeys += $k
        $num = $k -replace '^ch', ''
        $cleanNums += $num
    }

    $BaseName = "chapter" + ($cleanNums -join "_")
    $Target = "$BaseName.tex"
    $IsSingleChapter = $true
    $IsMultiChapter = $true

    # Auto-generate combination wrapper .tex if not already created
    if (-not (Test-Path $Target)) {
        Write-Step "Generate Wrapper" "Creating unified multi-chapter template: $Target"
        $inputLines = foreach ($vk in $validKeys) {
            $src = $ChapterMap[$vk] -replace '\\', '/' -replace '\.tex$', ''
            "\input{$src}"
        }
        $texTemplate = @"
\documentclass[oneside,openany,phd]{TMU-Thesis}
\usepackage{docmute}

% مشخصات رساله
\university{تربیت مدرس}
\faculty{مهندسی برق و کامپیوتر}
\department{گروه هوش مصنوعی و رباتیکز}
\subject{مهندسی کامپیوتر}
\field{مهندسی نرم‌افزار}
\credits{---}
\title{یادگیری تقویتی عمیق با شکل‌دهی تصادفی پاداش برای مدیریت عدم قطعیت در سیستم‌های خودوفق}
\firstsupervisor{دکتر ...}
\firstadvisor{دکتر ...}
\name{علیرضا}
\surname{کاویانی‌فر}
\studentID{...}
\thesisdate{بهمن ۱۴۰۴}

\latinuniversity{Tarbiat Modares University}
\latinfaculty{Faculty of Electrical and Computer Engineering}
\latinsubject{Computer Engineering}
\latinfield{Software Engineering}
\latintitle{Randomized Reward-Shaped Deep Reinforcement Learning for Managing Uncertainty in Self-Adaptive Systems}
\firstlatinsupervisor{Dr. ...}
\firstlatinadvisor{Dr. ...}
\latinname{Alireza}
\latinsurname{Kavianifar}
\latinthesisdate{February 2026}
\latinkeywords{Self-Adaptive Systems, Deep Reinforcement Learning, Randomized Reward Shaping, Uncertainty Management, Formal Verification, UPPAAL-SMC}

\input{commands}
\standalonefalse

\setcounter{secnumdepth}{3}
\setcounter{tocdepth}{3}
\raggedbottom

\usepackage{tocloft}
\providecommand{\cftchapdotfill}{\cftdotfill{\cftdotsep}}
\providecommand{\cftsecdotfill}{\cftdotfill{\cftdotsep}}
\providecommand{\cftsubsecdotfill}{\cftdotfill{\cftdotsep}}

\usepackage{fancyhdr}
\pagestyle{fancy}
\fancyhf{}
\fancyhead[L]{\thepage}
\fancyhead[R]{\small\leftmark}
\renewcommand{\chaptermark}[1]{\markboth{\chaptername\ \thechapter.\ #1}{}}
\renewcommand{\sectionmark}[1]{\markright{\thesection.\ #1}}
\let\oldheadrule\headrule
\renewcommand{\headrule}{\oldheadrule}
\fancyhead[R]{\small\nouppercase{\leftmark}}

\begin{document}
\AutoPersianDigits
\setstretch{1.5}

$($inputLines -join "`n`n")

\pagestyle{empty}
{
\renewcommand{\bibname}{مراجع}
\settocbibname{مراجع}
\onehalfspacing
\bibliographystyle{ieeetr-fa}
\bibliography{References,MyReferences}
}

\end{document}
"@
        Set-Content -Path $Target -Value $texTemplate -Encoding UTF8
    }
} elseif ($Target -ne "thesis_full_toc_persian_v3.tex") {
    if ($Target -like "*chapters*" -or $Target -like "*chapter*") {
        $IsSingleChapter = $true
    }
}

if (-not (Test-Path $Target)) {
    Write-Failure "Target LaTeX file not found: $Target"
    exit 1
}

$BaseName = [System.IO.Path]::GetFileNameWithoutExtension($Target)
$PdfFile = "$BaseName.pdf"
$LogFile = "$BaseName.log"

# Check and auto-generate master caches for single chapter builds
if ($IsSingleChapter -and (-not (Test-Path "master_labels.aux") -or -not (Test-Path "master.bbl"))) {
    if (-not (Test-Path "master_labels.aux") -and (Test-Path "thesis_full_toc_persian_v3.aux")) {
        Get-Content "thesis_full_toc_persian_v3.aux" -Encoding UTF8 | Where-Object { $_ -match '^\\(newlabel|bibcite)\{' } | Set-Content "master_labels.aux" -Encoding UTF8
    }
    if (-not (Test-Path "master.bbl") -and (Test-Path "thesis_full_toc_persian_v3.bbl")) {
        Copy-Item "thesis_full_toc_persian_v3.bbl" "master.bbl" -Force
    }
    if (-not (Test-Path "master_labels.aux") -or -not (Test-Path "master.bbl")) {
        Write-Step "Caches" "Generating master_labels.aux and master.bbl from full thesis..."
        Start-Process -FilePath "xelatex" -ArgumentList @("-no-pdf", "-interaction=nonstopmode", "thesis_full_toc_persian_v3.tex") -NoNewWindow -Wait
        Start-Process -FilePath "bibtex" -ArgumentList @("thesis_full_toc_persian_v3") -NoNewWindow -Wait
        Start-Process -FilePath "xelatex" -ArgumentList @("-no-pdf", "-interaction=nonstopmode", "thesis_full_toc_persian_v3.tex") -NoNewWindow -Wait
        if (Test-Path "thesis_full_toc_persian_v3.bbl") {
            Copy-Item "thesis_full_toc_persian_v3.bbl" "master.bbl" -Force
        }
        if (Test-Path "thesis_full_toc_persian_v3.aux") {
            Get-Content "thesis_full_toc_persian_v3.aux" -Encoding UTF8 | Where-Object { $_ -match '^\\(newlabel|bibcite)\{' } | Set-Content "master_labels.aux" -Encoding UTF8
        }
        Remove-Item "thesis_full_toc_persian_v3.aux", "thesis_full_toc_persian_v3.log", "thesis_full_toc_persian_v3.bbl", "thesis_full_toc_persian_v3.blg" -ErrorAction SilentlyContinue
        Write-Success "Generated master caches for cross-chapter reference and citation synchronization."
    }
}

$VerifyScript = Join-Path $ScriptDir ".agents\skills\thesis-latex-typesetting\scripts\verify_build.py"
$CleanScript  = Join-Path $ScriptDir ".agents\skills\thesis-build-cleanup\scripts\clean_build.py"
$SyncBibScript = Join-Path $ScriptDir ".agents\skills\thesis-latex-typesetting\scripts\sync_chapter_bib.py"

# 2. Check prerequisites
$requiredTools = @("xelatex", "bibtex", "python")
foreach ($tool in $requiredTools) {
    if (-not (Get-Command $tool -ErrorAction SilentlyContinue)) {
        Write-Failure "Prerequisite tool '$tool' was not found in PATH."
        exit 1
    }
}

Write-Banner "DOCTORAL DISSERTATION COMPILATION PIPELINE" "Cyan"
Write-Host "Target:       " -ForegroundColor Yellow -NoNewline
Write-Host $(if ($IsMultiChapter) { "$Target (Combined Chapters: $($cleanNums -join ', '))" } elseif ($IsSingleChapter) { "$Target (Single Chapter Mode)" } else { "$Target (All Chapters)" })
Write-Host "Output PDF:   " -ForegroundColor Yellow -NoNewline; Write-Host $PdfFile
Write-Host "Mode:         " -ForegroundColor Yellow -NoNewline; Write-Host $(if ($Fast) { "Fast (Single Pass)" } else { "Full (Multi-Pass + BibTeX)" })
Write-Host "Verification: " -ForegroundColor Yellow -NoNewline
Write-Host $(if ($NoVerify) { "Disabled" } else { if ($IsSingleChapter) { "Active (Single Chapter Mode)" } else { "Active (Full Thesis Baseline)" } })
Write-Host "Auto-Clean:   " -ForegroundColor Yellow -NoNewline; Write-Host $(if ($NoClean) { "Disabled (Keeping aux files)" } else { "Active (Clean intermediate files)" })

$Stopwatch = [System.Diagnostics.Stopwatch]::StartNew()

function Invoke-BuildCommand([string]$Executable, [string[]]$Arguments, [string]$Description) {
    Write-Step $Description "$Executable $($Arguments -join ' ')"
    $process = Start-Process -FilePath $Executable -ArgumentList $Arguments -NoNewWindow -Wait -PassThru
    if ($process.ExitCode -ne 0) {
        Write-Failure "$Description failed with exit code $($process.ExitCode)."
        if (Test-Path $LogFile) {
            Write-Host "`n--- Tail of $LogFile (Last 25 lines) ---" -ForegroundColor DarkYellow
            Get-Content $LogFile -Tail 25
        }
        exit $process.ExitCode
    }
}

# 3. Compilation Stages
try {
    # Pass 1: XeLaTeX
    Invoke-BuildCommand "xelatex" @("-interaction=nonstopmode", $Target) "XeLaTeX Pass 1"

    if (-not $Fast) {
        # Pass 2: BibTeX / Master Bibliography Synchronization
        if (-not $NoBib) {
            if ($IsSingleChapter -and (Test-Path "master.bbl")) {
                Write-Step "Sync Bibliography" "python $SyncBibScript $BaseName"
                $syncProc = Start-Process -FilePath "python" -ArgumentList @($SyncBibScript, $BaseName) -NoNewWindow -Wait -PassThru
                if ($syncProc.ExitCode -ne 0) {
                    Invoke-BuildCommand "bibtex" @($BaseName) "BibTeX Compilation (Fallback)"
                }
            } else {
                Invoke-BuildCommand "bibtex" @($BaseName) "BibTeX Compilation"
            }
        }

        # Pass 3: XeLaTeX (absorb citations and TOC updates)
        Invoke-BuildCommand "xelatex" @("-interaction=nonstopmode", $Target) "XeLaTeX Pass 2 (Citations & References)"

        # Pass 4: XeLaTeX (settle cross-references, TOC, and XePersian bidirectional page counters)
        Invoke-BuildCommand "xelatex" @("-interaction=nonstopmode", $Target) "XeLaTeX Pass 3 (Settling Layout & TOC)"
    }

    # 4. Verification Stage
    $VerificationPassed = $true
    if (-not $NoVerify -and (Test-Path $VerifyScript) -and (Test-Path $LogFile)) {
        Write-Banner "STAGE 2: ZERO-DEFECT LOG VERIFICATION" "Magenta"
        $verifyArgs = @($VerifyScript, $LogFile)
        if ($IsSingleChapter) {
            $verifyArgs += "--single-chapter"
        }
        if ($Fast -or $NoBib) {
            $verifyArgs += "--fast"
        }
        Write-Step "Audit Log" "python $($verifyArgs -join ' ')"
        $verifyProc = Start-Process -FilePath "python" -ArgumentList $verifyArgs -NoNewWindow -Wait -PassThru
        if ($verifyProc.ExitCode -ne 0) {
            $VerificationPassed = $false
            Write-Failure "Build log verification detected issues. Review warnings above."
        } else {
            Write-Success "All zero-defect verification checks passed!"
        }
    }

    # Update master caches if full thesis was compiled
    if (-not $IsSingleChapter) {
        if (Test-Path "$BaseName.bbl") {
            Copy-Item "$BaseName.bbl" "master.bbl" -Force
            Write-Step "Bib Cache" "Updated master.bbl from full thesis bibliography."
        }
        if (Test-Path "$BaseName.aux") {
            Get-Content "$BaseName.aux" -Encoding UTF8 | Where-Object { $_ -match '^\\(newlabel|bibcite)\{' } | Set-Content "master_labels.aux" -Encoding UTF8
            Write-Step "Label Cache" "Updated master_labels.aux for standalone chapter resolution."
        }
    }

    # 5. Cleanup Stage
    if (-not $NoClean -and (Test-Path $CleanScript)) {
        if ($VerificationPassed) {
            Write-Banner "STAGE 3: POST-COMPILATION CLEANUP" "DarkCyan"
            Write-Step "Purge Artifacts" "python $CleanScript"
            Start-Process -FilePath "python" -ArgumentList @($CleanScript) -NoNewWindow -Wait
            Write-Success "Intermediate build artifacts successfully purged."
        } else {
            Write-Host "`n[NOTICE] Skipping cleanup to preserve $LogFile and auxiliary files for inspection." -ForegroundColor Yellow
        }
    }

    $Stopwatch.Stop()
    $Elapsed = $Stopwatch.Elapsed

    # 6. Final Summary
    Write-Banner "COMPILATION SUMMARY" "Green"

    if (Test-Path $PdfFile) {
        $pdfItem = Get-Item $PdfFile
        $sizeMB = [math]::Round($pdfItem.Length / 1MB, 2)
        Write-Host "Generated PDF: " -ForegroundColor Green -NoNewline
        Write-Host "$($pdfItem.FullName) ($sizeMB MB)" -ForegroundColor White
        Write-Host "Build Time:    " -ForegroundColor Green -NoNewline
        Write-Host "$($Elapsed.Minutes)m $($Elapsed.Seconds)s" -ForegroundColor White
        Write-Host "Status:        " -ForegroundColor Green -NoNewline
        if ($VerificationPassed) {
            Write-Host "SUCCESS (Zero Defects)" -ForegroundColor Green
        } else {
            Write-Host "BUILD SUCCEEDED WITH VERIFICATION WARNINGS" -ForegroundColor Yellow
        }

        if ($Open) {
            Write-Host "`nOpening PDF in default viewer..." -ForegroundColor Cyan
            Start-Process $PdfFile
        }
    } else {
        Write-Failure "Expected output PDF was not found: $PdfFile"
        exit 1
    }

    if (-not $VerificationPassed) {
        exit 2
    }
}
catch {
    Write-Failure "An unexpected error occurred: $_"
    exit 1
}
