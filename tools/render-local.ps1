# PowerShell script to render PlantUML diagram locally
# Requires Java to be installed

param(
    [string]$InputFile = "rs-drl-mape-k-diagram.puml",
    [string]$Format = "png",
    [int]$DPI = 300
)

# Colors for output
$ErrorColor = "Red"
$SuccessColor = "Green"
$InfoColor = "Cyan"

Write-Host ""
Write-Host "=== PlantUML Local Renderer ===" -ForegroundColor $InfoColor
Write-Host ""

# Check if Java is installed
Write-Host "Checking for Java..." -ForegroundColor $InfoColor
try {
    $javaCheck = Get-Command java -ErrorAction Stop
    $javaVersion = java -version 2>&1 | Select-Object -First 1
    Write-Host "[OK] Java found: $javaVersion" -ForegroundColor $SuccessColor
} catch {
    Write-Host "[ERROR] Java is not installed or not in PATH" -ForegroundColor $ErrorColor
    Write-Host ""
    Write-Host "Please install Java first:" -ForegroundColor $ErrorColor
    Write-Host "  1. Visit https://adoptium.net/" -ForegroundColor Yellow
    Write-Host "  2. Download Java 17 LTS or newer" -ForegroundColor Yellow
    Write-Host "  3. Install and restart your terminal" -ForegroundColor Yellow
    Write-Host ""
    Write-Host "Or use Chocolatey (as Administrator):" -ForegroundColor Yellow
    Write-Host "  choco install openjdk" -ForegroundColor Yellow
    exit 1
}

# Check if input file exists
if (-not (Test-Path $InputFile)) {
    Write-Host "[ERROR] Input file not found: $InputFile" -ForegroundColor $ErrorColor
    exit 1
}

# Look for plantuml.jar in common locations
$plantumlJar = $null
$useCommand = $false
$scriptDir = Split-Path -Parent $MyInvocation.MyCommand.Path
$possibleLocations = @(
    "$scriptDir\plantuml.jar",  # Same directory as script
    ".\plantuml.jar",            # Current directory
    ".\tools\plantuml.jar",      # Tools subdirectory (if run from main dir)
    "$env:USERPROFILE\PlantUML\plantuml.jar",
    "C:\PlantUML\plantuml.jar",
    "$env:ProgramFiles\PlantUML\plantuml.jar"
)

Write-Host "Looking for plantuml.jar..." -ForegroundColor $InfoColor
foreach ($location in $possibleLocations) {
    if (Test-Path $location) {
        $plantumlJar = $location
        Write-Host "[OK] Found: $plantumlJar" -ForegroundColor $SuccessColor
        break
    }
}

# If not found, check if plantuml command is available
if (-not $plantumlJar) {
    try {
        $null = Get-Command plantuml -ErrorAction Stop
        $plantumlCheck = plantuml -version 2>&1
        if ($LASTEXITCODE -eq 0) {
            Write-Host "[OK] PlantUML command found in PATH" -ForegroundColor $SuccessColor
            $useCommand = $true
        }
    } catch {
        $useCommand = $false
    }
}

# If still not found, offer to download
if (-not $plantumlJar -and -not $useCommand) {
    Write-Host "[ERROR] plantuml.jar not found" -ForegroundColor $ErrorColor
    Write-Host ""
    Write-Host "Would you like to download it automatically? (Y/N)" -ForegroundColor Yellow
    $response = Read-Host
    
    if ($response -eq "Y" -or $response -eq "y") {
        Write-Host "Downloading plantuml.jar..." -ForegroundColor $InfoColor
        
        # Get latest release URL
        $latestUrl = "https://github.com/plantuml/plantuml/releases/latest/download/plantuml.jar"
        $downloadPath = ".\plantuml.jar"
        
        try {
            Invoke-WebRequest -Uri $latestUrl -OutFile $downloadPath -UseBasicParsing
            if (Test-Path $downloadPath) {
                $plantumlJar = $downloadPath
                Write-Host "[OK] Downloaded: $downloadPath" -ForegroundColor $SuccessColor
            }
        } catch {
            Write-Host "[ERROR] Download failed. Please download manually:" -ForegroundColor $ErrorColor
            Write-Host "  https://github.com/plantuml/plantuml/releases/latest" -ForegroundColor Yellow
            exit 1
        }
    } else {
        Write-Host ""
        Write-Host "Please download plantuml.jar manually:" -ForegroundColor $ErrorColor
        Write-Host "  1. Visit https://github.com/plantuml/plantuml/releases/latest" -ForegroundColor Yellow
        Write-Host "  2. Download plantuml.jar" -ForegroundColor Yellow
        Write-Host "  3. Place it in this directory or add to PATH" -ForegroundColor Yellow
        exit 1
    }
}

