$ErrorActionPreference = "Stop"

Write-Host "== Drives =="
[System.IO.DriveInfo]::GetDrives() |
    Where-Object { $_.IsReady } |
    Select-Object Name, DriveType, VolumeLabel,
        @{Name = "FreeGB"; Expression = { [math]::Round($_.AvailableFreeSpace / 1GB, 2) } },
        @{Name = "TotalGB"; Expression = { [math]::Round($_.TotalSize / 1GB, 2) } } |
    Format-Table -AutoSize

Write-Host "`n== Environment =="
$ollamaModels = [Environment]::GetEnvironmentVariable("OLLAMA_MODELS", "User")
$jarvisData = [Environment]::GetEnvironmentVariable("JARVIS_DATA_DIR", "User")
Write-Host "OLLAMA_MODELS=$ollamaModels"
Write-Host "JARVIS_DATA_DIR=$jarvisData"

Write-Host "`n== Tools =="
if (Get-Command ollama -ErrorAction SilentlyContinue) {
    ollama --version
} elseif (Test-Path "$env:LOCALAPPDATA\Programs\Ollama\ollama.exe") {
    & "$env:LOCALAPPDATA\Programs\Ollama\ollama.exe" --version
} else {
    Write-Host "ollama: not found"
}

if (Test-Path ".venv\Scripts\python.exe") {
    .venv\Scripts\python.exe --version
} else {
    python --version
}

Write-Host "`n== Jarvis Data =="
if ($jarvisData -and (Test-Path $jarvisData)) {
    Get-ChildItem -Force $jarvisData | Select-Object Mode, Length, LastWriteTime, Name | Format-Table -AutoSize
} else {
    Write-Host "Jarvis data folder is missing or not configured."
}
