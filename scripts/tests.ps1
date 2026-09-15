
# OQubit Test Runner
# Runs the complete OQubit test suite.

$ErrorActionPreference = "Stop"

Write-Host "=== OQubit Tests ==="

# Resolve repository root
$RepoRoot = Split-Path -Parent $PSScriptRoot
Set-Location $RepoRoot

# Check Python
if (-not (Get-Command python -ErrorAction SilentlyContinue)) {
    Write-Error "Python was not found in PATH."
    exit 1
}

# Check pytest
python -m pytest --version *> $null

if ($LASTEXITCODE -ne 0) {
    Write-Error "pytest is not installed."
    Write-Host "Install it with: python -m pip install pytest"
    exit 1
}

Write-Host ""
Write-Host "Running OQubit test suite..."
Write-Host ""

python -m pytest tests/ -v

if ($LASTEXITCODE -ne 0) {
    Write-Error "OQubit tests failed."
    exit $LASTEXITCODE
}

Write-Host ""
Write-Host "All OQubit tests passed."
Read-Host " "