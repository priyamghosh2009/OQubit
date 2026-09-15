$ErrorActionPreference = "Stop"
Write-Host "=== OQubit Benchmarks ==="
$RepoRoot = Split-Path -Parent $PSScriptRoot
Set-Location $RepoRoot
if (-not (Get-Command python -ErrorAction SilentlyContinue)) {
    Write-Error "Python was not found in PATH."
    exit 1
}
python -m pytest --version *> $null
if ($LASTEXITCODE -ne 0) {
    Write-Error "pytest is not installed."
    Write-Host "Install it with: python -m pip install pytest"
    exit 1
}
Write-Host ""
Write-Host "Running OQubit benchmarks..."
Write-Host ""
python -m pytest benchmarks/ --benchmark-only -v
if ($LASTEXITCODE -ne 0) {
    Write-Error "OQubit benchmarks failed."
    exit $LASTEXITCODE
}
Write-Host ""
Write-Host "OQubit benchmarks completed."
Read-Host " "