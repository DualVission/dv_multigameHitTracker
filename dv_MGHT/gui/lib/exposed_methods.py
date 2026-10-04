from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING

from PySide6 import QtCore, QtWidgets
from PySide6.QtWidgets import QWidget
from PySide6.QtCore import QCoreApplication

if TYPE_CHECKING:
    from collections.abc import Callable

def __zip_dict_list(*args, **kwargs) -> dict[str, str | None]:
    output = { k: v for k, v in kwargs.items() }
    for arg in args:
        output[arg] = None
    return output

CONTENT_WINDOW_EXPOSED_METHODS_WITH_HOTKEYS: dict[str, str | None] = {
    "open_state"                  : "Ctrl+O",
    "save_state"                  : "Ctrl+S",
    "select_game_first"           : "Ctrl+Shift+PageUp",
    "select_game_prior"           : "Ctrl+PageUp",
    "select_game_next"            : "Ctrl+PageDown",
    "select_game_last"            : "Ctrl+Shift+PageDown",
    "move_selected_game_far_left" : "Ctrl+Shift+Left",
    "move_selected_game_left"     : "Ctrl+Left",
    "move_selected_game_right"    : "Ctrl+Right",
    "move_selected_game_far_right": "Ctrl+Shift+Right"
}
CONTENT_WINDOW_EXPOSED_METHODS_WITHOUT_HOTKEYS: list[str] = [
    "set_selected_game_current",
    "set_selected_game_failed",
    "set_selected_game_success",
    "set_selected_game_forced",
    "shuffle_all",
    "shuffle_clear_all",
    "clear_all",
    "shuffle_after",
    "shuffle_clear_after",
    "smart_shuffle",
    "smart_clear",
    "smart_shift"
]
CONTENT_WINDOW_EXPOSED_METHODS: dict[str, str | None] = __zip_dict_list(
    *CONTENT_WINDOW_EXPOSED_METHODS_WITHOUT_HOTKEYS,
    **CONTENT_WINDOW_EXPOSED_METHODS_WITH_HOTKEYS
)

ALL_EXPOSED_METHODS_WITH_HOTKEYS: dict[str, str | None] = {
    **CONTENT_WINDOW_EXPOSED_METHODS_WITH_HOTKEYS
}
ALL_EXPOSED_METHODS_WITHOUT_HOTKEYS: list[str] = [
    *CONTENT_WINDOW_EXPOSED_METHODS_WITHOUT_HOTKEYS
]
ALL_EXPOSED_METHODS: dict[str, str | None] = __zip_dict_list(
    *ALL_EXPOSED_METHODS_WITHOUT_HOTKEYS,
    **ALL_EXPOSED_METHODS_WITH_HOTKEYS
)

