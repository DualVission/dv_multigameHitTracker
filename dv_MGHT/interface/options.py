from __future__ import annotations

import dataclasses
from enum import Enum
from typing import TYPE_CHECKING, Any, TypeVar, get_origin

from PySide6 import QtCore, QtGui

import dv_MGHT.gui.lib.exposed_methods as exposed_m

from dv_MGHT.interface import persistent_options
from dv_MGHT.interface.json_tools import json_lib, JSONDecodeError
from dv_MGHT.interface.package_classes import DVmghtPackage, DVmghtGame, DVmghtStatus
from dv_MGHT.interface.local_data import (
    _return_with_default,
    Serializer,
    localData,
    identity
)

if TYPE_CHECKING:
    from collections.abc import Callable
    from pathlib import Path

class split_Options(localData):
    _caption: str | None = None
    _splits: dict[str, split_Options] = {}

    def __init__(
        self,
        data_dir: Path,
        user_dir: Path | None = None,
        split: DVmghtGame | None = None,
        parent_options: game_Options | split_Options | None = None
    ):
        super().__init__(data_dir, user_dir)
        self.split = split
        self._parent_options = parent_options

        def split_decoder(split: str, raw_data: dict) -> split_option:
            split_option = split_Options(
                self.data_dir,
                self.user_dir,
                self.split.split_from_id[split],
                self
            )
            split_option.load_from_persistent(raw_data, True)
            return split_option

        self._SERIAL_DICT = {
            "caption": Serializer(identity, str),
            "splits"  : Serializer(
                lambda obj: { k: v._serialize_fields() for k, v in obj.items()},
                lambda obj: { k: split_decoder(k, v) for k, v in obj.items() }
            )
        }
        
        for child_split in self.split.splits:
            self._splits[child_split.id] = split_Options(data_dir, user_dir, child_split, self)

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
        return data_to_persist

    def _save_to_disk(self) -> None:
        self._is_dirty = False
        data_to_persist = self._serialize_fields()
        self._parent_options._save_to_disk()

    # Properties

    @property
    def caption(self) -> str:
        return _return_with_default(self._caption, lambda: self.split.caption)
    @caption.setter
    def caption(self, value: str) -> None:
        self._edit_field("caption", value)

    @property
    def splits(self) -> dict[str, split_Options]:
        return self._splits #_return_with_default(self._splits, lambda: {})
    @splits.setter
    def splits(self, value: dict[str, split_Options]) -> None:
        self._edit_field("splits", value)

class game_Options(localData):
    _caption: str | None = None
    _splits: dict[str, split_Options] = {}

    def __init__(
        self,
        data_dir: Path,
        user_dir: Path | None = None,
        game: DVmghtGame | None = None,
        package_options: package_Options | None = None
    ):
        super().__init__(data_dir, user_dir)
        self.game = game
        self._package_options = package_options

        def split_decoder(split: str, raw_data: dict) -> split_option:
            split_option = split_Options(
                self.data_dir,
                self.user_dir,
                self.game.split_from_id[split],
                self
            )
            split_option.load_from_persistent(raw_data, True)
            return split_option

        self._SERIAL_DICT = {
            "caption": Serializer(identity, str),
            "splits"  : Serializer(
                lambda obj: { k: v._serialize_fields() for k, v in obj.items()},
                lambda obj: { k: split_decoder(k, v) for k, v in obj.items() }
            )
        }

        for split in self.game.splits:
            self._splits[split.id] = split_Options(data_dir, user_dir, split, self)

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
        return data_to_persist

    def _save_to_disk(self) -> None:
        self._is_dirty = False
        data_to_persist = self._serialize_fields()
        self._package_options._save_to_disk()

    # Properties

    @property
    def caption(self) -> str:
        return _return_with_default(self._caption, lambda: self.game.name.caption)
    @caption.setter
    def caption(self, value: str) -> None:
        self._edit_field("caption", value)

    @property
    def splits(self) -> dict[str, split_Options]:
        return self._splits #_return_with_default(self._splits, lambda: {})
    @splits.setter
    def splits(self, value: dict[str, split_Options]) -> None:
        self._edit_field("splits", value)

