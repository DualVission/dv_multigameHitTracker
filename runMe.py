from __future__ import annotations

from PySide6 import QtCore, QtGui, QtWidgets #, QMainWindow
from PySide6.QtCore import Qt, QUrl, Signal

import sys
import typing
import random
import os
import json

from pathlib import Path

import dv_MGHT
from dv_MGHT.gui.content_window import ContentWindow
from dv_MGHT.classes.package_classes import DVmghtPackage

def jsonReadGames(path: Path) -> list:
    return [*json.loads(open(path).read())]

def jsonReadPackage(path: Path) -> dict:
    return {**json.loads(open(path).read()), "path": os.fspath(path)}

dv_loz = dv_MGHT.get_package_base_path().joinpath("dv_loz_gr")

myPack = DVmghtPackage(**jsonReadPackage(dv_loz.joinpath("manifest.json")))
myPack.load_games(jsonReadGames(dv_loz.joinpath("games.json")))

# TODO
myApp = QtWidgets.QApplication(sys.argv)
myWindow = ContentWindow(selectedPackage=myPack)
myWindow.show()
sys.exit(myApp.exec())