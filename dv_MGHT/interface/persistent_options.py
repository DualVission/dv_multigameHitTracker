from __future__ import annotations

from typing import TYPE_CHECKING

from dv_MGHT.interface import migration
from dv_MGHT.interface.json_tools import json_lib

if TYPE_CHECKING:
    from collections.abc import Iterator
    from pathlib import Path

_FIRST_VERSION_IN_SUBFOLDER = 0

def _convert_v1(options: dict) -> dict:
    return options

def _only_new_fields(options: dict) -> dict:
    return options

_CONVERTERS_BY_VERSION = [
    _convert_v1
]

_CURRENT_OPTIONS_FILE_VERSION = migration.get_version(_CONVERTERS_BY_VERSION)

def _try_read_file(file_path: Path) -> str | None:
    try:
        contents = file_path.read_text("utf-8")
        if contents.strip() == "":
            return None
        return contents
    except FileNotFoundError:
        return None

def serialized_data_for_options(
    data_to_persist: dict,
    file_type: str = "",
    **kwargs
) -> dict:
    outputD = {
        "version": _CURRENT_OPTIONS_FILE_VERSION,
        "file"   : file_type,
        **kwargs,
        "options": data_to_persist
    }
    return outputD

def get_options_from_data(persist_options: dict) -> dict:
    options = persist_options.get("options", {})
    options["schema_version"] = persist_options.get("version", 0)
    return migration.apply_migrations(
        options,
        _CONVERTERS_BY_VERSION
    )

# Config

def find_config_files(data_path: Path) -> Iterator[str]:
    for version in range(
        _CURRENT_OPTIONS_FILE_VERSION,
        _FIRST_VERSION_IN_SUBFOLDER -1,
        -1
    ):
        if (
            result := _try_read_file(
                data_path.joinpath(
                    "versioned_config",
                    "{}.json".format(version)
                )
            )
        ) != None:
            yield result
    if (result := _try_read_file(data_path.joinpath("config.json"))) != None:
        yield result

def replace_config_file(data_path: Path, new_data: dict) -> None:
    new_config_path = data_path.joinpath("config_new.json")
    json_lib.write_path(new_config_path, new_data)

    config_path = data_path.joinpath(
        "versioned_config",
        "{}.json".format(_CURRENT_OPTIONS_FILE_VERSION)
    )
    config_path.parent.mkdir(parents=True, exist_ok=True)
    new_config_path.replace(config_path)

# Package

def find_package_setting_files(data_path: Path, package_id: str) -> Iterator[str]:
    for version in range(
        _CURRENT_OPTIONS_FILE_VERSION,
        _FIRST_VERSION_IN_SUBFOLDER -1,
        -1
    ):
        if (
            result := _try_read_file(
                data_path.joinpath(
                    "package_settings",
                    package_id,
                    "{}.json".format(version)
                )
            )
        ) != None:
            yield result
    if (result := _try_read_file(
        data_path.joinpath("{}.json".format(package_id)))
    ) != None:
        yield result

def replace_package_setting_file(data_path: Path, new_data: dict, package_id: str) -> None:
    new_setting_path = data_path.joinpath("setting_new.json")
    json_lib.write_path(new_setting_path, new_data)

    setting_path = data_path.joinpath(
        "package_settings",
        package_id,
        "{}.json".format(_CURRENT_OPTIONS_FILE_VERSION)
    )
    setting_path.parent.mkdir(parents=True, exist_ok=True)
    new_setting_path.replace(setting_path)