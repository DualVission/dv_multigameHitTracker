from __future__ import annotations
from pathlib import Path

def get_file_path() -> Path:
    #if is_frozen():
    #    file_dir = Path(getattr(sys, "_MEIPASS"))
    return Path(__file__).parent

def get_package_base_path() -> Path:
    return get_file_path().joinpath("packages")

def get_asset_path() -> Path:
    return get_file_path().joinpath("asset")

def retry_img_path() -> Path:
    return get_asset_path().joinpath("img")