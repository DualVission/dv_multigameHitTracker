from __future__ import annotations

from PySide6 import QtCore, QtGui, QtWidgets
from PySide6.QtCore import Qt, QUrl, Signal

from functools import partial
from pathlib import Path
import os

import typing
import random

import dv_MGHT
from dv_MGHT.gui.lib import qt_mght as dv_qt
from dv_MGHT.gui.gen.ui_content_window import Ui_ContentWindow
from dv_MGHT.classes.package_classes import DVmghtPackage, DVmghtGame

# from dv_MGHT import VERSION
VERSION = 1

class ContentWindow(Ui_ContentWindow, QtWidgets.QMainWindow):
    options_changed_signal = Signal()

    def __init__(
        self,
        options: Options,
        selectedPackage: DVmghtPackage | None = None
    ):
        super().__init__()
        self.setupUi(self)

        self._options = options

        self._selected_package: DVmghtPackage | None = None

        self.display_flow_layout = dv_qt.GameFlowLayout(self.gameDisplayWidget, True)
        self.display_flow_layout.setSpacing(15)
        self.display_flow_layout.setAlignment(Qt.AlignHCenter)

        self._display_game_elements: dict[DVmghtGame, dv_qt.GameQtTile] = {}

        if selectedPackage:
            self._load_package(selectedPackage)
        else:
            self.setWindowTitle("dv_MGHT {}".format(VERSION))

        self._current_game: DVmghtGame = None
        self._selected_game: DVmghtGame = None
        self._show_game_options(False)

        # Signals
        self.options_changed_signal.connect(self.on_options_changed)

        # On Click
        self.gameSetCurrent.clicked.connect(partial(self.set_selected_game_current))
        self.gameSetSuccess.clicked.connect(partial(self.set_selected_game_success))
        self.gameSetFailed.clicked.connect(partial(self.set_selected_game_failed))



    # Options
    def on_options_changed(self):
        self.menu_action_display_counter.setChecked(self._options.display_counter)
        self.update_status_display_full()

    # Package
    # Reaction events
    def _load_package(self, selectedPackage: DVmghtPackage):
        if self._selected_package != None:
            for game in self._selected_package.games:
                del self._display_game_elements[game]
        self._selected_package = selectedPackage
        self.setWindowTitle(
            "dv_MGHT {} ({})".format(VERSION, self._selected_package.name)
        )

        for game in self._selected_package.games:
            this_game_tile = dv_qt.GameQtTile(game, self.gameDisplayWidget, self)
            self.display_flow_layout.addWidget(this_game_tile)
            self._display_game_elements[game] = this_game_tile

    # Game
    # Reaction events
    def update_status_full(self):
        self.update_status_display()
    def update_status_display_full(self):
        for _, tile in self._display_game_elements:
            tile.update_status()

    def update_status_at(self, index):
        self.update_status_display_at(index)
    def update_status_display_at(self, index):
        self._display_game_elements[index].update_status()

    def set_selected_game(self, game: DVmghtGame):
        if self._selected_game == game:
            self._selected_game.set_selected(False)
            self.update_status_display_at(self._selected_game)
            self._selected_game = None
            self._show_game_options(False)
            return
        elif self._selected_game != None:
            self._selected_game.set_selected(False)
            self.update_status_display_at(self._selected_game)
        self._selected_game = game
        self._selected_game.set_selected(True)
        self.update_status_display_at(self._selected_game)
        self._show_game_options(True)

    def _show_game_options(self, other: bool | None = None):
        if other == None:
            other = not self.gameSetLabel.isVisible()
        if other:
            game_text = "Set <i>{}</i> to:".format(self._selected_game.name.game)
        else:
            game_text = "Select game"
        self.gameSetLabel.setText(game_text)
        self.gameSetLabel.setVisible(other)
        self.gameSetCurrent.setVisible(other)
        self.gameSetSuccess.setVisible(other)
        self.gameSetFailed.setVisible(other)


    def set_current_game(self, game: DVmghtGame):
        if self._current_game != None:
            self._current_game.set_current(False)
            self.update_status_display_at(self._current_game)
        self._current_game = game
        self._current_game.set_current(True)
        self.update_status_display_at(self._current_game)

    def set_game_failed(self, game: DVmghtGame):
        game.set_failed()
        self.update_status_display_at(game)

    def set_game_success(self, game: DVmghtGame):
        game.set_success()
        self.update_status_display_at(game)

    def set_game_retried(self, game: DVmghtGame):
        game.set_retried()
        self.update_status_display_at(game)

    def set_selected_game_current(self):
        if self._selected_game != None:
            self.set_current_game(self._selected_game)

    def set_selected_game_failed(self):
        if self._selected_game != None:
            self.set_game_failed(self._selected_game)

    def set_selected_game_success(self):
        if self._selected_game != None:
            self.set_game_success(self._selected_game)

    def set_selected_game_retried(self):
        if self._selected_game != None:
            self.set_game_retried(self._selected_game)

    def randomize_order(self):
        random.shuffle(self.display_flow_layout.contents._item_list)
