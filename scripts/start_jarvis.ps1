$ErrorActionPreference = "Stop"

$jarvisData = [Environment]::GetEnvironmentVariable("JARVIS_DATA_DIR", "User")
$ollamaModels = [Environment]::GetEnvironmentVariable("OLLAMA_MODELS", "User")

if ($jarvisData) {
    $env:JARVIS_DATA_DIR = $jarvisData
}

if ($ollamaModels) {
    $env:OLLAMA_MODELS = $ollamaModels
}

.venv\Scripts\python.exe -m jarvis_app