CONTENT_WINDOW_HOTKEY_LABELS: dict[str, dict[str, str]] = {
    "open_state": {
        "label": QCoreApplication.translate(
            "ContentWindow",
            u"Open Save File"
        ),
        "tooltip": QCoreApplication.translate(
            "ContentWindow",
            u"Open Save File"
        )
    },
    "save_state": {
        "label": QCoreApplication.translate(
            "ContentWindow",
            u"Save File"
        ),
        "tooltip": QCoreApplication.translate(
            "ContentWindow",
            u"Save File"
        )
    },
    "select_game_first": {
        "label": QCoreApplication.translate(
            "ContentWindow",
            u"Select First Game"
        ),
        "tooltip": QCoreApplication.translate(
            "ContentWindow",
            u"Select First Game"
        )
    },
    "select_game_prior": {
        "label": QCoreApplication.translate(
            "ContentWindow",
            u"Select Prior Game"
        ),
        "tooltip": QCoreApplication.translate(
            "ContentWindow",
            u"Select Prior Game"
        )
    },
    "select_game_next": {
        "label": QCoreApplication.translate(
            "ContentWindow",
            u"Select Next Game"
        ),
        "tooltip": QCoreApplication.translate(
            "ContentWindow",
            u"Select Next Game"
        )
    },
    "select_game_last": {
        "label": QCoreApplication.translate(
            "ContentWindow",
            u"Select Game Last"
        ),
        "tooltip": QCoreApplication.translate(
            "ContentWindow",
            u"Select Game Last"
        )
    },
    "move_selected_game_far_left": {
        "label": QCoreApplication.translate(
            "ContentWindow",
            u"\u23ee Move Selected Game to Start"
        ),
        "tooltip": QCoreApplication.translate(
            "ContentWindow",
            u"Move Selected Game to Start"
        )
    },
    "move_selected_game_left": {
        "label": QCoreApplication.translate(
            "ContentWindow",
            u"\u23f4 Move Selected Game Left"
        ),
        "tooltip": QCoreApplication.translate(
            "ContentWindow",
            u"Move Selected Game Left"
        )
    },
    "move_selected_game_right": {
        "label": QCoreApplication.translate(
            "ContentWindow",
            u"\u23f5 Move Selected Game Right"
        ),
        "tooltip": QCoreApplication.translate(
            "ContentWindow",
            u"Move Selected Game Right"
        )
    },
    "move_selected_game_far_right": {
        "label": QCoreApplication.translate(
            "ContentWindow",
            u"\u23ed Move Selected Game to End"
        ),
        "tooltip": QCoreApplication.translate(
            "ContentWindow",
            u"Move Selected Game to End"
        )
    },
    "set_selected_game_current": {
        "label": QCoreApplication.translate(
            "ContentWindow",
            u"Set Selected Game to Current"
        ),
        "tooltip": QCoreApplication.translate(
            "ContentWindow",
            u"Set Selected Game to Current"
        )
    },
    "set_selected_game_success": {
        "label": QCoreApplication.translate(
            "ContentWindow",
            u"Set Selected Game to Successful"
        ),
        "tooltip": QCoreApplication.translate(
            "ContentWindow",
            u"Set Selected Game to Successful"
        )
    },
    "set_selected_game_failed": {
        "label": QCoreApplication.translate(
            "ContentWindow",
            u"Set Selected Game to Failed"
        ),
        "tooltip": QCoreApplication.translate(
            "ContentWindow",
            u"Set Selected Game to Failed"
        )
    },
    "set_selected_game_forced": {
        "label": QCoreApplication.translate(
            "ContentWindow",
            u"Set Selected Game to Force Retry"
        ),
        "tooltip": QCoreApplication.translate(
            "ContentWindow",
            u"Set Selected Game to Force Retry"
        )
    },
    "shuffle_all": {
        "label": QCoreApplication.translate(
            "ContentWindow",
            u"Shuffle All"
        ),
        "tooltip": QCoreApplication.translate(
            "ContentWindow",
            u"Shuffle Game Order"
        )
    },
    "shuffle_clear_all": {
        "label": QCoreApplication.translate(
            "ContentWindow",
            u"Clear Status And Shuffle All"
        ),
        "tooltip": QCoreApplication.translate(
            "ContentWindow",
            u"Shuffle Game Order and Clear Status"
        )
    },
    "clear_all": {
        "label": QCoreApplication.translate(
            "ContentWindow",
            u"Clear All Status"
        ),
        "tooltip": QCoreApplication.translate(
            "ContentWindow",
            u"Clear all Game Statuses"
        )
    },
    "shuffle_after": {
        "label": QCoreApplication.translate(
            "ContentWindow",
            u"Shuffle after Selected"
        ),
        "tooltip": QCoreApplication.translate(
            "ContentWindow",
            u"Shuffle Games after Selected Game"
        )
    },
    "shuffle_clear_after": {
        "label": QCoreApplication.translate(
            "ContentWindow",
            u"Clear Status And Shuffle All"
        ),
        "tooltip": QCoreApplication.translate(
            "ContentWindow",
            u"Shuffle Games and clear Statuses on Games after Selected Game"
        )
    },
    "smart_shuffle": {
        "label": QCoreApplication.translate(
            "ContentWindow",
            u"Shift Success Chain Left"
        ),
        "tooltip": QCoreApplication.translate(
            "ContentWindow",
            u"Shift Successful Games in End Chain First and Shuffle Failed Games"
        )
    },
    "smart_clear": {
        "label": QCoreApplication.translate(
            "ContentWindow",
            u"Clear Status And Shuffle After Selected"
        ),
        "tooltip": QCoreApplication.translate(
            "ContentWindow",
            u"Shift Successful Games in End Chain First and Clear Statuses on Failed Games"
        )
    },
    "smart_shift": {
        "label": QCoreApplication.translate(
            "ContentWindow",
            u"Shift Successful First"
        ),
        "tooltip": QCoreApplication.translate(
            "ContentWindow",
            u"Shift Successful Games in End Chain First"
        )
    }
}

def get_default_hotkeys(*args) -> str | dict[str, str]:
        if len(args) == 1:
            return ALL_EXPOSED_METHODS[args[0]]
        return ALL_EXPOSED_METHODS_WITH_HOTKEYS

class _atlas_item():
    def __init__(self, mirror: object, method_name: str):
        self.method: Callable = getattr(mirror, method_name)
        self.default_hotkey: str | None = get_default_hotkeys(method_name)

    def __str__(self):
        return "_atlas_item ({}: {})".format(self.method, self.default_hotkey)

class __exposedMethods():
    __mirror: QWidget | None = None
    __atlas: dict[str, _atlas_item] = {}

    @property
    def atlas(self) -> dict[str, _atlas_item]:
        return self.__atlas

    @property
    def methods(self) -> dict[str, Callable]:
        return { v: self.atlas[v].method for v in self.atlas.keys()}

    @property
    def default_hotkeys(self) -> dict[str, str]:
        return { v: self.atlas[v].default_hotkey for v in self.atlas.keys()}

class contentWindowExposedMethods(__exposedMethods):
    def __init__(self, mirror: QWidget):
        self.__mirror: QWidget = mirror
        self.__atlas: dict[str, _atlas_item] = {
            v: self._atlas_item(v) for v in CONTENT_WINDOW_EXPOSED_METHODS
        }

    def _atlas_item(self, method_name: str) -> _atlas_item:
        return _atlas_item(self.__mirror, method_name)