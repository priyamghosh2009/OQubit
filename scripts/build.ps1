$ErrorActionPreference = "Stop"
$ProjectRoot = Split-Path $PSScriptRoot -Parent
Set-Location $ProjectRoot
Write-Host "Building wheel file for OQubit Library..."
python setup.py sdist bdist_wheel
Write-Host "Build completed."
Write-Host "Now run the installation.ps1 file to install OQubit Library to your Python environment."
Read-Host " "