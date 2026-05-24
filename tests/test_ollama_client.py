from jarvis_app.ai.ollama_client import OllamaClient
from jarvis_app.ai.ollama_client import OllamaError


def test_ollama_url_building():
    client = OllamaClient("http://localhost:11434/")

    assert client._url("/api/tags") == "http://localhost:11434/api/tags"


def test_ollama_error_includes_underlying_detail(monkeypatch):
    def fake_urlopen(*_args, **_kwargs):
        raise TimeoutError("timed out")

    monkeypatch.setattr("jarvis_app.ai.ollama_client.urlopen", fake_urlopen)
    client = OllamaClient("http://localhost:11434")

    try:
        client.list_models()
    except OllamaError as exc:
        assert "TimeoutError" in str(exc)
        assert "timed out" in str(exc)
    else:
        raise AssertionError("Expected OllamaError")
