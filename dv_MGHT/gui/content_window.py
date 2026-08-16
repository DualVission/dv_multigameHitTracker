from __future__ import annotations

from PySide6 import QtCore, QtGui, QtWidgets, QMainWindow
from PySide6.QtCore import Qt, QUrl, Signal

import typing
import random

from dv_MGHT.gui.lib import qt_mght as dv_qt
from dv_MGHT.classes.package_classes import DVmghtPackage, DVmghtGame

class ContentWindow(QMainWindow):
    options_changed_signal = Signal()

    def __init__(
        self,
        options: Options,
        selectedPackage: DVmghtPackage
    ):
        super().__init__()
        #self.setupUi(self)

        # from dv_MGHT import VERSION
        VERSION = 1

        self._options = Options

        self._selected_package = selectedPackage
        self.setWindowTitle(
            "dv_MGHT {} ({})".format(VERSION, self._selected_package.name)
        )
        self._display_game_elements: dict[DVmghtGame, dv_qt.GameQtTile] = {}
        self._current_game: DVmghtGame = None
        self._selected_game: DVmghtGame = None

        # Signals
        self.options_changed_signal.connect(self.on_options_changed)

        self.display_flow_layout = dv_qt.GameFlowLayout(REPLACE, True)
        self.display_flow_layout.setSpacing(15)
        self.display_flow_layout.setAlignment(Qt.AlignHCenter)

        for game in self._selected_package.games:
            this_game_tile = dv_qt.GameQtTile(game, REPLACE,self)
            self.display_flow_layout.addWidget(this_game_tile)
            self._display_game_elements[game] = this_game_tile

    # Options
    def on_options_changed(self):
        self.menu_action_display_counter.setChecked(self._options.display_counter)
        self.update_status_display_full()


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
        If self._selected_game != None:
            self._selected_game.status.set_selected(False)
            self.update_status_display_at(self._selected_game)
        self._selected_game = game
        self._selected_game.set_selected(True)
        self.update_status_display_at(self._selected_game)

    def set_current_game(self, game: DVmghtGame):
        If self._current_game != None:
            self._current_game.status.set_current(False)
            self.update_status_display_at(self._current_game)
        self._current_game = game
        self._current_game.set_current(True)
        self.update_status_display_at(self._current_game)

    def set_game_failed(self, game: DVmghtGame):
        game.set_failed()
        self.update_status_display_at(self._selected_game)

    def set_game_success(self, game: DVmghtGame):
        game.set_success()
        self.update_status_display_at(self._selected_game)

    def set_game_retried(self, game: DVmghtGame):
        game.set_retried()
        self.update_status_display_at(self._selected_game)

    def randomize_order(self):
        random.shuffle(self.display_flow_layout.contents._item_list)
