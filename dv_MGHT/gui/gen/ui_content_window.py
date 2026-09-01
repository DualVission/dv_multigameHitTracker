# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'content_window.ui'
##
## Created by: Qt User Interface Compiler version 6.11.2
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
from PySide6.QtWidgets import (QApplication, QFrame, QGridLayout, QHBoxLayout,
    QLabel, QListWidget, QListWidgetItem, QMainWindow,
    QMenu, QMenuBar, QPushButton, QSizePolicy,
    QSpacerItem, QStatusBar, QToolButton, QVBoxLayout,
    QWidget)

class Ui_ContentWindow(object):
    def setupUi(self, ContentWindow):
        if not ContentWindow.objectName():
            ContentWindow.setObjectName(u"ContentWindow")
        ContentWindow.resize(767, 640)
        ContentWindow.setStyleSheet(u"QToolButton {\n"
"	font-family: \"Segoe UI Symbol\";\n"
"}")
        self.actionLoadPackage = QAction(ContentWindow)
        self.actionLoadPackage.setObjectName(u"actionLoadPackage")
        self.actionDarkMode = QAction(ContentWindow)
        self.actionDarkMode.setObjectName(u"actionDarkMode")
        self.actionDarkMode.setCheckable(True)
        self.actionDarkMode.setChecked(True)
        self.actionDisplayCounters = QAction(ContentWindow)
        self.actionDisplayCounters.setObjectName(u"actionDisplayCounters")
        self.actionDisplayCounters.setCheckable(True)
        self.actionRandomizeOrderOpenOnStartup = QAction(ContentWindow)
        self.actionRandomizeOrderOpenOnStartup.setObjectName(u"actionRandomizeOrderOpenOnStartup")
        self.actionRandomizeOrderOpenOnStartup.setCheckable(True)
        self.actionRandomizeOrderOpenOnStartup.setChecked(True)
        self.centralwidget = QWidget(ContentWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.gameDisplayWidget = QWidget(self.centralwidget)
        self.gameDisplayWidget.setObjectName(u"gameDisplayWidget")
        self.gameDisplayWidget.setContextMenuPolicy(Qt.ContextMenuPolicy.NoContextMenu)
        self.gameDisplayWidget.setStyleSheet(u"QStackedWidget {\n"
"}")

        self.verticalLayout.addWidget(self.gameDisplayWidget)

        self.selectedGameLayoutWidget = QWidget(self.centralwidget)
        self.selectedGameLayoutWidget.setObjectName(u"selectedGameLayoutWidget")
        self.selectedGameLayout = QVBoxLayout(self.selectedGameLayoutWidget)
        self.selectedGameLayout.setObjectName(u"selectedGameLayout")
        self.selectedGameLabel = QLabel(self.selectedGameLayoutWidget)
        self.selectedGameLabel.setObjectName(u"selectedGameLabel")
        self.selectedGameLabel.setAlignment(Qt.AlignmentFlag.AlignCenter)

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

        self.midSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Maximum, QSizePolicy.Policy.Minimum)

        self.gameButtonsLayout.addItem(self.midSpacer)

        self.gamePositionLayout = QHBoxLayout()
        self.gamePositionLayout.setObjectName(u"gamePositionLayout")
        self.gamePositionLabel = QLabel(self.selectedGameLayoutWidget)
        self.gamePositionLabel.setObjectName(u"gamePositionLabel")

        self.gamePositionLayout.addWidget(self.gamePositionLabel)

        self.gamePosition0FarLeftButton = QToolButton(self.selectedGameLayoutWidget)
        self.gamePosition0FarLeftButton.setObjectName(u"gamePosition0FarLeftButton")
        self.gamePosition0FarLeftButton.setToolButtonStyle(Qt.ToolButtonStyle.ToolButtonIconOnly)
        self.gamePosition0FarLeftButton.setArrowType(Qt.ArrowType.NoArrow)

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

        self.gameOrderLayout = QVBoxLayout()
        self.gameOrderLayout.setObjectName(u"gameOrderLayout")
        self.gameOrderLayout.setContentsMargins(-1, 5, -1, 5)
        self.gameOrderTitleLayout = QHBoxLayout()
        self.gameOrderTitleLayout.setObjectName(u"gameOrderTitleLayout")
        self.gameOrderTitleLayout.setContentsMargins(5, 5, 5, -1)
        self.postspacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gameOrderTitleLayout.addItem(self.postspacer)

        self.gameOrderTitleLabel = QLabel(self.centralwidget)
        self.gameOrderTitleLabel.setObjectName(u"gameOrderTitleLabel")

        self.gameOrderTitleLayout.addWidget(self.gameOrderTitleLabel)

        self.gameOrderTitleButton = QToolButton(self.centralwidget)
        self.gameOrderTitleButton.setObjectName(u"gameOrderTitleButton")
        self.gameOrderTitleButton.setToolButtonStyle(Qt.ToolButtonStyle.ToolButtonIconOnly)
        self.gameOrderTitleButton.setArrowType(Qt.ArrowType.DownArrow)

        self.gameOrderTitleLayout.addWidget(self.gameOrderTitleButton)

        self.prespacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gameOrderTitleLayout.addItem(self.prespacer)


        self.gameOrderLayout.addLayout(self.gameOrderTitleLayout)

        self.gameOrderLine = QFrame(self.centralwidget)
        self.gameOrderLine.setObjectName(u"gameOrderLine")
        self.gameOrderLine.setFrameShadow(QFrame.Shadow.Raised)
        self.gameOrderLine.setFrameShape(QFrame.Shape.HLine)

        self.gameOrderLayout.addWidget(self.gameOrderLine)

        self.gameOrderOptionsLayoutWidget = QWidget(self.centralwidget)
        self.gameOrderOptionsLayoutWidget.setObjectName(u"gameOrderOptionsLayoutWidget")
        self.gameOrderOptionsLayout = QGridLayout(self.gameOrderOptionsLayoutWidget)
        self.gameOrderOptionsLayout.setObjectName(u"gameOrderOptionsLayout")
        self.gameOrderShuffleAllButton = QPushButton(self.gameOrderOptionsLayoutWidget)
        self.gameOrderShuffleAllButton.setObjectName(u"gameOrderShuffleAllButton")

        self.gameOrderOptionsLayout.addWidget(self.gameOrderShuffleAllButton, 0, 0, 1, 1)

        self.gameOrderShuffleAfterButton = QPushButton(self.gameOrderOptionsLayoutWidget)
        self.gameOrderShuffleAfterButton.setObjectName(u"gameOrderShuffleAfterButton")
        self.gameOrderShuffleAfterButton.setEnabled(False)

        self.gameOrderOptionsLayout.addWidget(self.gameOrderShuffleAfterButton, 0, 1, 1, 1)

        self.gameOrderShuffleClearAllButton = QPushButton(self.gameOrderOptionsLayoutWidget)
        self.gameOrderShuffleClearAllButton.setObjectName(u"gameOrderShuffleClearAllButton")

        self.gameOrderOptionsLayout.addWidget(self.gameOrderShuffleClearAllButton, 1, 0, 1, 1)

        self.gameOrderSmartShuffleButton = QPushButton(self.gameOrderOptionsLayoutWidget)
        self.gameOrderSmartShuffleButton.setObjectName(u"gameOrderSmartShuffleButton")

        self.gameOrderOptionsLayout.addWidget(self.gameOrderSmartShuffleButton, 0, 2, 1, 1)

        self.gameOrderShuffleClearAfterButton = QPushButton(self.gameOrderOptionsLayoutWidget)
        self.gameOrderShuffleClearAfterButton.setObjectName(u"gameOrderShuffleClearAfterButton")
        self.gameOrderShuffleClearAfterButton.setEnabled(False)

        self.gameOrderOptionsLayout.addWidget(self.gameOrderShuffleClearAfterButton, 1, 1, 1, 1)

        self.gameOrderSmartShuffleClearButton = QPushButton(self.gameOrderOptionsLayoutWidget)
        self.gameOrderSmartShuffleClearButton.setObjectName(u"gameOrderSmartShuffleClearButton")

        self.gameOrderOptionsLayout.addWidget(self.gameOrderSmartShuffleClearButton, 1, 2, 1, 1)

        self.gameOrderClearAllButton = QPushButton(self.gameOrderOptionsLayoutWidget)
        self.gameOrderClearAllButton.setObjectName(u"gameOrderClearAllButton")

        self.gameOrderOptionsLayout.addWidget(self.gameOrderClearAllButton, 2, 0, 1, 1)

        self.gameOrderClearAfterButton = QPushButton(self.gameOrderOptionsLayoutWidget)
        self.gameOrderClearAfterButton.setObjectName(u"gameOrderClearAfterButton")
        self.gameOrderClearAfterButton.setEnabled(False)

        self.gameOrderOptionsLayout.addWidget(self.gameOrderClearAfterButton, 2, 1, 1, 1)


        self.gameOrderLayout.addWidget(self.gameOrderOptionsLayoutWidget)


        self.verticalLayout.addLayout(self.gameOrderLayout)

        self.splitDisplayWidget = QListWidget(self.centralwidget)
        self.splitDisplayWidget.setObjectName(u"splitDisplayWidget")

        self.verticalLayout.addWidget(self.splitDisplayWidget)

        ContentWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(ContentWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 767, 33))
        self.menuFile = QMenu(self.menubar)
        self.menuFile.setObjectName(u"menuFile")
        self.menuOptions = QMenu(self.menubar)
        self.menuOptions.setObjectName(u"menuOptions")
        ContentWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(ContentWindow)
        self.statusbar.setObjectName(u"statusbar")
        ContentWindow.setStatusBar(self.statusbar)
        QWidget.setTabOrder(self.gameStatus0CurrentButton, self.gameStatus1SuccessButton)
        QWidget.setTabOrder(self.gameStatus1SuccessButton, self.gameStatus2FailedButton)
        QWidget.setTabOrder(self.gameStatus2FailedButton, self.gameStatus3ForcedFailedButton)
        QWidget.setTabOrder(self.gameStatus3ForcedFailedButton, self.gamePosition0FarLeftButton)
        QWidget.setTabOrder(self.gamePosition0FarLeftButton, self.gamePosition1LeftButton)
        QWidget.setTabOrder(self.gamePosition1LeftButton, self.gamePosition2RightButton)
        QWidget.setTabOrder(self.gamePosition2RightButton, self.gamePosition3FarRightButton)
        QWidget.setTabOrder(self.gamePosition3FarRightButton, self.gameOrderTitleButton)
        QWidget.setTabOrder(self.gameOrderTitleButton, self.gameOrderShuffleAllButton)
        QWidget.setTabOrder(self.gameOrderShuffleAllButton, self.gameOrderShuffleAfterButton)
        QWidget.setTabOrder(self.gameOrderShuffleAfterButton, self.gameOrderSmartShuffleButton)
        QWidget.setTabOrder(self.gameOrderSmartShuffleButton, self.gameOrderShuffleClearAllButton)
        QWidget.setTabOrder(self.gameOrderShuffleClearAllButton, self.gameOrderShuffleClearAfterButton)
        QWidget.setTabOrder(self.gameOrderShuffleClearAfterButton, self.gameOrderSmartShuffleClearButton)
        QWidget.setTabOrder(self.gameOrderSmartShuffleClearButton, self.gameOrderClearAllButton)
        QWidget.setTabOrder(self.gameOrderClearAllButton, self.gameOrderClearAfterButton)
        QWidget.setTabOrder(self.gameOrderClearAfterButton, self.splitDisplayWidget)

        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuOptions.menuAction())
        self.menuFile.addAction(self.actionLoadPackage)
        self.menuOptions.addAction(self.actionDarkMode)
        self.menuOptions.addAction(self.actionDisplayCounters)
        self.menuOptions.addAction(self.actionRandomizeOrderOpenOnStartup)

        self.retranslateUi(ContentWindow)

        QMetaObject.connectSlotsByName(ContentWindow)
    # setupUi

    def retranslateUi(self, ContentWindow):
        ContentWindow.setWindowTitle(QCoreApplication.translate("ContentWindow", u"MainWindow", None))
        self.actionLoadPackage.setText(QCoreApplication.translate("ContentWindow", u"Load Package...", None))
        self.actionDarkMode.setText(QCoreApplication.translate("ContentWindow", u"Dark Mode", None))
        self.actionDisplayCounters.setText(QCoreApplication.translate("ContentWindow", u"Display Counters", None))
        self.actionRandomizeOrderOpenOnStartup.setText(QCoreApplication.translate("ContentWindow", u"Randomize Order Open on Startup", None))
        self.selectedGameLabel.setText(QCoreApplication.translate("ContentWindow", u"TextLabel", None))
        self.gameStatusLabel.setText(QCoreApplication.translate("ContentWindow", u"Set Status to", None))
        self.gameStatus0CurrentButton.setText(QCoreApplication.translate("ContentWindow", u"Current", None))
        self.gameStatus1SuccessButton.setText(QCoreApplication.translate("ContentWindow", u"Successful", None))
        self.gameStatus2FailedButton.setText(QCoreApplication.translate("ContentWindow", u"Failed", None))
        self.gameStatus3ForcedFailedButton.setText(QCoreApplication.translate("ContentWindow", u"Force Retry", None))
        self.gamePositionLabel.setText(QCoreApplication.translate("ContentWindow", u"Move", None))
        self.gamePosition0FarLeftButton.setText(QCoreApplication.translate("ContentWindow", u"\u23ee", None))
        self.gamePosition1LeftButton.setText(QCoreApplication.translate("ContentWindow", u"\u23f4", None))
        self.gamePosition2RightButton.setText(QCoreApplication.translate("ContentWindow", u"\u23f5", None))
        self.gamePosition3FarRightButton.setText(QCoreApplication.translate("ContentWindow", u"\u23ed", None))
        self.gameOrderTitleLabel.setText(QCoreApplication.translate("ContentWindow", u"Randomize Order", None))
        self.gameOrderTitleButton.setText("")
        self.gameOrderShuffleAllButton.setText(QCoreApplication.translate("ContentWindow", u"Shuffle All", None))
        self.gameOrderShuffleAfterButton.setText(QCoreApplication.translate("ContentWindow", u"Shuffle after Selected", None))
        self.gameOrderShuffleClearAllButton.setText(QCoreApplication.translate("ContentWindow", u"Clear Status And Shuffle All", None))
        self.gameOrderSmartShuffleButton.setText(QCoreApplication.translate("ContentWindow", u"Shift Success Chain Left", None))
        self.gameOrderShuffleClearAfterButton.setText(QCoreApplication.translate("ContentWindow", u"Clear Status And Shuffle After Selected", None))
        self.gameOrderSmartShuffleClearButton.setText(QCoreApplication.translate("ContentWindow", u"Shift Success Chain And Clear Status", None))
        self.gameOrderClearAllButton.setText(QCoreApplication.translate("ContentWindow", u"Clear All Status", None))
        self.gameOrderClearAfterButton.setText(QCoreApplication.translate("ContentWindow", u"Clear Status After Selected", None))
        self.menuFile.setTitle(QCoreApplication.translate("ContentWindow", u"File", None))
        self.menuOptions.setTitle(QCoreApplication.translate("ContentWindow", u"Options", None))
    # retranslateUi

