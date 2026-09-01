from __future__ import annotations

from PySide6 import QtCore, QtGui, QtWidgets #, QMainWindow
from PySide6.QtWidgets import QSizePolicy
from PySide6.QtCore import Qt, QUrl, Signal, QSize

from functools import partial
from pathlib import Path
import os

import typing
import random

import dv_MGHT
from dv_MGHT.gui.lib import flow_layout, clickable_label
from dv_MGHT.classes.package_classes import DVmghtPackage, DVmghtGame, DVgameStatus

class GameFlowLayout(flow_layout.FlowLayout):
    def __init__(self, parent=None, center=False):
        super().__init__(parent, center)
        self._games: list[str] = []

    def invalidate(self):
        super().invalidate()
        self._games = [ items.widget().game.name.id for items in self._item_list ]

    
    def __get_old_index(self, other: int | str | GameQtTile | DVmghtGame | None) -> int:
        if isinstance(other, int):
            return other
        elif isinstance(other, GameQtTile):
            return self._item_list.index(other)
        elif isinstance(other, DVmghtGame):
            return self._games.index(other.name.id)
        elif isinstance(other, str) and other in self._games:
            return self._games.index(other)
        else:
            return None

    def clear_status(self) -> None:
        for widgetItem in self._item_list:
            widgetItem.widget().game.status.set(DVgameStatus.UPCOMING)
            widgetItem.widget().update()

    def clear_status_after(self, other: int | str | GameQtTile | DVmghtGame) -> None:
        old_index = self.__get_old_index(other)
        if old_index == None:
            return
        if old_index > (self.count() - 2):
            print("{} in far right.".format(other))
            return
        for widgetItem in self._item_list[old_index + 1:]:
            widgetItem.widget().game.status.set(DVgameStatus.UPCOMING)
            widgetItem.widget().update()

    def move_left(self, other: int | str | GameQtTile | DVmghtGame) -> None:
        old_index = self.__get_old_index(other)
        if old_index == None:
            return
        if old_index <= 0:
            print("{} already in far left.".format(other))
            return
        item = self.takeAt(old_index)
        self.insertItem(old_index - 1, item)
        self.invalidate()

    def move_far_left(self, other: int | str | GameQtTile | DVmghtGame) -> None:
        old_index = self.__get_old_index(other)
        if old_index == None:
            return
        if old_index <= 0:
            print("{} already in far left.".format(other))
            return
        item = self.takeAt(old_index)
        self.insertItem(0, item)
        self.invalidate()

    def move_right(self, other: int | str | GameQtTile | DVmghtGame) -> None:
        old_index = self.__get_old_index(other)
        if old_index == None:
            return
        if old_index >= (self.count() - 1):
            print("{} already in far right.".format(other))
            return
        item = self.takeAt(old_index)
        self.insertItem(old_index + 1, item)
        self.invalidate()

    def move_far_right(self, other: int | str | GameQtTile | DVmghtGame) -> None:
        old_index = self.__get_old_index(other)
        if old_index == None:
            return
        if old_index >= (self.count() - 1):
            print("{} already in far right.".format(other))
            return
        item = self.takeAt(old_index)
        self.addItem(item)
        self.invalidate()

    def load_order(self, load_order: list[str]) -> None:
        if len(self._item_list) != len(load_order):
            print("Expected {} items, new order has {}.".format(len(self._item_list), len(load_order)))
            return
        new_order: list[int] = [ self._games.index(item) for item in load_order ]
        self._set_order(new_order)

    def shuffle_order(self) -> None:
        new_order = [ *range(len(self._item_list)) ]
        random.shuffle(new_order)
        self._set_order(new_order)

    def shuffle_order_from(self, index: int) -> None:
        if index >= len(self._item_list):
            print("Index {} greater than list length of {}.".format(index, len(self._item_list)))
            return
        items_to_shuffle = len(self._item_list) - index
        if items_to_shuffle <= 1:
            return
        new_order = [ *range(len(self._item_list)) ]
        trail = new_order[index:]
        if items_to_shuffle != 2:
            # Ensures visual change on engagement
            while trail == new_order[index:]:
                random.shuffle(trail)
        else:
            random.shuffle(trail)
        new_order[index:] = trail
        self._set_order(new_order)

    def shuffle_order_after(self, other: int | str | GameQtTile | DVmghtGame) -> None:
        old_index = self.__get_old_index(other)
        if old_index == None:
            return
        if old_index > (self.count() - 2):
            print("{} in far right.".format(other))
            return
        self.shuffle_order_from(old_index + 1)

    def shift_success(self, shuffle_failed: bool = True, clear_failed: bool = False) -> None:
        current_chain = -1
        for i in range(len(self._item_list)-1,-1,-1):
            this_game = self._item_list[i].widget().game
            if not this_game.status.is_success:
                current_chain = i + 1
                break
            elif this_game.status.is_retry:
                current_chain = i
                break
        if current_chain >= len(self._item_list) or current_chain <= 0: # when all games failed, halt execution
            if clear_failed:
                self.clear_status()
            if shuffle_failed:
                self.shuffle_order()
            return
        header = [ *range(current_chain, len(self._item_list)) ]
        trail = [ *range(current_chain) ]
        if clear_failed:
            for widgetItem in self._item_list[:current_chain]:
                widgetItem.widget().game.status.set(DVgameStatus.UPCOMING)
        if shuffle_failed:
            random.shuffle(trail)
        new_order = header + trail
        self._set_order(new_order)


    def _set_order(self, new_order: list[int]) -> None:
        if len(self._item_list) != len(new_order):
            print("Expected {} items, new order has {}.".format(len(self._item_list), len(new_order)))
            return
        old_order = self._item_list.copy()
        for i in range(len(new_order)):
            self._item_list[i] = old_order[new_order[i]]
        self.invalidate()


