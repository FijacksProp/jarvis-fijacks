from __future__ import annotations

import json
from dataclasses import dataclass
from typing import Iterable
from urllib.error import URLError
from urllib.request import Request, urlopen


class OllamaError(RuntimeError):
    """Raised when the local Ollama API cannot complete a request."""


@dataclass(slots=True)
class OllamaClient:
    base_url: str = "http://localhost:11434"
    timeout_seconds: int = 30

    def health(self) -> bool:
        try:
            self._request("GET", "/api/tags")
        except OllamaError:
            return False
        return True

    def list_models(self) -> list[str]:
        payload = self._request("GET", "/api/tags")
        return [model["name"] for model in payload.get("models", []) if "name" in model]

    def chat(
        self,
        model: str,
        messages: list[dict[str, str]],
        stream: bool = False,
    ) -> dict | Iterable[dict]:
        body = {
            "model": model,
            "messages": messages,
            "stream": stream,
        }
        if stream:
            return self._stream("POST", "/api/chat", body)
        return self._request("POST", "/api/chat", body)

    def _request(self, method: str, path: str, body: dict | None = None) -> dict:
        url = self._url(path)
        data = None if body is None else json.dumps(body).encode("utf-8")
        headers = {"Content-Type": "application/json"} if body is not None else {}
        request = Request(url, data=data, headers=headers, method=method)

        try:
            with urlopen(request, timeout=self.timeout_seconds) as response:
                return json.loads(response.read().decode("utf-8"))
        except (OSError, URLError, json.JSONDecodeError) as exc:
            raise OllamaError(f"Ollama request failed: {url}") from exc

    def _stream(self, method: str, path: str, body: dict) -> Iterable[dict]:
        url = self._url(path)
        request = Request(
            url,
            data=json.dumps(body).encode("utf-8"),
            headers={"Content-Type": "application/json"},
            method=method,
        )

        try:
            with urlopen(request, timeout=self.timeout_seconds) as response:
                for line in response:
                    if not line:
                        continue
                    yield json.loads(line.decode("utf-8"))
        except (OSError, URLError, json.JSONDecodeError) as exc:
            raise OllamaError(f"Ollama stream failed: {url}") from exc

    def _url(self, path: str) -> str:
        return f"{self.base_url.rstrip('/')}/{path.lstrip('/')}"