# Determine output file name
$baseName = [System.IO.Path]::GetFileNameWithoutExtension($InputFile)
$outputFile = "$baseName.$Format"

Write-Host ""
Write-Host "Rendering diagram..." -ForegroundColor $InfoColor
Write-Host "  Input:  $InputFile" -ForegroundColor Gray
Write-Host "  Output: $outputFile" -ForegroundColor Gray
Write-Host "  Format: $Format" -ForegroundColor Gray
Write-Host "  DPI:    $DPI" -ForegroundColor Gray
Write-Host ""

# Render the diagram
try {
    if ($useCommand) {
        # Use plantuml command if available
        $formatFlag = switch ($Format) {
            "svg" { "-tsvg" }
            "pdf" { "-tpdf" }
            "eps" { "-teps" }
            default { "" }
        }
        
        $dpiFlag = if ($Format -eq "png") { "-SDPI=$DPI" } else { "" }
        
        # Use explicit border to prevent clipping
        $borderFlag = "-Sborder=50"
        if ($formatFlag -and $dpiFlag) {
            & plantuml $formatFlag $dpiFlag $borderFlag $InputFile
        } elseif ($formatFlag) {
            & plantuml $formatFlag $borderFlag $InputFile
        } elseif ($dpiFlag) {
            & plantuml $dpiFlag $borderFlag $InputFile
        } else {
            & plantuml $borderFlag $InputFile
        }
    } elseif ($plantumlJar) {
        # Use java -jar
        $formatFlag = switch ($Format) {
            "svg" { "-tsvg" }
            "pdf" { "-tpdf" }
            "eps" { "-teps" }
            default { "" }
        }
        
        $dpiFlag = if ($Format -eq "png") { "-SDPI=$DPI" } else { "" }
        
        # Use explicit border and no autofit to prevent clipping
        # -Sborder sets border size, -Sautofit=false prevents auto-cropping
        $borderFlag = "-Sborder=50"
        if ($formatFlag -and $dpiFlag) {
            & java -jar $plantumlJar $formatFlag $dpiFlag $borderFlag $InputFile
        } elseif ($formatFlag) {
            & java -jar $plantumlJar $formatFlag $borderFlag $InputFile
        } elseif ($dpiFlag) {
            & java -jar $plantumlJar $dpiFlag $borderFlag $InputFile
        } else {
            & java -jar $plantumlJar $borderFlag $InputFile
        }
    } else {
        Write-Host "[ERROR] Cannot render: PlantUML not found" -ForegroundColor $ErrorColor
        exit 1
    }
    
    if ($LASTEXITCODE -eq 0 -and (Test-Path $outputFile)) {
        Write-Host "[OK] Successfully rendered: $outputFile" -ForegroundColor $SuccessColor
        Write-Host ""
        
        # Try to open the file
        $openFile = Read-Host "Open the rendered file? (Y/N)"
        if ($openFile -eq "Y" -or $openFile -eq "y") {
            Start-Process $outputFile
        }
    } else {
        Write-Host "[ERROR] Rendering failed. Check for errors above." -ForegroundColor $ErrorColor
        exit 1
    }
} catch {
    Write-Host "[ERROR] Error during rendering: $_" -ForegroundColor $ErrorColor
    exit 1
}

Write-Host ""
Write-Host "Done!" -ForegroundColor $SuccessColor
