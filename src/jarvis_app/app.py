from __future__ import annotations

import sys


def main(argv: list[str] | None = None) -> int:
    """Run the desktop app."""
    _ = argv or sys.argv[1:]

    try:
        from jarvis_app.ui.main_window import run
    except ImportError as exc:
        missing = exc.name or "a required dependency"
        print(
            "Jarvis desktop UI could not start because "
            f"{missing!r} is not installed.\n"
            "Install dependencies with: python -m pip install -r requirements.txt"
        )
        return 1

    return run()