class package_Options(localData):
    _display_counter: bool | None = None
    _game_bg_img: bool | None = None
    _games: dict[str, game_Options] = {}

    _game_board_size: QtCore.QSize | None = None
    _game_board_scale: float | None = None

    _package: DVmghtPackage | None = None

    def __init__(
        self,
        data_dir: Path,
        user_dir: Path | None = None,
        package: DVmghtPackage | None = None
    ):
        super().__init__(data_dir, user_dir)
        self._package = package

        def game_decoder(game: str, raw_data: dict) -> game_Options:
            game_option = game_Options(
                self.data_dir,
                self.user_dir,
                self._package.game_from_id[game],
                self
            )
            game_option.load_from_persistent(raw_data, True)
            return game_option

        self._SERIAL_DICT = {
            "display_counter" : Serializer(identity, bool),
            "game_bg_img"     : Serializer(identity, bool),
            "game_board_size" : Serializer(
                lambda obj: obj.toTuple(),
                lambda obj: QtCore.QSize(*obj)
            ),
            "game_board_scale": Serializer(identity, float),
            "games"           : Serializer(
                lambda obj: { k: v._serialize_fields() for k, v in obj.items()},
                lambda obj: { k: game_decoder(k, v) for k, v in obj.items() }
            )
        }
        
        for game in self.package.games:
            self._games[game.name.id] = game_Options(data_dir, user_dir, game, self)
        

    def _get_data_files(self) -> list[Path]:
        if self.package == None:
            return
        return persistent_options.find_package_setting_files(
            self._data_dir,
            self._package.id
        )

    def _serialized_data(self, data_to_persist: dict) -> dict:
        return persistent_options.serialized_data_for_options(
            data_to_persist,
            "package_options",
            package={
                "package_id": self._package.id,
                "version": self._package.version
            }
        )

    def _replace_file(self, data_to_persist: dict) -> None:
        if self.package == None:
            return
        persistent_options.replace_package_setting_file(
            self._data_dir,
            data_to_persist,
            self._package.id
        )

    def _assert_error(self) -> str:
        return "Attempting to edit a package option, but it wasn't made editable"


    # Properties

    @property
    def display_counter(self) -> bool:
        return _return_with_default(self._display_counter, lambda: False)
    @display_counter.setter
    def display_counter(self, value: bool) -> None:
        self._edit_field("display_counter", value)

    @property
    def game_bg_img(self) -> bool:
        return _return_with_default(self._game_bg_img, lambda: False)
    @game_bg_img.setter
    def game_bg_img(self, value: bool) -> None:
        self._edit_field("game_bg_img", value)

    @property
    def game_bg_img(self) -> bool:
        return _return_with_default(self._game_bg_img, lambda: False)
    @game_bg_img.setter
    def game_bg_img(self, value: bool) -> None:
        self._edit_field("game_bg_img", value)

    @property
    def game_board_size(self) -> QtCore.QSize:
        return _return_with_default(self._game_board_size, lambda: QtCore.QSize(512, 64))
    @game_board_size.setter
    def game_board_size(self, value: QtCore.QSize) -> None:
        self._edit_field("game_board_size", value)

    @property
    def game_board_scale(self) -> float:
        return _return_with_default(self._game_board_scale, lambda: False)
    @game_board_scale.setter
    def game_board_scale(self, value: float) -> None:
        self._edit_field("game_board_scale", value)

    @property
    def games(self) -> dict[str, game_Options]:
        return self._games #_return_with_default(self._games, lambda: {})
    @games.setter
    def games(self, value: dict[str, game_Options]) -> None:
        self._edit_field("games", value)

