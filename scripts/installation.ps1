$wheel = Get-ChildItem -Path "..\dist\*.whl" |
    Sort-Object LastWriteTime -Descending |
    Select-Object -First 1
Write-Host "Installing $($wheel.Name)..."
python -m pip install $wheel.FullName --force-reinstall
Write-Host "Installation Completed: "
Read-Host " "