from __future__ import annotations

import os
from pathlib import Path


APP_NAME = "LocalJarvis"


def project_root() -> Path:
    return Path(__file__).resolve().parents[2]


def default_data_dir() -> Path:
    configured = os.environ.get("JARVIS_DATA_DIR")
    if configured:
        return Path(configured).expanduser().resolve()
    return project_root() / "data"


def default_config_path() -> Path:
    return default_data_dir() / "config.json"


def ensure_runtime_dirs(data_dir: Path | None = None) -> None:
    base = data_dir or default_data_dir()
    for child in (
        base,
        base / "outputs",
        base / "outputs" / "notes",
        base / "outputs" / "reports",
        base / "attachments",
        base / "indexes",
        base / "backups",
        project_root() / "logs",
    ):
        child.mkdir(parents=True, exist_ok=True)