class GameQtTile(QtWidgets.QStackedWidget):

    def __init__(
        self,
        game: DVmghtGame,
        parent,
        window
    ):
        super().__init__(parent)
        self.game = game
        self._parent = parent
        self._window = window

        # Select Game Display and Buttons
        self.setToolTip(self.game.name.caption) # self._window._options.game_caption(self.game))
        self.setAccessibleName(self.game.accessible_name)
        self.setSizePolicy(
            QSizePolicy.Policy.MinimumExpanding,
            QSizePolicy.Policy.MinimumExpanding
            )
        self.tile = clickable_label.ClickableLabel(self)
        self.setObjectName("GameQtTile_" + self.game.name.id)
        self.setMinimumSize(46, 46)

        self._hover_effect = QtWidgets.QGraphicsColorizeEffect(self)
        self._hover_effect.setStrength(0.5)
        self._hover_effect.setEnabled(False)
        self.setGraphicsEffect(self._hover_effect)
        
        self.tile.clicked.connect(partial(self._window.set_selected_game, self.game))
        self.tile.entered.connect(partial(self._hover_effect.setEnabled, True))
        self.tile.left.connect(partial(self._hover_effect.setEnabled, False))

        # Retry Indicator
        self.retried_on_fail = QtWidgets.QLabel(self.tile)
        self.retried_on_fail.setPixmap(QtGui.QPixmap(os.fspath(
            dv_MGHT.get_img_path().joinpath("retry_icon.png")
        )))
        self.retried_on_fail.setScaledContents(True)
        self.retried_on_fail.setFixedSize(20, 20)
        self.retried_on_fail.setStyleSheet(""" QLabel { border: 0px hidden; }""")

        # Game Display Text
        self.caption = QtWidgets.QLabel(self.tile)
        self.caption.setText(self.game.name.caption)
        self.caption.resize(self.caption.sizeHint())
        self.caption.setAlignment(QtCore.Qt.AlignHCenter | QtCore.Qt.AlignVCenter)

        # Counter
        self.counter = QtWidgets.QLabel(self.tile)
        self.counter.setStyleSheet(""" QLabel {
            font-size: 5;
            right: 5;
            top: 0;
            border: 0px hidden;
        }""")
        self.counter.setText("A")

        self.update_status()

    def update_status(self):
        self.setStyleSheet(self.game.background_style)
        self.caption.setStyleSheet(self.game.caption_style)
        self.retried_on_fail.setVisible(self.game.status.is_retry)
        self.setAccessibleName(self.game.accessible_name)
        self.caption.resize(self.caption.sizeHint() + QSize(10, 0))
        if self._window._selected_package.settings.display_counter:
            self.counter.setVisible(True)
            self.counter.setText(self.game.personal_best_text)
            self.tile.setMinimumSize(self.caption.sizeHint() + QSize(20, 10))
            self.setMinimumSize(self.caption.sizeHint() + QSize(20, 10))
        else:
            self.counter.setVisible(False)
            self.tile.setMinimumSize(self.caption.sizeHint() + QSize(10, 10))
            self.setMinimumSize(self.caption.sizeHint() + QSize(10, 10))
        self.retried_on_fail.move(
            0,
            self.tile.height()-self.retried_on_fail.height()
        )
