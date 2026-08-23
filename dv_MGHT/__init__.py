from __future__ import annotations
from pathlib import Path

def get_file_path() -> Path:
    #if is_frozen():
    #    file_dir = Path(getattr(sys, "_MEIPASS"))
    return Path(__file__).parent

def get_asset_path() -> Path:
    return get_file_path().joinpath("asset")

def retry_icon_path() -> Path:
    return get_asset_path().joinpath("retry_icon.png")