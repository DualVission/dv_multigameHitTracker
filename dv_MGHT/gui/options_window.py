from __future__ import annotations

from PySide6 import QtCore, QtGui, QtWidgets
from PySide6.QtCore import Qt, QUrl, Signal, QCoreApplication

from functools import partial
from pathlib import Path

import dv_MGHT
from dv_MGHT.gui.lib import theme
from dv_MGHT.gui.gen.ui_options_window import Ui_optionsWindow # Why is Options lowercase?
from dv_MGHT.interface.options import Options


class OptionsWindow(Ui_optionsWindow, QtWidgets.QDialog):
    _display_counter_text = QCoreApplication.translate(
        "OptionsWindow",
        u"Display Hit Counter on Game Tiles",
        None
    )
    _display_game_bg_img = QCoreApplication.translate(
        "OptionsWindow",
        u"Display Background Images on Game Tiles",
        None
    )

    current_color_window: dict[str, QtWidgets.QColorDialog] = {}

    options_changed_signal = Signal()

    def __init__(
        self,
        parent,
        options: Options,
        advanced_options: bool = False
    ):
        self.parent = parent
        super().__init__(self.parent)
        self.setupUi(self)
        self._options: Options = options

        self.statusForceFailedButton.setVisible(advanced_options)
        self.statusForceFailedLabel.setVisible(advanced_options)

        self.general1DarkModeCheck.clicked.connect(partial(self._on_dark_mode))
        self.general2RandomizeOrderCheck.clicked.connect(partial(self._on_open_shuffle))

        self.statusUpcomingButton.clicked.connect(partial(self._on_status_button, "UPCOMING"))
        self.statusSelectedButton.clicked.connect(partial(self._on_status_button, "SELECTED"))
        self.statusCurrentButton.clicked.connect(partial(self._on_status_button, "CURRENT"))
        self.statusSuccessButton.clicked.connect(partial(self._on_status_button, "SUCCESS"))
        self.statusFailedButton.clicked.connect(partial(self._on_status_button, "FAILED"))
        self.statusForceFailedButton.clicked.connect(partial(self._on_status_button, "FORCE_FAILED"))

        # Signals
        self.options_changed_signal.connect(self.on_options_changed)

        self.on_options_changed()

    # Overrides
    def closeEvent(self,*args, **kwargs):
        super().closeEvent(*args, **kwargs)

    # Options
    def on_options_changed(self):
        self.general1DarkModeCheck.setChecked(self._options.dark_mode)
        theme.set_dark_theme(self._options.dark_mode, self)
        self.general2RandomizeOrderCheck.setChecked(self._options.open_shuffle)
        def tool_style(other:QtGui.QColor):
            statusStyle = """
QToolButton {oc}
    background: #{bg};
    color: {fc}
{cc}"""
            output = {}
            output["oc"] = "{"
            output["cc"] = "}"
            output["bg"] = hex(other.rgba())[4:]
            y = other.lightness() / 255
            if y > 0.2:
                output["fc"] = "black"
            else:
                output["fc"] = "white"
            return statusStyle.format(**output)
        self.statusUpcomingButton.setStyleSheet(
            tool_style(self._options.status_colors.UPCOMING)
        )
        self.statusSelectedButton.setStyleSheet(
            tool_style(self._options.status_colors.SELECTED)
        )
        self.statusCurrentButton.setStyleSheet(
            tool_style(self._options.status_colors.CURRENT)
        )
        self.statusSuccessButton.setStyleSheet(
            tool_style(self._options.status_colors.SUCCESS)
        )
        self.statusFailedButton.setStyleSheet(
            tool_style(self._options.status_colors.FAILED)
        )
        self.statusForceFailedButton.setStyleSheet(
            tool_style(self._options.status_colors.FORCE_FAILED)
        )
    ## Dark Mode
    def _on_dark_mode(self):
        with self._options as options:
            options.dark_mode = self.general1DarkModeCheck.isChecked()
    ## Open Shuffle
    def _on_open_shuffle(self):
        with self._options as options:
            options.open_shuffle = self.general2RandomizeOrderCheck.isChecked()
    ## Status Color
    def _on_status_color(self, status: str, color: QtGui.QColor):
        these_colors = self._options.status_colors
        these_colors._set_field(
            status,
            color
        )
        with self._options as options:
            options.status_colors = these_colors
    ### Launch Window
    def _on_status_button(self, status: str):
        if status not in self.current_color_window:
            self.current_color_window[status] = QtWidgets.QColorDialog()
            self.current_color_window[status].setCurrentColor(
                getattr(self._options.status_colors, status, QtGui.QColor())
            )
        self.current_color_window[status].currentColorChanged.connect(partial(
            self._on_status_color,
            status
        ))
        self.current_color_window[status].colorSelected.connect(partial(
            self._on_status_color,
            status
        ))
        self.current_color_window[status].show()

    def update_status_full(self):
        self.parent.update_status_full()
    def update_game_status_at(self, index):
        self.parent.update_game_status_at(index)