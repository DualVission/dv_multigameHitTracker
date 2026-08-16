from __future__ import annotations

from PySide6 import QtCore, QtGui, QtWidgets, QMainWindow
from PySide6.QtCore import Qt, QUrl, Signal

import typing
import random

from dv_MGHT.gui.lib import *
from dv_MGHT.classes.package_classes import DVmghtPackage, DVmghtGame

class GameFlowLayout(flow_layout.FlowLayout):
    def __init__(self, parent=None, center=False):
        super().__init__(parent, center)
        self._games: list[str] = []

    def invalidate(self):
        super.invalidate()
        self._games = [ items.game.name.id for items in self._item_list ]           

    def move_left(self, other: int | str | GameQtTile | DVmghtGame) -> None:
        if isinstance(other, int):
            old_index = other
        elif isinstance(other, GameQtTile):
            old_index = self._item_list.index(other)
        elif isinstance(other, DVmghtGame):
            old_index = self._games.index(other.name.id)
        elif isinstance(other, str) and other in self._games:
            old_index = self._games.index(other)
        else:
            return
        if old_index <= 0:
            print("{} already in far left.".format(other))
            return
        item = self.takeAt(old_index)
        self.insertItem(old_index - 1, item)
        self.invalidate()

    def move_far_left(self, other: int | str | GameQtTile | DVmghtGame) -> None:
        if isinstance(other, int):
            old_index = other
        elif isinstance(other, GameQtTile):
            old_index = self._item_list.index(other)
        elif isinstance(other, DVmghtGame):
            old_index = self._games.index(other.name.id)
        elif isinstance(other, str) and other in self._games:
            old_index = self._games.index(other)
        else:
            return
        if old_index <= 0:
            print("{} already in far left.".format(other))
            return
        item = self.takeAt(old_index)
        self.insertItem(0, item)
        self.invalidate()

    def move_right(self, other: int | str | GameQtTile | DVmghtGame) -> None:
        if isinstance(other, int):
            old_index = other
        elif isinstance(other, GameQtTile):
            old_index = self._item_list.index(other)
        elif isinstance(other, DVmghtGame):
            old_index = self._games.index(other.name.id)
        elif other in self._games:
            old_index = self._games.index(other)
        else:
            return
        if old_index >= (self.count() - 1):
            print("{} already in far right.".format(other))
            return
        item = self.takeAt(old_index)
        self.insertItem(old_index, item) # No need to add 1, as old item to right is now old_index
        self.invalidate()

    def move_far_right(self, other: int | str | GameQtTile | DVmghtGame) -> None:
        if isinstance(other, int):
            old_index = other
        elif isinstance(other, GameQtTile):
            old_index = self._item_list.index(other)
        elif isinstance(other, DVmghtGame):
            old_index = self._games.index(other.name.id)
        elif other in self._games:
            old_index = self._games.index(other)
        else:
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

    def shift_success(self, shuffle_failed: bool = True) -> None:
        current_chain = -1
        for i in range(len(self._item_list)-1,-1,-1):
            this_game = self._item_list[i].game
            if this_game.is_failed and not this_game.is_retry:
                current_chain = i + 1
                break
        if current_chain == len(self._item_list): # when all games failed, halt execution
            if shuffle_failed:
                self.shuffle_order()
            return
        
        header = [ *range(current_chain, len(self._item_list)) ]
        trail = [ *range(current_chain) ]
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


class GameQtTile(QtWidgets.QWidget):

    def __init__(
        self,
        game: DVmghtGame,
        parent,
        window
    ):
        super.__init__(parent)
        self.game = game
        self._parent = parent
        self._window = window

        # Select Game Display and Buttons
        self.tile = clickable_label.ClickableLabel(self)
        self.tile.setToolTip(self._window._options.game_caption(self.game))
        self.tile.setAccessibleName(self.game.accessible_name)
        #--self.tile.setFixedSize(200, 150)
        # Would need to happen before transformed into clickable if set size

        self._hover_effect = QtWidgets.QGraphicsColorizeEffect(self.tile)
        self._hover_effect.setStrength(0.5)
        
        self.tile.clicked.connect(partial(self._window.set_selected_game, self.game))
        self.tile.entered.connect(partial(self._hover_effect.setEnabled, True))
        self.tile.left.connect(partial(self._hover_effect.setEnabled, False))

        # Game Display Text
        self.caption = QtWidgets.QLabel(self.tile)
        self.caption.setText(self.game.name.caption)

        # Retry Indicator
        self.retried_on_fail = QtWidgets.QLabel(self.tile)
        #--self.retried_on_fail.setPixmap(QtGui.QPixmap(os.fspath(image_path)))
        # Uncertain if I want to use a graphic or use webstyle

        # Counter
        self.counter = QtWidgets.QLabel(self.tile)
        self.counter.setStyle("""
            font-size: 5;
            right: 5;
            top: 0;
            """)
        self.counter.setText("A")

        self.update_status()

    def update_status(self):
        self.tile.setStyle(self.game.status.background_style)
        self.retried_on_fail.setVisible(self.game.status.is_retry)
        if self._window._options.display_counter:
            self.counter.setVisible(True)
            self.counter.setText(self.game.personal_best_text)
        else:
            self.counter.setVisible(False)