from __future__ import annotations

from PySide6 import QtCore, QtGui, QtWidgets #, QMainWindow
from PySide6.QtCore import Qt, QUrl, Signal

import sys
# import typing
# import random
import os

from pathlib import Path

import dv_MGHT
from dv_MGHT.interface.options import Options
from dv_MGHT.gui.content_window import ContentWindow
from dv_MGHT.classes.json_tools import package_from_json #, json_lib, package_json_reader
# from dv_MGHT.classes.package_classes import DVmghtPackage

dv_loz = dv_MGHT.get_package_base_path().joinpath("dv_loz_gr")
myPack = package_from_json(dv_loz)

OPTIONS = Options(dv_MGHT.get_local_data_path())

# TODO
myApp = QtWidgets.QApplication(sys.argv)
myWindow = ContentWindow(options=OPTIONS)
myWindow.show()
sys.exit(myApp.exec())