class statusColorOptions():
    _UPCOMING:     QtGui.QColor | None = None
    _SELECTED:     QtGui.QColor | None = None
    _CURRENT:      QtGui.QColor | None = None
    _SUCCESS:      QtGui.QColor | None = None
    _FAILED:       QtGui.QColor | None = None
    _FORCE_FAILED: QtGui.QColor | None = None

    __items = [
        "UPCOMING",
        "SELECTED",
        "CURRENT",
        "SUCCESS",
        "FAILED",
        "FORCE_FAILED"
    ]

    _d_UPCOMING     = QtGui.QColor("#ccc")
    _d_SELECTED     = QtGui.QColor("#0ff")
    _d_CURRENT      = QtGui.QColor("#fff")
    _d_SUCCESS      = QtGui.QColor("#1f1")
    _d_FAILED       = QtGui.QColor("#d21")
    _d_FORCE_FAILED = QtGui.QColor("#f0f")

    def __init__(self, parent):
        self.__parent = parent

    @classmethod
    def from_dict(self, parent, persistent: dict) -> statusColorOptions:
        new_status_colors = statusColorOptions(parent)
        for field_name, value in persistent.items():
            if value != None:
                new_status_colors._set_field(field_name, value)
        return new_status_colors

    def __eq__(self, other):
        if not isinstance(other, statusColorOptions):
            return False
        return self.to_dict() == other.to_dict()

    def __str__(self):
        return str(self.to_dict())

    def _edit_field(self, field_name: str, new_value) -> None:
        current_value = getattr(self, field_name)
        if current_value != new_value:
            self.__parent._check_editable_and_mark_dirty()
            self._set_field(field_name, new_value)

    def _set_field(self, field_name: str, new_value) -> None:
        new_color: QtGui.QColor | None
        if isinstance(new_value, QtGui.QColor):
            new_color = new_value
        elif isinstance(new_value, list) or isinstance(new_value, tuple):
            new_color = QtGui.QColor(*new_value)
        elif isinstance(new_value, str):
            new_color = QtGui.QColor(new_value)
        elif value == None:
            new_color = None
        else:
            raise TypeError("Expected QColor or String. Received {}.".format(type(value)))
        if new_color != getattr(self, "_d_" + field_name):
            setattr(self, "_" + field_name, new_color)
        else:
            setattr(self, "_" + field_name, None)

    def to_dict(self) -> dict[str, list[int]] | None:
        data_to_persist = {}
        for field_name in self.__items:
            value = getattr(self, "_" + field_name, None)
            if value != None:
                data_to_persist[field_name] = value.toTuple()[:3]
        if len(data_to_persist.keys()) <= 0:
            return None
        return data_to_persist

    def _return_with_default(self, field_name: str) -> QtGui.QColor:
        value = getattr(self, "_" + field_name, None)
        if value != None:
            return value
        return getattr(self, "_d_" + field_name)

    def get_color_from_status(self, check_status: DVmghtStatus) -> QtGui.QColor:
        if check_status.name == "SELECTED":
            return self.SELECTED
        if check_status.name == "CURRENT":
            return self.CURRENT
        if check_status.name == "SUCCESS":
            return self.SUCCESS
        if check_status.name == "FAILED":
            return self.FAILED
        if check_status.name == "FORCE_FAILED":
            return self.FORCE_FAILED
        return self.UPCOMING

    def get_hex_from_status(self, check_status: DVmghtStatus) -> str:
        color = self.get_color_from_status(check_status)
        return hex(color.rgba())[4:]

    def is_default(self, check_status: DVmghtStatus) -> bool:
        value = getattr(self, "_" + check_status.name, None)
        return value == None

    @property
    def UPCOMING(self) -> QtGui.QColor:
        return self._return_with_default("UPCOMING")
    @UPCOMING.setter
    def UPCOMING(self, value) -> None:
        self._edit_field("UPCOMING", value)

    @property
    def SELECTED(self) -> QtGui.QColor:
        return self._return_with_default("SELECTED")
    @SELECTED.setter
    def SELECTED(self, value) -> None:
        self._edit_field("SELECTED", value)

    @property
    def CURRENT(self) -> QtGui.QColor:
        return self._return_with_default("CURRENT")
    @CURRENT.setter
    def CURRENT(self, value) -> None:
        self._edit_field("CURRENT", value)

    @property
    def SUCCESS(self) -> QtGui.QColor:
        return self._return_with_default("SUCCESS")
    @SUCCESS.setter
    def SUCCESS(self, value) -> None:
        self._edit_field("SUCCESS", value)

    @property
    def FAILED(self) -> QtGui.QColor:
        return self._return_with_default("FAILED")
    @FAILED.setter
    def FAILED(self, value) -> None:
        self._edit_field("FAILED", value)

    @property
    def FORCE_FAILED(self) -> QtGui.QColor:
        return self._return_with_default("FORCE_FAILED")
    @FORCE_FAILED.setter
    def FORCE_FAILED(self, value) -> None:
        self._edit_field("FORCE_FAILED", value)

