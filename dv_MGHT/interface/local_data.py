from __future__ import annotations

import dataclasses
from enum import Enum
from typing import TYPE_CHECKING, Any, TypeVar, get_origin

from dv_MGHT.interface import persistent_options
from dv_MGHT.interface.json_tools import json_lib, JSONDecodeError
from dv_MGHT.classes.package_classes import DVmghtPackage, DVmghtGame

if TYPE_CHECKING:
    from collections.abc import Callable
    from pathlib import Path

T = TypeVar("T")

def identity(v: T) -> T:
    return v

@dataclasses.dataclass(frozen=True)
class Serializer:
    encode: Callable[[Any], Any]
    decode: Callable[[Any], Any]

def _return_with_default(value: T | None, default_factory: Callable[[], T]) -> T:
    if value is None:
        return default_factory()
    else:
        return value

class localData(object):
    _data_dir: Path
    _user_dir:  Path
    _on_options_changed: Callable[[], None] | None = None
    _nested_autosave_level: int = 0

    _is_dirty:  bool = False

    _SERIAL_DICT: dict[str, Any]

    def __init__(
        self,
        data_dir: Path,
        user_dir: Path | None = None
    ):
        self._data_dir = data_dir
        self._user_dir  = user_dir or data_dir

    def __getattr__(self,item):
        if isinstance(item, str):
            result = getattr(self, "_{}".format(item), None)
            return result
        raise AttributeError(item)

    def _set_field(self, field_name: str, value) -> None:
        setattr(self, "_" + field_name, value)

    def load_from_disk(self, ignore_decode_errors: bool = True) -> bool:
        result = None
        for content in self._get_data_files():
            try:
                persist_options = json_lib.loads(content)
                result = persistent_options.get_options_from_data(persist_options)
            except (JSONDecodeError) as e:
                if ignore_decode_errors:
                    continue
                else:
                    raise DecodeFailedException("Unable to decode JSON: {}".format(e))
            break

        if result == None:
            return False

        self.load_from_persistent(result, ignore_decode_errors)
        return True

    def _get_data_files(self) -> list[Path]:
        return []

    def load_from_persistent(
        self,
        persistent: dict,
        ignore_decode_errors: bool
    ) -> None:
        for field_name, serializer in self._SERIAL_DICT.items():
            value = persistent.get(field_name, None)
            if value != None:
                try:
                    decoded = serializer.decode(value)
                except Exception as e:
                    if ignore_decode_errors:
                        print("Unable to decode {}".format(field_name))
                        decoded = None
                    else:
                        raise DecodeFailedException(
                            "Unable to decode {}".format(field_name)
                        )
                if decoded != None:
                    self._set_field(field_name, decoded)

    def _serialize_fields(self) -> dict:
        data_to_persist = {}
        for field_name, serializer in self._SERIAL_DICT.items():
            value = getattr(self, "_" + field_name, None)
            if value != None:
                data_to_persist[field_name] = serializer.encode(value)
        return self._serialized_data(data_to_persist)

    def _serialized_data(self, data_to_persist: dict) -> dict:
        return persistent_options.serialized_data_for_options(data_to_persist, "")

    def _save_to_disk(self) -> None:
        self._is_dirty = False
        data_to_persist = self._serialize_fields()
        self._replace_file(data_to_persist)

    def _replace_file(self, data_to_persist: dict) -> None:
        pass

    def _check_editable_and_mark_dirty(self) -> None:
        assert self._nested_autosave_level != 0, self._assert_error()
        self._is_dirty = True

    def _assert_error(self) -> str:
        pass

    def _edit_field(self, field_name: str, new_value) -> None:
        current_value = getattr(self, field_name)
        if current_value != new_value:
            self._check_editable_and_mark_dirty()
            self._set_field(field_name, new_value)

    def __enter__(self):
        self._nested_autosave_level += 1
        return self

    def __exit__(self, exc_type, exc_value, exc_tb):
        if self._nested_autosave_level == 1:
            if self._is_dirty:
                if self._on_options_changed != None:
                    self._on_options_changed()
                self._save_to_disk()
        self._nested_autosave_level -= 1

    # Events
    def _set_on_options_changed(self, value):
        self._on_options_changed = value
    on_options_changed = property(fset=_set_on_options_changed)

    def reset_to_defaults(self) -> None:
        self._check_editable_and_mark_dirty()
        for field_name in self._SERIAL_DICT.keys():
            self._set_field(field_name, None)

    # Properties
    @property
    def data_dir(self) -> Path:
        return self._data_dir

    @property
    def user_dir(self) -> Path:
        return self._user_dir
