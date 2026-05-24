from jarvis_app.ai.ollama_client import OllamaClient


def test_ollama_url_building():
    client = OllamaClient("http://localhost:11434/")

    assert client._url("/api/tags") == "http://localhost:11434/api/tags"

