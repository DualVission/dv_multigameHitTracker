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

def set_version(for_release: bool = False):
    from github import Github
    from datetime import date
    g = Github()
    repo = g.get_repo("DualVission/dv_multigameHitTracker")
    releases = [ release.name for release in repo.get_releases() if release.name != "" ]
    g.close()
    today = date.today()
    _version = today.strftime("%Y-%m")
    _v_tupple = (*today.timetuple()[0:3], 0)
    if _version in releases:
        _version = today.strftime("%Y-%m-%d")
        if _version in releases:
            if releases[0][-1].isalpha():
                letter = chr(ord(releases[0][-1]) + 1)
                _version += letter
                _v_tupple = (*today.timetuple()[0:3], letter)
            else:
                _version += "a"
                _v_tupple = (*today.timetuple()[0:3], "a")
        else:
            _v_tupple = (*today.timetuple()[0:3], 0)
    if not for_release:
        _version += "\u03b1"
        _v_tuple = (*today.timetuple()[0:3], "unfrozen")
    with open(get_file_path().joinpath("version.py"), "wt", encoding="utf-8") as file:
        file.write("""
from __future__ import annotations

VERSION: str                       = \"{version}\"
VERSION_TUPLE: tuple[int|str, ...] = {tup}
""".format(version=_version, tup=_v_tuple))

try:
    from .version import VERSION, VERSION_TUPLE
except:
    set_version()
    from .version import VERSION, VERSION_TUPLE

from .packages import PACKAGES, PACKAGE_BY_ID
