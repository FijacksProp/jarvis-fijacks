# Ollama Install Notes

Prepared paths:

```text
OLLAMA_MODELS=E:\Jarvis\OllamaModels
JARVIS_DATA_DIR=E:\Jarvis\JarvisData
Installer folder=E:\Jarvis\Installers
```

Before pulling any models, confirm:

```powershell
[Environment]::GetEnvironmentVariable("OLLAMA_MODELS", "User")
```

Expected:

```text
E:\Jarvis\OllamaModels
```

Terminal install route:

```powershell
$env:OLLAMA_MODELS = [Environment]::GetEnvironmentVariable("OLLAMA_MODELS", "User")
winget install --id Ollama.Ollama --source winget --accept-source-agreements --accept-package-agreements
```

Detected winget package:

```text
Ollama.Ollama 0.24.0
```

Recommended first model:

```powershell
ollama pull llama3.2:3b
```

Optional smaller first model:

```powershell
ollama pull llama3.2:1b
```

Recommended coding model later:

```powershell
ollama pull qwen2.5-coder:3b
```
