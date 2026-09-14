# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'package_options.ui'
##
## Created by: Qt User Interface Compiler version 6.11.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QAbstractButton, QApplication, QCheckBox, QDialog,
    QDialogButtonBox, QFrame, QGridLayout, QLabel,
    QPushButton, QScrollArea, QSizePolicy, QSpinBox,
    QVBoxLayout, QWidget)

class Ui_PackageOptionsWindow(object):
    def setupUi(self, PackageOptionsWindow):
        if not PackageOptionsWindow.objectName():
            PackageOptionsWindow.setObjectName(u"PackageOptionsWindow")
        PackageOptionsWindow.setWindowModality(Qt.WindowModality.ApplicationModal)
        PackageOptionsWindow.resize(362, 354)
        PackageOptionsWindow.setStyleSheet(u"*[ sectionHeader ] {\n"
"	text-align: bottom;\n"
"}\n"
"*[ sectionHeader=\"1\" ]{\n"
"	font: 550 14pt \"Segoe UI\";\n"
"	border-bottom: 2px solid white;\n"
"}\n"
"*[ sectionHeader=\"2\" ]{\n"
"	font: 650 13pt \"Segoe UI\";\n"
"	border-bottom: 1px solid white;\n"
"}\n"
"*[ sectionHeader=\"3\" ]{\n"
"	font: 750 12pt \"Segoe UI\";\n"
"	border-bottom: 1px dotted white;\n"
"}\n"
"*[ sectionHeader=\"4\" ]{\n"
"	font: 850 11pt \"Segoe UI\";\n"
"}")
        PackageOptionsWindow.setModal(True)
        self.windowLayout = QVBoxLayout(PackageOptionsWindow)
        self.windowLayout.setObjectName(u"windowLayout")
        self.mainLayoutWidget = QWidget(PackageOptionsWindow)
        self.mainLayoutWidget.setObjectName(u"mainLayoutWidget")
        self.mainLayout = QVBoxLayout(self.mainLayoutWidget)
        self.mainLayout.setObjectName(u"mainLayout")
        self.packageWidget = QWidget(self.mainLayoutWidget)
        self.packageWidget.setObjectName(u"packageWidget")
        self.packageWidget.setMinimumSize(QSize(0, 140))
        self.packageLayout = QVBoxLayout(self.packageWidget)
        self.packageLayout.setObjectName(u"packageLayout")
        self.packageLayout.setContentsMargins(5, -1, -1, -1)
        self.packageLabel = QLabel(self.packageWidget)
        self.packageLabel.setObjectName(u"packageLabel")
        self.packageLabel.setProperty(u"sectionHeader", 1)

        self.packageLayout.addWidget(self.packageLabel)

        self.packageScroll = QScrollArea(self.packageWidget)
        self.packageScroll.setObjectName(u"packageScroll")
        self.packageScroll.setFrameShape(QFrame.Shape.NoFrame)
        self.packageScroll.setWidgetResizable(True)
        self.packageGridWidget = QWidget()
        self.packageGridWidget.setObjectName(u"packageGridWidget")
        self.packageGridWidget.setStyleSheet(u"QLabel {\n"
"	qproperty-wordWrap: true;\n"
"}")
        self.packageGrid = QGridLayout(self.packageGridWidget)
        self.packageGrid.setObjectName(u"packageGrid")
        self.package1CounterLabel = QLabel(self.packageGridWidget)
        self.package1CounterLabel.setObjectName(u"package1CounterLabel")

        self.packageGrid.addWidget(self.package1CounterLabel, 0, 0, 1, 1)

        self.package2GameBgImgCheck = QCheckBox(self.packageGridWidget)
        self.package2GameBgImgCheck.setObjectName(u"package2GameBgImgCheck")

        self.packageGrid.addWidget(self.package2GameBgImgCheck, 1, 1, 1, 1)

        self.package2GameBgImgLabel = QLabel(self.packageGridWidget)
        self.package2GameBgImgLabel.setObjectName(u"package2GameBgImgLabel")

        self.packageGrid.addWidget(self.package2GameBgImgLabel, 1, 0, 1, 1)

        self.package1CounterCheck = QCheckBox(self.packageGridWidget)
        self.package1CounterCheck.setObjectName(u"package1CounterCheck")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.package1CounterCheck.sizePolicy().hasHeightForWidth())
        self.package1CounterCheck.setSizePolicy(sizePolicy)
        self.package1CounterCheck.setText(u"")

        self.packageGrid.addWidget(self.package1CounterCheck, 0, 1, 1, 1)

        self.package3GameBoardSizeLabel = QLabel(self.packageGridWidget)
        self.package3GameBoardSizeLabel.setObjectName(u"package3GameBoardSizeLabel")

        self.packageGrid.addWidget(self.package3GameBoardSizeLabel, 2, 0, 1, 1)

        self.package3GameBoardSizeLayout = QVBoxLayout()
        self.package3GameBoardSizeLayout.setObjectName(u"package3GameBoardSizeLayout")
        self.package3GameBoardSizeXBox = QSpinBox(self.packageGridWidget)
        self.package3GameBoardSizeXBox.setObjectName(u"package3GameBoardSizeXBox")
        self.package3GameBoardSizeXBox.setMaximum(10000)

        self.package3GameBoardSizeLayout.addWidget(self.package3GameBoardSizeXBox)

        self.package3GameBoardSizeYBox = QSpinBox(self.packageGridWidget)
        self.package3GameBoardSizeYBox.setObjectName(u"package3GameBoardSizeYBox")
        self.package3GameBoardSizeYBox.setMaximum(4000)

        self.package3GameBoardSizeLayout.addWidget(self.package3GameBoardSizeYBox)

        self.package3GameBoardSizeButton = QPushButton(self.packageGridWidget)
        self.package3GameBoardSizeButton.setObjectName(u"package3GameBoardSizeButton")

        self.package3GameBoardSizeLayout.addWidget(self.package3GameBoardSizeButton)


        self.packageGrid.addLayout(self.package3GameBoardSizeLayout, 2, 1, 1, 1)

        self.packageScroll.setWidget(self.packageGridWidget)

        self.packageLayout.addWidget(self.packageScroll)


        self.mainLayout.addWidget(self.packageWidget)

        self.gameWidget = QWidget(self.mainLayoutWidget)
        self.gameWidget.setObjectName(u"gameWidget")
        self.gameWidget.setMinimumSize(QSize(0, 140))
        self.gameLayout = QVBoxLayout(self.gameWidget)
        self.gameLayout.setObjectName(u"gameLayout")
        self.gameLabel = QLabel(self.gameWidget)
        self.gameLabel.setObjectName(u"gameLabel")
        self.gameLabel.setProperty(u"sectionHeader", 1)

        self.gameLayout.addWidget(self.gameLabel)

        self.gameScroll = QScrollArea(self.gameWidget)
        self.gameScroll.setObjectName(u"gameScroll")
        self.gameScroll.setFrameShape(QFrame.Shape.NoFrame)
        self.gameScroll.setWidgetResizable(True)
        self.gameOptionsWidget = QWidget()
        self.gameOptionsWidget.setObjectName(u"gameOptionsWidget")
        self.gameOptionsLayout = QVBoxLayout(self.gameOptionsWidget)
        self.gameOptionsLayout.setObjectName(u"gameOptionsLayout")
        self.gameScroll.setWidget(self.gameOptionsWidget)

        self.gameLayout.addWidget(self.gameScroll)


        self.mainLayout.addWidget(self.gameWidget)


        self.windowLayout.addWidget(self.mainLayoutWidget)

        self.buttonBox = QDialogButtonBox(PackageOptionsWindow)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setOrientation(Qt.Orientation.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.StandardButton.Save)

        self.windowLayout.addWidget(self.buttonBox)


        self.retranslateUi(PackageOptionsWindow)
        self.buttonBox.accepted.connect(PackageOptionsWindow.accept)
        self.buttonBox.rejected.connect(PackageOptionsWindow.reject)

        QMetaObject.connectSlotsByName(PackageOptionsWindow)
    # setupUi

    def retranslateUi(self, PackageOptionsWindow):
        PackageOptionsWindow.setWindowTitle(QCoreApplication.translate("PackageOptionsWindow", u"Dialog", None))
        self.packageLabel.setText(QCoreApplication.translate("PackageOptionsWindow", u"Package Level Options", None))
        self.package1CounterLabel.setText(QCoreApplication.translate("PackageOptionsWindow", u"Display Hit Counter on Game Tiles", None))
        self.package2GameBgImgCheck.setText("")
        self.package2GameBgImgLabel.setText(QCoreApplication.translate("PackageOptionsWindow", u"Display Background Images on Game Tiles", None))
        self.package3GameBoardSizeLabel.setText(QCoreApplication.translate("PackageOptionsWindow", u"NDI Game Board Size", None))
        self.package3GameBoardSizeXBox.setSuffix(QCoreApplication.translate("PackageOptionsWindow", u"px", None))
        self.package3GameBoardSizeYBox.setSuffix(QCoreApplication.translate("PackageOptionsWindow", u"px", None))
        self.package3GameBoardSizeButton.setText(QCoreApplication.translate("PackageOptionsWindow", u"Display NDI Window", None))
        self.gameLabel.setText(QCoreApplication.translate("PackageOptionsWindow", u"Game Options", None))
    # retranslateUi

