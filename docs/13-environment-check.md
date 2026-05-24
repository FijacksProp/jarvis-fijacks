# Environment Check

Date: 2026-05-23

## Current Findings

| Item | Result | Status |
| --- | --- | --- |
| Python | Python 3.14.3 | available |
| Python launcher | Python 3.14.3 only | available |
| Ollama CLI | Installed at `C:\Users\HP\AppData\Local\Programs\Ollama\ollama.exe`; current PowerShell session may need PATH refresh | available |
| Internal storage | C drive has about 10.75GB free | low |
| External storage | E drive has about 423.39GB free | available |
| Virtual environment | `.venv` created with pip 25.3 | available |
| PySide6 | 6.11.1 installed in `.venv` | available |
| pytest | 9.0.3 installed in `.venv` | available |
| pypdf | 6.12.1 installed in `.venv` | available |
| python-docx | 1.2.0 installed in `.venv` | available |
| Ollama model path | `E:\Jarvis\OllamaModels` | configured |
| Jarvis data path | `E:\Jarvis\JarvisData` | configured |
| Winget Ollama package | `Ollama.Ollama` version `0.24.0` | available |
| Installed model | `llama3.2:3b` | available |
| Ollama API | `http://localhost:11434` responds through Jarvis client | available |

## Notes

- Python is installed, but 3.14 is very new. If PySide6 or other packages fail to install, use Python 3.12 or 3.11 for the virtual environment.
- Ollama is not currently available from PowerShell. It may need to be installed, or its install folder may need to be added to PATH.
- Internal storage is tight. Avoid downloading multiple models to the C drive.
- The 500GB external drive is connected as `E:\`.
- Large assistant data and Ollama models should go under `E:\Jarvis`.
- Python could not bootstrap pip until the command was retried with normal filesystem permissions.
- Installing project dependencies required a longer install window because PySide6 downloads are large.
- Tests pass when run with normal filesystem permissions.
- User-level environment variables have been set for `OLLAMA_MODELS` and `JARVIS_DATA_DIR`.
- Existing terminals may need to be restarted before they inherit the new environment variables.
- `winget` can find `Ollama.Ollama` from the community source.
- `llama3.2:3b` is installed and visible to the Jarvis Ollama client.
- Jarvis config default model is `llama3.2:3b`.

## Recommended Next Environment Actions

1. Install or fix Ollama.
2. Run the desktop app with `scripts\start_jarvis.ps1`.
3. Test a few local chat prompts.
4. Add app/folder quick actions.
5. Add file attachment support.

## First Model Recommendation

Start with one small model through Ollama:

- A 3B general instruction model for default chat.
- Add a small coding model later if storage allows.