class hotkeyOptions():
    _exposed_methods: dict[ str, list[ QtGui.QKeySequence ] ] = {
        k: [] for k in exposed_m.ALL_EXPOSED_METHODS.keys()
    }
    _d_exposed_methods: dict[str, QtGui.QKeySequence | None] = {}

    def __init__(self, parent):
        for field_name, value in exposed_m.ALL_EXPOSED_METHODS.items():
            self._d_exposed_methods[field_name] = self._convert_value(value)
        self.__parent = parent

    @classmethod
    def from_dict(self, parent, persistent: dict) -> hotkeyOptions:
        new_hotkey_options = hotkeyOptions(parent)
        for field_name, value in persistent.items():
            if value != None:
                new_hotkey_options._set_field(field_name, value)
        return new_hotkey_options

    def __eq__(self, other):
        if not isinstance(other, hotkeyOptions):
            return False
        return self.to_dict() == other.to_dict()

    def __len__(self):
        output: int = 0
        for value in self._exposed_methods.values():
            output += 1 if len(value) >= 0 else 0
        return output

    def __getitem__(self, field_name: str) -> list[QtGui.QKeySequence]:
        return self._return_with_default(field_name)

    def __setitem__(self, field_name: str, new_value: list | None):
        self._edit_field(field_name, new_value)

    def __delitem__(self, field_name: str):
        self._edit_field(field_name, None)

    def __contains__(self, field_name: str):
        return field_name in self.exposed_methods.keys()

    def keys(self):
        return self._exposed_methods.keys()

    def values(self):
        return self._exposed_methods.values()

    def items(self):
        return self._exposed_methods.items()

    def __str__(self):
        return str(self.to_dict())

    def to_dict(self) -> dict[str, list[str]] | None:
        data_to_persist = {}
        for field_name, value in self._exposed_methods.items():
            if len(value) <= 0:
                data_to_persist[field_name] = [v.toString() for v in value]
        if len(data_to_persist.keys()) <= 0:
            return None
        return data_to_persist

    def _edit_field(self, field_name: str, new_value: list | None) -> None:
        current_value = self._exposed_methods[field_name]
        if current_value != new_value:
            self.__parent._check_editable_and_mark_dirty()
            self._set_field(field_name, new_value)

    def _set_field(
        field_name: str,
        new_value: list,
        raise_on_error: bool = False
    ) -> None:
        self._exposed_methods[field_name] = self._convert_value(new_value, raise_on_error)

    @classmethod
    def _convert_value(
        cls,
        new_value: list | str,
        raise_on_error: bool = False
    ) -> list[QtGui.QKeySequence] | None:
        if new_value == None:
            return []
        elif isinstance(new_value, str):
            new_value: list[str] = [ new_value ]
        new_sequence: list[QtGui.QKeySequence] = []
        new_input: QtGui.QKeySequence | None
        for raw_input in new_value:
            new_input = None
            if isinstance(raw_input, str):
                new_input = QtGui.QKeySequence.fromString(raw_input)
            elif isinstance(raw_input, QtGui.QKeySequence):
                new_input = raw_input
            elif raw_input == None:
                continue
            else:
                err_txt = "Expected QKeySequence or String. Received {}.".format(
                    type(raw_input)
                )
                if raise_on_error:
                    raise TypeError(err_txt)
                else:
                    print(err_txt + " Error bypassed.")
                    continue
            if new_input != None:
                new_sequence.append(new_input)
        
        return new_sequence

    def _return_with_default(self, field_name: str | None) -> list[QtGui.QKeySequence]:
        value = self._exposed_methods[field_name]
        if value != None:
            return value
        return self._d_exposed_methods[field_name]

    def get_text(self, field_name: str) -> str:
        if len(self._exposed_methods[field_name]) <= 0:
            pass

