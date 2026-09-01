from __future__ import annotations

from PySide6 import QtGui, QtWidgets
from PySide6.QtCore import Qt

import re
prog = re.compile(r"QStackedWidget\s+\{\s+[A-z0-9;: -]+\s+\}")

_current_dark_theme = None

def set_dark_theme(
    active: bool,
    compact: bool = False,
    *,
    app: QtWidgets.QApplication | QtWidgets.QMainWindow = None
) -> None:
    global _current_dark_theme
    if _current_dark_theme == active:
        return

    if app == None:
        app = QtWidgets.QApplication.instance()
    new_palette = QtGui.QPalette(app.palette())

    import qdarktheme as QDark

    style = QDark.load_stylesheet(theme="dark" if active else "light")
    style += """
    QScrollArea { border: default; }
    """
    if compact:
        style += """
    QGroupBox { padding: 0px; }
    QGroupBox::title { padding-bottom: 12px; }
    QComboBox { padding-right: 10px; }
    QPushButton { min-width: 60px; }
    QToolButton { border: 0.5px solid #32414B; }
        """

    if active:
        new_palette.setColor(QtGui.QPalette.Link, Qt.cyan)
        new_palette.setColor(QtGui.QPalette.LinkVisited, Qt.blue)
        style += """
    QToolTip {
        background-color: black;
        color: white;
        border: black solid 1px;
    }
        """
    else:
        new_palette.setColor(QtGui.QPalette.Link, Qt.blue)
        new_palette.setColor(QtGui.QPalette.LinkVisited, Qt.darkMagenta)

    app.setStyleSheet(style)
    app.setPalette(new_palette)
    _current_dark_theme = active