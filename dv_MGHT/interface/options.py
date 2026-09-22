from __future__ import annotations

import dataclasses
from enum import Enum
from typing import TYPE_CHECKING, Any, TypeVar, get_origin

from PySide6 import QtCore, QtGui

from dv_MGHT.interface import persistent_options
from dv_MGHT.interface.json_tools import json_lib, JSONDecodeError
from dv_MGHT.classes.package_classes import DVmghtPackage, DVmghtGame, DVgameStatus
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

class status_color_options():
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

    def __init__(self):
        pass

    def __eq__(self, other):
        if not isinstance(other, status_color_options):
            return False
        return self.to_dict() == other.to_dict()

    def __str__(self):
        return str(self.to_dict())

    def _set_field(self, field_name: str, value) -> None:
        new_color: QtGui.QColor
        if isinstance(value, QtGui.QColor):
            new_color = value
        elif isinstance(value, list) or isinstance(value, tuple):
            new_color = QtGui.QColor(*value)
        elif isinstance(value, str):
            new_color = QtGui.QColor(value)
        elif isinstance(value, None):
            new_color = None
        else:
            raise TypeError("Expected QColor or String. Received {}.".format(type(value)))
        setattr(self, "_" + field_name, new_color)

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

    def get_color_from_status(self, check_status) -> QtGui.QColor:
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

    def get_hex_from_status(self, check_status: DVgameStatus) -> str:
        color = self.get_color_from_status(check_status)
        return hex(color.rgba())[4:]

    @property
    def UPCOMING(self) -> QtGui.QColor:
        return self._return_with_default("UPCOMING")
    @UPCOMING.setter
    def UPCOMING(self, value) -> None:
        self._set_field("UPCOMING", value)

    @property
    def SELECTED(self) -> QtGui.QColor:
        return self._return_with_default("SELECTED")
    @SELECTED.setter
    def SELECTED(self, value) -> None:
        self._set_field("SELECTED", value)

    @property
    def CURRENT(self) -> QtGui.QColor:
        return self._return_with_default("CURRENT")
    @CURRENT.setter
    def CURRENT(self, value) -> None:
        self._set_field("CURRENT", value)

    @property
    def SUCCESS(self) -> QtGui.QColor:
        return self._return_with_default("SUCCESS")
    @SUCCESS.setter
    def SUCCESS(self, value) -> None:
        self._set_field("SUCCESS", value)

    @property
    def FAILED(self) -> QtGui.QColor:
        return self._return_with_default("FAILED")
    @FAILED.setter
    def FAILED(self, value) -> None:
        self._set_field("FAILED", value)

    @property
    def FORCE_FAILED(self) -> QtGui.QColor:
        return self._return_with_default("FORCE_FAILED")
    @FORCE_FAILED.setter
    def FORCE_FAILED(self, value) -> None:
        self._set_field("FORCE_FAILED", value)

class Options(localData):
    _dark_mode: bool | None = None
    _open_shuffle: bool | None = None

    _status_colors: status_color_options | None = None
    _color_updating: bool = True

    def __init__(
        self,
        data_dir: Path,
        user_dir: Path | None = None
    ):
        def status_colors_decoder(persistent: dict) -> status_color_options:
            new_status_colors = status_color_options()
            for field_name, value in persistent.items():
                if value != None:
                    new_status_colors._set_field(field_name, value)
            return new_status_colors

        super().__init__(data_dir, user_dir)
        self._SERIAL_DICT = {
            "dark_mode"    : Serializer(identity, bool),
            "open_shuffle" : Serializer(identity, bool),
            "status_colors": Serializer(
                lambda obj: obj.to_dict(),
                lambda obj: status_colors_decoder(obj)
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
    def status_colors(self) -> status_color_options:
        return _return_with_default(self._status_colors, lambda: status_color_options())
    @status_colors.setter
    def status_colors(self, value: status_color_options) -> None:
        self._edit_field("status_colors", value)
