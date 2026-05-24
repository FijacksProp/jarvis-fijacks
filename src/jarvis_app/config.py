from __future__ import annotations

import json
from dataclasses import asdict, dataclass, field
from pathlib import Path

from jarvis_app.paths import default_config_path, default_data_dir, ensure_runtime_dirs


@dataclass(slots=True)
class FavoriteApp:
    name: str
    path: str


@dataclass(slots=True)
class FavoriteFolder:
    name: str
    path: str


@dataclass(slots=True)
class AppConfig:
    ollama_base_url: str = "http://localhost:11434"
    default_model: str = ""
    data_dir: str = field(default_factory=lambda: str(default_data_dir()))
    output_dir: str = field(default_factory=lambda: str(default_data_dir() / "outputs"))
    favorite_apps: list[FavoriteApp] = field(default_factory=list)
    favorite_folders: list[FavoriteFolder] = field(default_factory=list)

    @classmethod
    def load(cls, path: Path | None = None) -> "AppConfig":
        config_path = path or default_config_path()
        ensure_runtime_dirs()
        if not config_path.exists():
            config = cls()
            config.save(config_path)
            return config

        raw = json.loads(config_path.read_text(encoding="utf-8-sig"))
        raw["favorite_apps"] = [FavoriteApp(**item) for item in raw.get("favorite_apps", [])]
        raw["favorite_folders"] = [
            FavoriteFolder(**item) for item in raw.get("favorite_folders", [])
        ]
        return cls(**raw)

    def save(self, path: Path | None = None) -> None:
        config_path = path or default_config_path()
        ensure_runtime_dirs(Path(self.data_dir))
        config_path.parent.mkdir(parents=True, exist_ok=True)
        config_path.write_text(
            json.dumps(asdict(self), indent=2),
            encoding="utf-8",
        )
