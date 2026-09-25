from pathlib import Path
import sys
import webview

APP_NAME = "MáriX"

def game_path() -> Path:
    # PyInstaller extracts one-file bundles into this temporary folder.
    base = Path(getattr(sys, "_MEIPASS", Path(__file__).resolve().parent))
    path = base / "game.html"
    if not path.exists():
        raise FileNotFoundError(f"A játék fájlja nem található: {path}")
    return path

def main() -> None:
    url = game_path().as_uri()
    webview.create_window(APP_NAME, url, width=1100, height=700, min_size=(800, 540))
    webview.start(gui="edgechromium")

if __name__ == "__main__":
    main()
