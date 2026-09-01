from __future__ import annotations

import os
import jsonc as json
import json as json_og
from typing import TYPE_CHECKING, Any

from dv_MGHT.classes.package_classes import DVmghtPackage

if TYPE_CHECKING:
    from collections.abc import Hashable
    from pathlib import Path

JSONDecodeError = json_og.decoder.JSONDecodeError

class json_lib():
    @classmethod
    def _hook_for_raise_on_duplicate_keys(
        cls,
        ordered_pairs: list[tuple[Hashable, Any]]
    ) -> dict:
        dict_out = {}
        for key, val in ordered_pairs:
            if key in dict_out:
                raise ValueError("Duplicate key: {}".format(key))
            else:
                dict_out[key] = val
        return dict_out

    @classmethod
    def write_path(cls, path: Path, data: Any) -> None:
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(json.dumps(data, indent=4, separators=(",", ": ")))

    @classmethod
    def read_path(cls, path: Path, *, raise_on_duplicate_keys: bool = True) -> dict | list:
        with path.open("r") as file:
            return json.load(
                file,
                object_pairs_hook=cls._hook_for_raise_on_duplicate_keys if raise_on_duplicate_keys else None
            )

    @classmethod
    async def read_path_async(cls, path: Path, *, raise_on_duplicate_keys: bool = True) -> dict | list:
        async with aiofiles.open(path) as file:
            return json.loads(
                await f.read(),
                object_pairs_hook=cls._hook_for_raise_on_duplicate_keys if raise_on_duplicate_keys else None
            )

def package_json_reader(path: Path) -> dict:
    # print(os.fspath(path.parent()))
    outputD = {
        **json_lib.read_path(path.joinpath("manifest.json")),
        "path": os.fspath(path)
    }
    if path.joinpath("games.json").exists():
        outputD["games"] = json_lib.read_path(path.joinpath("games.json"))
    if path.joinpath("settings.json").exists():
        outputD["settings"] = json_lib.read_path(path.joinpath("settings.json"))
    return outputD
def package_from_json(path: Path) -> DVmghtPackage:
    return DVmghtPackage(**package_json_reader(path))