from __future__ import annotations

from PySide6 import QtGui, QtWidgets
from PySide6.QtCore import Qt, QUrl, Signal, QCoreApplication

from functools import partial
from pathlib import Path

import typing
import random

import dv_MGHT
from dv_MGHT.interface.options import Options, package_Options
from dv_MGHT.classes.package_classes import DVmghtPackage, DVmghtGame

from dv_MGHT.gui.lib import qt_mght, theme
from dv_MGHT.gui.gen.ui_content_window import Ui_ContentWindow
from dv_MGHT.gui.package_options_window import PackageOptionsWindow

class ContentWindow(Ui_ContentWindow, QtWidgets.QMainWindow):
    packageOptionsWindow: PackageOptionsWindow | None = None
    _disables_sentence = QCoreApplication.translate(
        "PackageOptionsWindow",
        u"{disable} {option}",
        None
    )
    _package_disables_text = QCoreApplication.translate(
        "PackageOptionsWindow",
        u"Package Disables",
        None
    )

    _display_counter_text = QCoreApplication.translate(
        "PackageOptionsWindow",
        u"Display Hit Counter on Game Tiles",
        None
    )
    _display_game_bg_img = QCoreApplication.translate(
        "PackageOptionsWindow",
        u"Display Background Images on Game Tiles",
        None
    )

    _author_text = QCoreApplication.translate("PackageOptionsWindow", u"Author", None)
    _games_text = QCoreApplication.translate("PackageOptionsWindow", u"Games", None)

    options_changed_signal = Signal()
    package_options_changed_signal = Signal()

    def __init__(
        self,
        options: Options | None = None,
        selectedPackage: DVmghtPackage | None = None
    ):
        super().__init__()
        self.setupUi(self)

        self.menuLoadedPackage = QtWidgets.QMenu(self)
        self.actionLoadedPackage.setMenu(self.menuLoadedPackage)

        self._loaded_packages_actions: list[QtGui.QAction] = []
        self._get_packages()

        self.actionPackageOptions.setVisible(False)
        self.actionQuickPackageOptions.setVisible(False)
        self.menuPackageOptions = QtWidgets.QMenu(self)
        self.actionQuickPackageOptions.setMenu(self.menuPackageOptions)
        self.actionDisplayCounters = QtGui.QAction(self)
        self.actionDisplayCounters.setText(self._display_counter_text)
        self.actionDisplayCounters.setCheckable(True)
        self.menuPackageOptions.addAction(self.actionDisplayCounters)
        self.actionDisplayGameBgImg = QtGui.QAction(self)
        self.actionDisplayGameBgImg.setText(self._display_game_bg_img)
        self.actionDisplayGameBgImg.setCheckable(True)
        self.menuPackageOptions.addAction(self.actionDisplayGameBgImg)


        self._selected_package: DVmghtPackage | None = None
        self._selected_package_options: package_Options | None = None
        self._options: Options

        self.gameDisplayWidget.setPalette(QtGui.QPalette())
        self.display_flow_layout = qt_mght.GameFlowLayout(self.gameDisplayWidget, True)
        self.display_flow_layout.setSpacing(15)
        self.display_flow_layout.setAlignment(Qt.AlignHCenter)

        self._display_game_elements: dict[DVmghtGame, qt_mght.GameQtTile] = {}

        if selectedPackage:
            self._load_package(selectedPackage)
        else:
            self.setWindowTitle("dv_MGHT {}".format(dv_MGHT.VERSION))

        self._current_game: DVmghtGame = None
        self._selected_game: DVmghtGame = None
        self._show_game_options(False)
        self.gameStatus3ForcedFailedButton.setVisible(False)

        # On Click

        ## Game Status
        self.gameStatus0CurrentButton.clicked.connect(partial(self.set_selected_game_current))
        self.gameStatus1SuccessButton.clicked.connect(partial(self.set_selected_game_success))
        self.gameStatus2FailedButton.clicked.connect(partial(self.set_selected_game_failed))
        self.gameStatus3ForcedFailedButton.clicked.connect(partial(self.set_selected_game_forced))

        ## Game Position
        self.gamePosition0FarLeftButton.clicked.connect(partial(self.move_selected_game_far_left))
        self.gamePosition1LeftButton.clicked.connect(partial(self.move_selected_game_left))
        self.gamePosition2RightButton.clicked.connect(partial(self.move_selected_game_right))
        self.gamePosition3FarRightButton.clicked.connect(partial(self.move_selected_game_far_right))

        ## Game Order
        self.gameOrderTitleButton.clicked.connect(partial(self._show_order_options))
        ### Shuffle All
        self.gameOrderShuffleAllButton.clicked.connect(partial(self.shuffle_all))
        self.gameOrderShuffleClearAllButton.clicked.connect(partial(self.shuffle_clear_all))
        self.gameOrderClearAllButton.clicked.connect(partial(self.clear_all))
        ### Shuffle After
        self.gameOrderShuffleAfterButton.clicked.connect(partial(self.shuffle_after))
        self.gameOrderShuffleClearAfterButton.clicked.connect(partial(self.shuffle_clear_after))
        self.gameOrderClearAfterButton.clicked.connect(partial(self.clear_after))
        ### Smart Shuffle
        self.gameOrderSmartShuffleButton.clicked.connect(partial(self.smart_shuffle, True, False))
        self.gameOrderSmartShuffleClearButton.clicked.connect(partial(self.smart_shuffle, True, True))

        # Action
        ## File
        ## Options
        self.actionDarkMode.triggered.connect(self._on_menu_action_dark_mode)
        self.actionRandomizeOrderOpenOnStartup.triggered.connect(self._on_menu_open_shuffle)
        ## Package Options
        self.actionPackageOptions.triggered.connect(self._on_menu_action_package_options)
        #### Package Options
        self.actionDisplayCounters.triggered.connect(self._on_menu_action_display_counter)
        self.actionDisplayGameBgImg.triggered.connect(self._on_menu_action_game_bg_img)



        if options == None:
            options = Options(dv_MGHT.get_local_data_path())
        options.on_options_changed = self.options_changed_signal.emit
        options.load_from_disk()
        self._options = options
        self._show_order_options(self._options.open_shuffle)

        # Signals
        self.options_changed_signal.connect(self.on_options_changed)
        self.options_changed_signal.connect(self.on_package_options_changed)


        self.on_options_changed()


    # Options
    ## Config
    def on_options_changed(self):
        self.actionDarkMode.setChecked(self._options.dark_mode)
        self.actionRandomizeOrderOpenOnStartup.setChecked(self._options.open_shuffle)
        theme.set_dark_theme(self._options.dark_mode, self)
        self.update_status_full()
    ### Dark Mode
    def _on_menu_action_dark_mode(self):
        with self._options as options:
            options.dark_mode = self.actionDarkMode.isChecked()
    ### Open Shuffle
    def _on_menu_open_shuffle(self):
        with self._options as options:
            options.open_shuffle = self.actionRandomizeOrderOpenOnStartup.isChecked()

    ## Package
    def on_package_options_changed(self):
        if self._selected_package_options == None:
            return
        self.actionDisplayCounters.setChecked(
            self._selected_package_options.display_counter
        )
        self.actionDisplayGameBgImg.setChecked(
            self._selected_package_options.game_bg_img
        )
        self.update_status_full()
    def _on_menu_action_package_options(self):
        if self._selected_package_options == None:
            return
        self.packageOptionsWindow = PackageOptionsWindow(
            self,
            self._selected_package,
            self._selected_package_options
        )
        self.packageOptionsWindow.show()
    ### Display Counter
    def _on_menu_action_display_counter(self):
        if self._selected_package_options == None:
            return
        with self._selected_package_options as options:
            options.display_counter = self.actionDisplayCounters.isChecked()
    ### Game Background Image
    def _on_menu_action_game_bg_img(self):
        if self._selected_package_options == None:
            return
        with self._selected_package_options as options:
            options.game_bg_img = self.actionDisplayCounters.isChecked()

    # Package
    # Reaction events
    def _load_package(self, selectedPackage: DVmghtPackage):
        if self._selected_package != None:
            for game in self._selected_package.games:
                self.display_flow_layout.takeAt(0)
                del self._display_game_elements[game]
            self._selected_package_options = None
        self._selected_package = selectedPackage
        if self._selected_package.settings.display_counter:
            self.actionDisplayCounters.setEnabled(True)
            self.actionDisplayCounters.setToolTip(None)
        else:
            self.actionDisplayCounters.setEnabled(False)
            self.actionDisplayCounters.setToolTip(self._disables_sentence.format(
                disable = self._package_disables_text,
                option  = self._display_counter_text
            ))
        if self._selected_package.settings.game_bg_img:
            self.actionDisplayGameBgImg.setEnabled(True)
            self.actionDisplayGameBgImg.setToolTip(None)
        else:
            self.actionDisplayGameBgImg.setEnabled(False)
            self.actionDisplayGameBgImg.setToolTip(self._disables_sentence.format(
                disable = self._package_disables_text,
                option  = self._display_game_bg_img
            ))
        self.actionPackageOptions.setVisible(True)
        self.actionQuickPackageOptions.setVisible(True)

        for game in self._selected_package.games:
            this_game_tile = qt_mght.GameQtTile(game, self.gameDisplayWidget, self)
            self.display_flow_layout.addWidget(this_game_tile)
            self._display_game_elements[game] = this_game_tile

        package_options = package_Options(
            self._options.data_dir,
            self._options.user_dir,
            self._selected_package
        )
        
        package_options.on_options_changed = self.options_changed_signal.emit
        package_options.load_from_disk()
        self._selected_package_options = package_options
        self.on_package_options_changed()

        self.setWindowTitle("dv_MGHT {version} ({name})".format(
            version = dv_MGHT.VERSION,
            name = self._selected_package.name
        ))

    # Visual events
    def update_status_full(self):
        self.update_status_display_full()
        self._show_game_options(self._selected_game != None)
    def update_status_display_full(self):
        for _, tile in self._display_game_elements.items():
            tile.update_status()

    def update_game_status_at(self, index):
        self.update_game_status_display_at(index)
    def update_game_status_display_at(self, index):
        self._display_game_elements[index].update_status()

    def _show_game_options(self, other: bool | None = None):
        if other == None:
            other = not self.selectedGameLayoutWidget.isVisible()
        if other:
            game_text = "<i>{}</i>".format(self._selected_game.name.game)
        else:
            game_text = "Select game"
        self.selectedGameLabel.setText(game_text)
        self.selectedGameLayoutWidget.setVisible(other)
        self.gameOrderShuffleAfterButton.setEnabled(other)
        self.gameOrderShuffleClearAfterButton.setEnabled(other)
        self.gameOrderClearAfterButton.setEnabled(other)

    def _show_order_options(self, other: bool | None = None):
        if other == None:
            other = not self.gameOrderOptionsLayoutWidget.isVisible()
        if other:
            self.gameOrderTitleButton.setArrowType(Qt.DownArrow)
        else:
            self.gameOrderTitleButton.setArrowType(Qt.LeftArrow)
        self.gameOrderOptionsLayoutWidget.setVisible(other)
        self.gameOrderLine.setVisible(not other)

    def _get_packages(self):
        for package in dv_MGHT.PACKAGES:
            thisAction = QtGui.QAction(self)
            thisAction.setText(package.name)
            thisToolTip = [
                "{}: ".format(self._author_text) + ", ".join(package.repository.authors),
                "{}: ".format(self._games_text) + ", ".join(package._games)
            ]
            thisAction.setToolTip("\n".join(thisToolTip))
            thisAction.triggered.connect(partial(self._load_package, package))
            self._loaded_packages_actions.append(thisAction)
            self.menuLoadedPackage.addAction(thisAction)

    # Game Statuses

    ## Selected
    def set_selected_game(self, game: DVmghtGame):
        if self._selected_game == game:
            self._selected_game.set_selected(False)
            self.update_game_status_display_at(self._selected_game)
            self._selected_game = None
            self._show_game_options(False)
            return
        elif self._selected_game != None:
            self._selected_game.set_selected(False)
            self.update_game_status_display_at(self._selected_game)
        self._selected_game = game
        self._selected_game.set_selected(True)
        self.update_game_status_display_at(self._selected_game)
        self._show_game_options(True)

    ## Current
    def set_current_game(self, game: DVmghtGame):
        if self._current_game != None:
            self._current_game.set_current(False)
            self.update_game_status_display_at(self._current_game)
        self._current_game = game
        self._current_game.set_current(True)
        self.update_status_display_at(self._current_game)

    def set_selected_game_current(self):
        if self._selected_game != None:
            self.set_current_game(self._selected_game)

    ## Failed
    def set_game_failed(self, game: DVmghtGame):
        game.set_failed()
        self.update_game_status_display_at(game)

    def set_selected_game_failed(self):
        if self._selected_game != None:
            self.set_game_failed(self._selected_game)

    ## Success
    def set_game_success(self, game: DVmghtGame):
        game.set_success()
        self.update_game_status_display_at(game)

    def set_selected_game_success(self):
        if self._selected_game != None:
            self.set_game_success(self._selected_game)

    ## Retried
    def set_game_retried(self, game: DVmghtGame):
        game.set_retried()
        self.update_game_status_display_at(game)

    def set_selected_game_retried(self):
        if self._selected_game != None:
            self.set_game_retried(self._selected_game)

    ## Forced Retried
    def set_game_forced(self, game: DVmghtGame):
        game.set_forced()
        self.update_game_status_display_at(game)

    def set_selected_game_forced(self):
        if self._selected_game != None:
            self.set_game_forced(self._selected_game)

    # Game Order

    ## Shuffle All
    def shuffle_all(self):
        self.display_flow_layout.shuffle_order()
        self.update_status_display_full()

    def shuffle_clear_all(self):
        self.display_flow_layout.shuffle_order()
        self.display_flow_layout.clear_status()
        self.set_selected_game(self._selected_game)
        self.update_status_display_full()

    def clear_all(self):
        self.display_flow_layout.clear_status()
        self.set_selected_game(self._selected_game)
        self.update_status_display_full()

    ## Shuffle After
    def shuffle_after(self):
        if self._selected_game != None:
            self.display_flow_layout.shuffle_order_after(self._selected_game)
        self.update_status_display_full()

    def shuffle_clear_after(self):
        if self._selected_game != None:
            self.display_flow_layout.shuffle_order_after(self._selected_game)
            self.display_flow_layout.clear_status_after(self._selected_game)
        self.update_status_display_full()

    def clear_after(self):
        if self._selected_game != None:
            self.display_flow_layout.clear_status_after(self._selected_game)
        self.update_status_display_full()

    ## Smart Shuffle
    def smart_shuffle(self, shuffle_failed: bool = True, clear_failed: bool = False):
        if self._selected_game != None:
            self.display_flow_layout.shift_success(
                shuffle_failed,
                clear_failed
            )
            if not self._selected_game.status.is_selected:
                self.set_selected_game(self._selected_game)
            self.update_status_display_full()

    ## Move Items

    ### Move Far Left
    def move_game_far_left(self, game: DVmghtGame):
        self.display_flow_layout.move_far_left(game)

    def move_selected_game_far_left(self):
        if self._selected_game != None:
            self.move_game_far_left(self._selected_game)

    ### Move Left
    def move_game_left(self, game: DVmghtGame):
        self.display_flow_layout.move_left(game)

    def move_selected_game_left(self):
        if self._selected_game != None:
            self.move_game_left(self._selected_game)

    ### Move Right
    def move_game_right(self, game: DVmghtGame):
        self.display_flow_layout.move_right(game)

    def move_selected_game_right(self):
        if self._selected_game != None:
            self.move_game_right(self._selected_game)

    ### Move Far Right
    def move_game_far_right(self, game: DVmghtGame):
        self.display_flow_layout.move_far_right(game)

    def move_selected_game_far_right(self):
        if self._selected_game != None:
            self.move_game_far_right(self._selected_game)