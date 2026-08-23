# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'content_window.ui'
##
## Created by: Qt User Interface Compiler version 6.6.3
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QLabel, QListWidget,
    QListWidgetItem, QMainWindow, QMenu, QMenuBar,
    QPushButton, QSizePolicy, QSpacerItem, QStatusBar,
    QVBoxLayout, QWidget)

class Ui_ContentWindow(object):
    def setupUi(self, ContentWindow):
        if not ContentWindow.objectName():
            ContentWindow.setObjectName(u"ContentWindow")
        ContentWindow.resize(820, 640)
        self.centralwidget = QWidget(ContentWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.gameDisplayWidget = QWidget(self.centralwidget)
        self.gameDisplayWidget.setObjectName(u"gameDisplayWidget")
        self.gameDisplayWidget.setContextMenuPolicy(Qt.NoContextMenu)

        self.verticalLayout.addWidget(self.gameDisplayWidget)

        self.gameOptionLayoutWidget = QHBoxLayout()
        self.gameOptionLayoutWidget.setObjectName(u"gameOptionLayoutWidget")
        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gameOptionLayoutWidget.addItem(self.horizontalSpacer_2)

        self.gameSetLabel = QLabel(self.centralwidget)
        self.gameSetLabel.setObjectName(u"gameSetLabel")

        self.gameOptionLayoutWidget.addWidget(self.gameSetLabel)

        self.gameSetCurrent = QPushButton(self.centralwidget)
        self.gameSetCurrent.setObjectName(u"gameSetCurrent")

        self.gameOptionLayoutWidget.addWidget(self.gameSetCurrent)

        self.gameSetSuccess = QPushButton(self.centralwidget)
        self.gameSetSuccess.setObjectName(u"gameSetSuccess")

        self.gameOptionLayoutWidget.addWidget(self.gameSetSuccess)

        self.gameSetFailed = QPushButton(self.centralwidget)
        self.gameSetFailed.setObjectName(u"gameSetFailed")

        self.gameOptionLayoutWidget.addWidget(self.gameSetFailed)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gameOptionLayoutWidget.addItem(self.horizontalSpacer)


        self.verticalLayout.addLayout(self.gameOptionLayoutWidget)

        self.splitDisplayWidget = QListWidget(self.centralwidget)
        self.splitDisplayWidget.setObjectName(u"splitDisplayWidget")

        self.verticalLayout.addWidget(self.splitDisplayWidget)

        ContentWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(ContentWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 820, 22))
        self.menuFile = QMenu(self.menubar)
        self.menuFile.setObjectName(u"menuFile")
        ContentWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(ContentWindow)
        self.statusbar.setObjectName(u"statusbar")
        ContentWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menuFile.menuAction())

        self.retranslateUi(ContentWindow)

        QMetaObject.connectSlotsByName(ContentWindow)
    # setupUi

    def retranslateUi(self, ContentWindow):
        ContentWindow.setWindowTitle(QCoreApplication.translate("ContentWindow", u"MainWindow", None))
        self.gameSetLabel.setText(QCoreApplication.translate("ContentWindow", u"Set Game to", None))
        self.gameSetCurrent.setText(QCoreApplication.translate("ContentWindow", u"Current", None))
        self.gameSetSuccess.setText(QCoreApplication.translate("ContentWindow", u"Successful", None))
        self.gameSetFailed.setText(QCoreApplication.translate("ContentWindow", u"Failed", None))
        self.menuFile.setTitle(QCoreApplication.translate("ContentWindow", u"File", None))
    # retranslateUi

