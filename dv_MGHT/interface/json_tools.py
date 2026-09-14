from __future__ import annotations

import jsonc as json
import json as json_og

import os
from enum import Enum, Flag
from typing import TYPE_CHECKING, Any, get_origin
import typing
# import dataclasses

from dv_MGHT.classes.package_classes import DVmghtPackage

if TYPE_CHECKING:
    from collections.abc import Hashable
    from pathlib import Path
   
type JsonPrimitive = str | int | float | bool | None

type JsonObject    = dict[str, "JsonType"]
type JsonType      = JsonObject | list["JsonType"] | JsonPrimitive

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
    def read_path(
        cls,
        path: Path,
        *,
        raise_on_duplicate_keys: bool = True
    ) -> dict | list:
        with path.open("r") as file:
            return json.load(
                file,
                object_pairs_hook=cls._hook_for_raise_on_duplicate_keys
                if raise_on_duplicate_keys else None
            )

    @classmethod
    async def read_path_async(
        cls,
        path: Path,
        *,
        raise_on_duplicate_keys: bool = True
    ) -> dict | list:
        async with aiofiles.open(path) as file:
            return json.loads(
                await f.read(),
                object_pairs_hook=cls._hook_for_raise_on_duplicate_keys
                if raise_on_duplicate_keys else None
            )
   
    @classmethod
    def _encode(value: Any) -> Any:
        if isinstance(value, Enum | Flag):
            return value.value
       
        if isinstance(value, list | tuple):
            return [ cls._encode(v) for v in value]
       
        if isinstance(value, dict):
            return { cls._encode(k): cls._encode(v) for k, v in value.items() }
       
        return value
   
    @classmethod
    def _decode(arg: Any, to_type: type | None = Any) -> Any:
        if arg == None:
            return None
       
        type_origin = get_origin(to_type) or to_type
       
        if inspect.isclass(to_type):
            if issubclass(arg, Enum) or issubclass(arg, Flag):
                return to_type(arg)
       
        elif type_origin is list:
            if type_args:= typing.get_args(to_type):
                value_type = type_args[0]
            else:
                value_type = Any
            return [
                cls._decode(v, value_type) for v in args
            ]
       
        elif type_origin is tuple:
            type_args = typing.get_args(type_)
            if type_args:
                if len(type_args) == 2 and type_args[1] == Ellipsis:
                    value_types = [type_args[0]] * len(arg)
                else:
                    value_types = type_args
            else:
                value_types = [typing.Any] * len(arg)
   
            return tuple(
                cls._decode(v, t, {}, metadata)
                for v, t in zip(arg, value_types, strict=True)
            )
           
        elif type_origin is dict:
            if type_args := typing.get_args(to_type):
                k_type, v_types = type_args
            else:
                k_type, v_types = str, typing.Any
   
            return type_origin(
                (
                    cls._decode(k, k_type, {}, metadata),
                    cls._decode(v, v_types, {}, metadata)
                )
                for k, v in arg.items()
            )
       
        elif hasattr(to_type, "from_json"):
            arg_spec = inspect.getfullargspec(to_type.from_json)
   
            return to_type.from_json(
                arg,
                **{
                    k: v
                    for k, v in extra_args.items()
                    if arg_spec.varkw is not None
                    or k in arg_spec.args
                    or k in arg_spec.kwonlyargs
                },
            )

        return arg

    @classmethod
    def loads(self, content):
        return json.loads(content)
           

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