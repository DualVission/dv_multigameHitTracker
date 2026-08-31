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
    QToolButton, QVBoxLayout, QWidget)

class Ui_ContentWindow(object):
    def setupUi(self, ContentWindow):
        if not ContentWindow.objectName():
            ContentWindow.setObjectName(u"ContentWindow")
        ContentWindow.resize(820, 640)
        ContentWindow.setStyleSheet(u"QToolButton {\n"
"	font-family: \"Segoe UI Symbol\";\n"
"}")
        self.centralwidget = QWidget(ContentWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.gameDisplayWidget = QWidget(self.centralwidget)
        self.gameDisplayWidget.setObjectName(u"gameDisplayWidget")
        self.gameDisplayWidget.setContextMenuPolicy(Qt.NoContextMenu)

        self.verticalLayout.addWidget(self.gameDisplayWidget)

        self.selectedGameLayoutWidget = QWidget(self.centralwidget)
        self.selectedGameLayoutWidget.setObjectName(u"selectedGameLayoutWidget")
        self.selectedGameLayout = QVBoxLayout(self.selectedGameLayoutWidget)
        self.selectedGameLayout.setObjectName(u"selectedGameLayout")
        self.selectedGameLabel = QLabel(self.selectedGameLayoutWidget)
        self.selectedGameLabel.setObjectName(u"selectedGameLabel")
        self.selectedGameLabel.setAlignment(Qt.AlignCenter)

        self.selectedGameLayout.addWidget(self.selectedGameLabel)

        self.gameButtonsLayout = QHBoxLayout()
        self.gameButtonsLayout.setObjectName(u"gameButtonsLayout")
        self.preSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gameButtonsLayout.addItem(self.preSpacer)

        self.gameStatusLayout = QHBoxLayout()
        self.gameStatusLayout.setObjectName(u"gameStatusLayout")
        self.gameStatusLabel = QLabel(self.selectedGameLayoutWidget)
        self.gameStatusLabel.setObjectName(u"gameStatusLabel")

        self.gameStatusLayout.addWidget(self.gameStatusLabel)

        self.gameStatus0CurrentButton = QPushButton(self.selectedGameLayoutWidget)
        self.gameStatus0CurrentButton.setObjectName(u"gameStatus0CurrentButton")

        self.gameStatusLayout.addWidget(self.gameStatus0CurrentButton)

        self.gameStatus1SuccessButton = QPushButton(self.selectedGameLayoutWidget)
        self.gameStatus1SuccessButton.setObjectName(u"gameStatus1SuccessButton")

        self.gameStatusLayout.addWidget(self.gameStatus1SuccessButton)

        self.gameStatus2FailedButton = QPushButton(self.selectedGameLayoutWidget)
        self.gameStatus2FailedButton.setObjectName(u"gameStatus2FailedButton")

        self.gameStatusLayout.addWidget(self.gameStatus2FailedButton)

        self.gameStatus3ForcedFailedButton = QPushButton(self.selectedGameLayoutWidget)
        self.gameStatus3ForcedFailedButton.setObjectName(u"gameStatus3ForcedFailedButton")

        self.gameStatusLayout.addWidget(self.gameStatus3ForcedFailedButton)


        self.gameButtonsLayout.addLayout(self.gameStatusLayout)

        self.midSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Minimum)

        self.gameButtonsLayout.addItem(self.midSpacer)

        self.gamePositionLayout = QHBoxLayout()
        self.gamePositionLayout.setObjectName(u"gamePositionLayout")
        self.gamePositionLayout.setContentsMargins(5, -1, 5, -1)
        self.gamePositionLabel = QLabel(self.selectedGameLayoutWidget)
        self.gamePositionLabel.setObjectName(u"gamePositionLabel")

        self.gamePositionLayout.addWidget(self.gamePositionLabel)

        self.gamePosition0FarLeftButton = QToolButton(self.selectedGameLayoutWidget)
        self.gamePosition0FarLeftButton.setObjectName(u"gamePosition0FarLeftButton")
        self.gamePosition0FarLeftButton.setToolButtonStyle(Qt.ToolButtonIconOnly)
        self.gamePosition0FarLeftButton.setArrowType(Qt.NoArrow)

        self.gamePositionLayout.addWidget(self.gamePosition0FarLeftButton)

        self.gamePosition1LeftButton = QToolButton(self.selectedGameLayoutWidget)
        self.gamePosition1LeftButton.setObjectName(u"gamePosition1LeftButton")

        self.gamePositionLayout.addWidget(self.gamePosition1LeftButton)

        self.gamePosition2RightButton = QToolButton(self.selectedGameLayoutWidget)
        self.gamePosition2RightButton.setObjectName(u"gamePosition2RightButton")

        self.gamePositionLayout.addWidget(self.gamePosition2RightButton)

        self.gamePosition3FarRightButton = QToolButton(self.selectedGameLayoutWidget)
        self.gamePosition3FarRightButton.setObjectName(u"gamePosition3FarRightButton")

        self.gamePositionLayout.addWidget(self.gamePosition3FarRightButton)


        self.gameButtonsLayout.addLayout(self.gamePositionLayout)

        self.postSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gameButtonsLayout.addItem(self.postSpacer)


        self.selectedGameLayout.addLayout(self.gameButtonsLayout)


        self.verticalLayout.addWidget(self.selectedGameLayoutWidget)

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
        self.selectedGameLabel.setText(QCoreApplication.translate("ContentWindow", u"TextLabel", None))
        self.gameStatusLabel.setText(QCoreApplication.translate("ContentWindow", u"Set to", None))
        self.gameStatus0CurrentButton.setText(QCoreApplication.translate("ContentWindow", u"Current", None))
        self.gameStatus1SuccessButton.setText(QCoreApplication.translate("ContentWindow", u"Successful", None))
        self.gameStatus2FailedButton.setText(QCoreApplication.translate("ContentWindow", u"Failed", None))
        self.gameStatus3ForcedFailedButton.setText(QCoreApplication.translate("ContentWindow", u"Force Retry", None))
        self.gamePositionLabel.setText(QCoreApplication.translate("ContentWindow", u"Move", None))
        self.gamePosition0FarLeftButton.setText(QCoreApplication.translate("ContentWindow", u"\u23ee", None))
        self.gamePosition1LeftButton.setText(QCoreApplication.translate("ContentWindow", u"\u23f4", None))
        self.gamePosition2RightButton.setText(QCoreApplication.translate("ContentWindow", u"\u23f5", None))
        self.gamePosition3FarRightButton.setText(QCoreApplication.translate("ContentWindow", u"\u23ed", None))
        self.menuFile.setTitle(QCoreApplication.translate("ContentWindow", u"File", None))
    # retranslateUi