class Options(localData):
    _dark_mode: bool | None = None
    _open_shuffle: bool | None = None

    _status_colors: statusColorOptions

    _global_hotkeys: bool | None = None
    _hotkeys: hotkeyOptions

    def __init__(
        self,
        data_dir: Path,
        user_dir: Path | None = None
    ):
        super().__init__(data_dir, user_dir)
        self._status_colors = statusColorOptions(self)
        self._hotkeys = hotkeyOptions(self)
        self._SERIAL_DICT = {
            "dark_mode"     : Serializer(identity, bool),
            "open_shuffle"  : Serializer(identity, bool),
            "status_colors" : Serializer(
                lambda obj: obj.to_dict(),
                lambda obj: statusColorOptions.from_dict(self, obj)
            ),
            "global_hotkeys": Serializer(identity, bool),
            "hotkeys": Serializer(
                lambda obj: obj.to_dict(),
                lambda obj: hotkeyOptions.from_dict(self, obj)
            )
        }

    # Overrides

    def _get_data_files(self) -> list[Path]:
        return persistent_options.find_config_files(self._data_dir)

    def _serialized_data(self, data_to_persist: dict) -> dict:
        return persistent_options.serialized_data_for_options(data_to_persist, "config")

    def _replace_file(self, data_to_persist: dict) -> None:
        persistent_options.replace_config_file(self._data_dir, data_to_persist)

    def _assert_error(self) -> str:
        return "Attempting to edit an application option, but it wasn't made editable"


    # Properties

    @property
    def dark_mode(self) -> bool:
        return _return_with_default(self._dark_mode, lambda: True)
    @dark_mode.setter
    def dark_mode(self, value: bool) -> None:
        self._edit_field("dark_mode", value)

    @property
    def open_shuffle(self) -> bool:
        return _return_with_default(self._open_shuffle, lambda: False)
    @open_shuffle.setter
    def open_shuffle(self, value: bool) -> None:
        self._edit_field("open_shuffle", value)

    @property
    def status_colors(self) -> statusColorOptions:
        if self._nested_autosave_level > 0:
            self._is_dirty = True
        return _return_with_default(
            self._status_colors,
            lambda: statusColorOptions(self)
        )
    @status_colors.setter
    def status_colors(self, value: statusColorOptions) -> None:
        self._edit_field("status_colors", value)

    @property
    def global_hotkeys(self) -> bool:
        return _return_with_default(self._global_hotkeys, lambda: False)
    @global_hotkeys.setter
    def global_hotkeys(self, value: bool) -> None:
        self._edit_field("global_hotkeys", value)

    @property
    def hotkeys(self) -> hotkeyOptions:
        if self._nested_autosave_level > 0:
            self._is_dirty = True
        return _return_with_default(
            self._hotkeys,
            lambda: hotkeyOptions(self)
        )
    @hotkeys.setter
    def hotkeys(self, value: hotkeyOptions) -> None:
        self._edit_field("hotkeys", value)
