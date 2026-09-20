from __future__ import annotations

from PySide6 import QtCore, QtGui, QtWidgets #, QMainWindow
from PySide6.QtCore import Qt, QUrl, Signal

import sys
import os

from pathlib import Path

import dv_MGHT
from dv_MGHT.interface.options import Options
from dv_MGHT.gui.content_window import ContentWindow
from dv_MGHT.classes.ndi_sender import NDISender

from github import Github, Auth

# TODO
myApp = QtWidgets.QApplication(sys.argv)
myWindow = ContentWindow() # options=OPTIONS)
myWindow.show()
# myNDI = NDISender(myWindow.gameDisplayWidget)
sys.exit(myApp.exec())
