from __future__ import annotations

from PySide6 import QtCore, QtGui, QtWidgets
from PySide6.QtCore import Qt, QUrl, Signal, QCoreApplication

from functools import partial
from pathlib import Path

import typing
import random

import dv_MGHT
from dv_MGHT.gui.gen.ui_package_options import Ui_PackageOptionsWindow
from dv_MGHT.classes.package_classes import DVmghtPackage, DVmghtGame, DVmghtSplit
from dv_MGHT.interface.options import (
    Options,
    package_Options,
    game_Options,
    split_Options
)

from dv_MGHT.interface.local_data import localData

class PackageOptionsWindow(Ui_PackageOptionsWindow, QtWidgets.QDialog):
    _disables_sentence = QCoreApplication.translate(
        "PackageOptionsWindow",
        u"{disable} {option}",
        None
    )
    _option_sentence = QCoreApplication.translate(
        "PackageOptionsWindow",
        u"{level} Options",
        None
    )

    _package_disables_text = QCoreApplication.translate(
        "PackageOptionsWindow",
        u"Package Disables",
        None
    )
    _game_disables_text = QCoreApplication.translate(
        "PackageOptionsWindow",
        u"Game Disables",
        None
    )
    _split_disables_text = QCoreApplication.translate(
        "PackageOptionsWindow",
        u"Split Disables",
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

    _split_text = QCoreApplication.translate(
        "PackageOptionsWindow",
        u"Split",
        None
    )
    _subsplit_text = QCoreApplication.translate(
        "PackageOptionsWindow",
        u"Subsplit",
        None
    )

    _caption_text = QCoreApplication.translate(
        "PackageOptionsWindow",
        u"Caption",
        None
    )

    _author_text = QCoreApplication.translate("PackageOptionsWindow", u"Author", None)
    _games_text = QCoreApplication.translate("PackageOptionsWindow", u"Games", None)

    package_options_changed_signal = Signal()

    def __init__(
        self,
        parent,
        package: DVmghtPackage,
        package_options: package_Options
    ):
        super().__init__(parent)
        self.setupUi(self)
        self.package: DVmghtPackage | None = package
        self.package_options: package_Options | None = package_options
        self.game_layouts: dict[str, QtWidgets.QLayout] = {}
        self.game_split_layouts: dict[str, dict[str, QtWidgets.QLayout]] = {}

        if self.package.settings.display_counter:
            self.package1CounterLabel.setEnabled(True)
            self.package1CounterLabel.setToolTip(None)
            self.package1CounterCheck.setEnabled(True)
            self.package1CounterCheck.setToolTip(None)
        else:
            self.package1CounterLabel.setEnabled(False)
            self.package1CounterLabel.setToolTip(self._disables_sentence.format(
                disable = self._package_disables_text,
                option  = self._display_counter_text
            ))
            self.package1CounterCheck.setEnabled(False)
            self.package1CounterCheck.setToolTip(self._disables_sentence.format(
                disable = self._package_disables_text,
                option  = self._display_counter_text
            ))
        if self.package.settings.game_bg_img:
            self.package2GameBgImgLabel.setEnabled(True)
            self.package2GameBgImgLabel.setToolTip(None)
            self.package2GameBgImgCheck.setEnabled(True)
            self.package2GameBgImgCheck.setToolTip(None)
        else:
            self.package2GameBgImgLabel.setEnabled(False)
            self.package2GameBgImgLabel.setToolTip(self._disables_sentence.format(
                disable = self._package_disables_text,
                option  = self._display_game_bg_img
            ))
            self.package2GameBgImgCheck.setEnabled(False)
            self.package2GameBgImgCheck.setToolTip(self._disables_sentence.format(
                disable = self._package_disables_text,
                option  = self._display_game_bg_img
            ))

        self.on_package_options_changed()

        self.setWindowTitle("dv_MGHT {version} ({name} Options)".format(
            version = dv_MGHT.VERSION,
            name = self.package.name
        ))
        for game in self.package.games:
            self.addGameOptions(game, self.package_options.games[game.name.id])

    def addGameOptions(
        self,
        game_object: DVmghtGame,
        game_options: game_Options
    ) -> None:

        game_options_dict = {
            "caption": {
                "type": "str",
                "default": game_object.name.caption,
                "value": game_options.caption,
                "label": self._caption_text
            }
        }

        self.game_layouts[game_object.name.id] = \
            self.addChildOptions(
                game_object,
                game_options,
                game_object.name.game,
                game_options_dict,
                self.gameOptionsLayout,
                2
            )

        if len(game_object.splits) > 0:
            thisLabel = QtWidgets.QLabel(self.mainLayoutWidget)
            thisLabel.setText(self._option_sentence.format(level=self._split_text))
            thisLabel.setProperty(u"sectionHeader", 2)
            self.game_layouts[game_object.name.id].addWidget(thisLabel)

            for split in game_object.splits:
                self.addSplitOptions(
                    split,
                    game_options[split.id],
                    game_object,
                    self.game_layouts[game_object.name.id]
                )


    def addSplitOptions(
        self,
        split_object: DVmghtSplit,
        split_options: split_Options,
        game_object: DVmghtGame,
        parent_layout: QtWidgets.QLayout,
        header_level: int = 3
    ) -> None:

        split_options_dict = {
            "caption": {
                "type": "str",
                "default": split_object.caption,
                "value": split_options.caption,
                "label": self._caption_text
            }
        }

        self.game_split_layouts[game_object.name.id][split_object.id] = \
            self.addChildOptions(
                split_object,
                split_options,
                split_object.caption,
                split_options_dict,
                parent_layout,
                header_level
            )
        
        if len(game_object.splits) > 0:
            thisLabel = QtWidgets.QLabel(self.mainLayoutWidget)
            thisLabel.setText(self._option_sentence.format(level=self._split_text))
            thisLabel.setProperty(u"sectionHeader", header_level)
            self.game_layouts[game_object.name.id].addWidget(thisLabel)

            for split in split_options.splits:
                self.addSplitOptions(
                    split,
                    split_options[split.id],
                    game_object,
                    self.game_split_layouts[game_object.name.id][split_object.id],
                    header_level + 1
                )


    def addChildOptions(
        self,
        child_object: DVmghtGame | DVmghtSplit,
        child_options: game_Options | split_Options,
        child_name: str,
        options_dict: dict[str, dict],
        parent_layout: QtWidgets.QLayout,
        header_level: int
    ) -> QtWidgets.QLayout:
        header_level = max(header_level, 4)

        thisLayout = QtWidgets.QVBoxLayout()

        thisLabel = QtWidgets.QLabel(self.mainLayoutWidget)
        thisLabel.setText(self._option_sentence.format(level=child_name))
        thisLabel.setWordWrap(True)
        thisLabel.setProperty(u"sectionHeader", header_level)
        thisLayout.addWidget(thisLabel)

        thisGrid = QtWidgets.QGridLayout()
        i = 0

        for field_name, properties in options_dict.items():
            match properties["type"]:
                case "str":
                    thisOptionLabel = QtWidgets.QLabel(self.mainLayoutWidget)
                    thisOptionLabel.setText(properties["label"])
                    thisOptionLabel.setWordWrap(True)
                    thisOptionLabel.setAlignment(Qt.AlignVCenter | Qt.AlignRight)
                    thisGrid.addWidget(thisOptionLabel, i, 0)

                    thisOptionInput = QtWidgets.QPlainTextEdit(self.mainLayoutWidget)
                    thisOptionInput.setPlaceholderText(properties["default"])
                    thisOptionInput.setProperty(u"fieldType", properties["type"])
                    thisOptionInput.setProperty(u"fieldName", field_name)
                    thisOptionInput.setProperty(u"fieldDefault", properties["default"])
                    thisOptionInput.setMaximumSize(QtCore.QSize(16777215, 34))
                    if properties["value"] != properties["default"]:
                        thisOptionInput.setPlainText(properties["value"])

                    sizePolicy = QtWidgets.QSizePolicy(
                        QtWidgets.QSizePolicy.Policy.MinimumExpanding,
                        QtWidgets.QSizePolicy.Policy.Fixed
                    )
                    sizePolicy.setHorizontalStretch(0)
                    sizePolicy.setVerticalStretch(0)
                    sizePolicy.setHeightForWidth(
                        thisOptionInput.sizePolicy().hasHeightForWidth()
                    )
                    thisOptionInput.setSizePolicy(sizePolicy)

                    thisOptionLabel.setBuddy(thisOptionInput)

                    thisOptionInput.textChanged.connect(partial(
                        self.updateOption,
                        child_options,
                        thisOptionInput
                    ))

                    thisGrid.addWidget(thisOptionInput, i, 1)

                case "bool":
                    thisOptionLabel = QtWidgets.QLabel(self.mainLayoutWidget)
                    thisOptionLabel.setText(properties["label"])
                    thisOptionLabel.setWordWrap(True)
                    thisOptionLabel.setAlignment(Qt.AlignVCenter | Qt.AlignRight)
                    thisGrid.addWidget(thisOptionLabel, i, 0)

                    thisOptionInput = QtWidgets.QCheckBox(self.mainLayoutWidget)
                    thisOptionInput.setText("")
                    thisOptionInput.setProperty(u"fieldType", properties["type"])
                    thisOptionInput.setProperty(u"fieldName", field_name)
                    thisOptionInput.setProperty(u"fieldDefault", properties["default"])
                    if properties["value"] != properties["default"] \
                    and properties["value"] != None :
                        thisOptionInput.setChecked(properties["value"])

                    sizePolicy = QtWidgets.QSizePolicy(
                        QtWidgets.QSizePolicy.Policy.Fixed,
                        QtWidgets.QSizePolicy.Policy.Fixed
                    )
                    sizePolicy.setHorizontalStretch(0)
                    sizePolicy.setVerticalStretch(0)
                    sizePolicy.setHeightForWidth(
                        thisOptionInput.sizePolicy().hasHeightForWidth()
                    )
                    thisOptionInput.setSizePolicy(sizePolicy)


                    thisOptionInput.clicked.connect(partial(
                        self.updateOption,
                        child_options,
                        thisOptionInput
                    ))

                    thisGrid.addWidget(thisOptionInput, i, 1)

            i += 1

        thisLayout.addLayout(thisGrid)
        parent_layout.addLayout(thisLayout)
        return thisLayout

    def updateOption(
        self,
        options: localData,
        input_widget: QWidget
    ) -> None:
        field_name = input_widget.property(u"fieldName")
        if field_name == None or field_name == "":
            return
        value = None
        match input_widget.property(u"fieldType"):
            case "str":
                value = input_widget.toPlainText()
            case "bool":
                value = input_widget.isChecked()
        if value == "" or value == input_widget.property(u"fieldDefault"):
            value = None
        with options as option:
            option._edit_field(field_name, value)

    def update_status_full(self):
        self.parent.update_status_full()

    def update_status_at(self, index):
        self.parent.update_status_at(index)

    def on_package_options_changed(self):
        if self.package_options == None:
            return
        self.package1CounterCheck.setChecked(self.package_options.display_counter)
        self.package2GameBgImgCheck.setChecked(self.package_options.game_bg_img)
        game_board_size = self.package_options.game_board_size
        self.package3GameBoardSizeXBox.setValue(game_board_size.width())
        self.package3GameBoardSizeYBox.setValue(game_board_size.height())