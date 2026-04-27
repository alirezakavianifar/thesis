# Local Rendering Setup Guide

This guide will help you set up local rendering of PlantUML diagrams without needing an internet connection.

## Step 1: Install Java

PlantUML requires Java to run. Here are the easiest options:

### Option A: Install Java via Chocolatey (Recommended for Windows)

If you have Chocolatey package manager:

```powershell
# Run PowerShell as Administrator
choco install openjdk
```

### Option B: Download Java Manually

1. Visit [Adoptium (Eclipse Temurin)](https://adoptium.net/) - recommended
   - Or [Oracle JDK](https://www.oracle.com/java/technologies/downloads/)
   - Or [OpenJDK](https://openjdk.org/)

2. Download **Java 17 LTS** or newer (Windows x64 installer)

3. Run the installer and follow the prompts

4. Verify installation:
   ```powershell
   java -version
   ```

### Option C: Use Portable Java (No Installation)

1. Download portable Java from [Adoptium](https://adoptium.net/temurin/releases/?version=17)
   - Choose "JDK" → "Windows" → "x64" → "zip" format

2. Extract to a folder (e.g., `C:\Java\jdk-17`)

3. Add to PATH temporarily or use full path in commands

## Step 2: Download PlantUML

### Option A: Download PlantUML JAR (Recommended)

1. Download `plantuml.jar` from:
   - [PlantUML Releases](https://github.com/plantuml/plantuml/releases)
   - Direct link: [plantuml-1.2024.x.jar](https://github.com/plantuml/plantuml/releases/latest)

2. Save it to your project folder or a dedicated location (e.g., `C:\PlantUML\plantuml.jar`)

### Option B: Use Package Manager

If you have Chocolatey:
```powershell
choco install plantuml
```

## Step 3: Render Your Diagram

### Method 1: Using the Provided Script (Easiest)

After setting up Java and downloading `plantuml.jar`, use the provided `render-local.ps1` script:

```powershell
.\render-local.ps1
```

This will automatically find Java and PlantUML and render your diagram.

### Method 2: Manual Command

If `plantuml.jar` is in your project folder:

```powershell
java -jar plantuml.jar rs-drl-mape-k-diagram.puml
```

If `plantuml.jar` is in a different location:

```powershell
java -jar "C:\PlantUML\plantuml.jar" rs-drl-mape-k-diagram.puml
```

### Method 3: Add PlantUML to PATH (Permanent Solution)

1. Create a folder for PlantUML (e.g., `C:\PlantUML`)

2. Download `plantuml.jar` to that folder

3. Create a batch file `plantuml.bat` in that folder:
   ```batch
   @echo off
   java -jar "%~dp0plantuml.jar" %*
   ```

4. Add `C:\PlantUML` to your system PATH:
   - Press `Win + X` → System → Advanced system settings
   - Click "Environment Variables"
   - Under "System variables", find "Path" and click "Edit"
   - Click "New" and add `C:\PlantUML`
   - Click OK on all dialogs

5. Now you can use:
   ```powershell
   plantuml rs-drl-mape-k-diagram.puml
   ```

## Output Formats

By default, PlantUML generates PNG. To specify a format:

```powershell
# PNG (default)
java -jar plantuml.jar rs-drl-mape-k-diagram.puml

# SVG
java -jar plantuml.jar -tsvg rs-drl-mape-k-diagram.puml

# PDF
java -jar plantuml.jar -tpdf rs-drl-mape-k-diagram.puml

# EPS
java -jar plantuml.jar -teps rs-drl-mape-k-diagram.puml
```

## Troubleshooting

### "java is not recognized"
- Java is not installed or not in PATH
- Verify with: `java -version`
- Reinstall Java or add it to PATH

### "Error: Unable to access jarfile"
- `plantuml.jar` path is incorrect
- Use full path: `java -jar "C:\full\path\to\plantuml.jar" diagram.puml`

### "OutOfMemoryError"
- Increase Java heap size:
  ```powershell
  java -Xmx2048m -jar plantuml.jar rs-drl-mape-k-diagram.puml
  ```

### Diagram not rendering correctly
- Make sure you have the latest `plantuml.jar`
- Check for syntax errors in the `.puml` file

## Quick Setup Script

A PowerShell script (`render-local.ps1`) is provided that will:
1. Check if Java is installed
2. Download PlantUML if needed
3. Render your diagram

Just run:
```powershell
.\render-local.ps1
```

