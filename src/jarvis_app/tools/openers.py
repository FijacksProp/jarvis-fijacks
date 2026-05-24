from __future__ import annotations

import os
import subprocess
from dataclasses import dataclass
from pathlib import Path


class ToolError(RuntimeError):
    """Raised when a local automation tool cannot safely run."""


@dataclass(slots=True)
class ToolResult:
    ok: bool
    message: str


def open_folder(path: str) -> ToolResult:
    folder = Path(path).expanduser().resolve()
    if not folder.exists() or not folder.is_dir():
        raise ToolError(f"Folder does not exist: {folder}")
    _open_path(folder)
    return ToolResult(ok=True, message=f"Opened folder: {folder}")


def open_app(path: str) -> ToolResult:
    app_path = Path(path).expanduser().resolve()
    if not app_path.exists() or not app_path.is_file():
        raise ToolError(f"App does not exist: {app_path}")
    _open_path(app_path)
    return ToolResult(ok=True, message=f"Opened app: {app_path}")


def _open_path(path: Path) -> None:
    if os.name == "nt":
        os.startfile(path)  # type: ignore[attr-defined]
        return
    subprocess.Popen(["open" if os.uname().sysname == "Darwin" else "xdg-open", str(path)])

