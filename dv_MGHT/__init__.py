from __future__ import annotations

from pathlib import Path
import sys

def is_frozen() -> bool:
    return getattr(sys, "frozen", False)

def get_file_path() -> Path:
    if is_frozen():
        return Path(getattr(sys, "_MEIPASS"))
    return Path(__file__).parent

def get_package_base_path() -> Path:
    return get_file_path().joinpath("packages")

def get_asset_path() -> Path:
    return get_file_path().joinpath("asset")

def get_img_path() -> Path:
    return get_asset_path().joinpath("img")

def get_local_data_path() -> Path:
    home = Path.home()

    system_paths = {
        "win32" : home.joinpath("AppData", "Roaming", "DV", "dv_MGHT"),
        "linux" : home.joinpath(".local", "share", "DV", "dv_MGHT"),
        "darwin": home.joinpath("Library", "Application Supprt", "DV", "dv_MGHT")
    }

    if sys.platform not in system_paths:
        raise SystemError("""
Unknown platform detected: {}.\n
dv_MGHT only supports: Windows, Linux, and MacOS.
        """.format(sys.platform))

    return system_paths[sys.platform]