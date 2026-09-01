from __future__ import annotations

import dataclasses
import jsonc as json
import json as json_og
from enum import Enum
from typing import TYPE_CHECKING, Any, TypeVar

from dv_MGHT.interface import persistent_options
from dv_MGHT.classes.json_tools import json_lib, JSONDecodeError

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

_SERIAL_FIELDS = {
    "dark_mode"      : Serializer(identity, bool),
    "display_counter": Serializer(identity, bool),
    "open_shuffle"   : Serializer(identity, bool)
}

def _return_with_default(value: T | None, default_factory: Callable[[], T]) -> T:
    if value is None:
        return default_factory()
    else:
        return value

class Options:
    _data_dir: Path
    _user_dir:  Path
    _on_options_changed: Callable[[], None] | None = None
    _nested_autosave_level: int = 0

    _is_dirty:  bool = False

    _dark_mode: bool | None = None
    _display_counter: bool | None = None
    _open_shuffle: bool | None = None

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

    def _set_field(self, field_name: str, value):
        setattr(self, "_" + field_name, value)

    def load_from_disk(self, ignore_decode_errors: bool = True) -> bool:
        result = None
        for content in persistent_options.find_config_files(self._data_dir):
            try:
                persist_options = json.loads(content)
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

    def load_from_persistent(
        self,
        persistent: dict,
        ignore_decode_errors: bool
    ):
        for field_name, serializer in _SERIAL_FIELDS.items():
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
        for field_name, serializer in _SERIAL_FIELDS.items():
            value = getattr(self, "_" + field_name, None)
            if value != None:
                data_to_persist[field_name] = serializer.encode(value)
        return persistent_options.serialized_data_for_options(data_to_persist)

    def _save_to_disk(self):
        self._is_dirty = False
        data_to_persist = self._serialize_fields()
        persistent_options.replace_config(self._data_dir, data_to_persist)

    def _check_editable_and_mark_dirty(self):
        assert self._nested_autosave_level != 0, "Attempting to edit an Option, but it wasn't made editable"
        self._is_dirty = True

    def _edit_field(self, field_name: str, new_value):
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

    def reset_to_defaults(self):
        self._check_editable_and_mark_dirty()
        for field_name in _SERIAL_FIELDS.keys():
            self._set_field(field_name, None)

    # Properties
    @property
    def data_dir(self) -> Path:
        return self._data_dir

    @property
    def user_dir(self) -> Path:
        return self._user_dir

    @property
    def dark_mode(self) -> bool:
        return _return_with_default(self._dark_mode, lambda: False)
    @dark_mode.setter
    def dark_mode(self, value: bool) -> None:
        self._edit_field("dark_mode", value)

    @property
    def display_counter(self) -> bool:
        return _return_with_default(self._display_counter, lambda: False)
    @display_counter.setter
    def display_counter(self, value: bool) -> None:
        self._edit_field("display_counter", value)

    @property
    def open_shuffle(self) -> bool:
        return _return_with_default(self._open_shuffle, lambda: False)
    @open_shuffle.setter
    def open_shuffle(self, value: bool) -> None:
        self._edit_field("open_shuffle", value)

    
    