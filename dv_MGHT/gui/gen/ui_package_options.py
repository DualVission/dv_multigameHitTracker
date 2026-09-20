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
    QDialogButtonBox, QDoubleSpinBox, QFrame, QGridLayout,
    QLabel, QPushButton, QScrollArea, QSizePolicy,
    QSpinBox, QVBoxLayout, QWidget)

class Ui_PackageOptionsWindow(object):
    def setupUi(self, PackageOptionsWindow):
        if not PackageOptionsWindow.objectName():
            PackageOptionsWindow.setObjectName(u"PackageOptionsWindow")
        PackageOptionsWindow.setWindowModality(Qt.WindowModality.ApplicationModal)
        PackageOptionsWindow.resize(362, 400)
        PackageOptionsWindow.setStyleSheet(u"QLabel {\n"
"	qproperty-wordWrap: true;\n"
"	max-height: 100%;\n"
"}\n"
"*[ sectionHeader ] {\n"
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
        self.packageSubWidget = QWidget()
        self.packageSubWidget.setObjectName(u"packageSubWidget")
        self.packageSubWidget.setGeometry(QRect(0, 0, 300, 249))
        self.packageSubLayout = QVBoxLayout(self.packageSubWidget)
        self.packageSubLayout.setObjectName(u"packageSubLayout")
        self.package1Label = QLabel(self.packageSubWidget)
        self.package1Label.setObjectName(u"package1Label")
        self.package1Label.setProperty(u"sectionHeader", 2)

        self.packageSubLayout.addWidget(self.package1Label)

        self.package1Grid = QGridLayout()
        self.package1Grid.setObjectName(u"package1Grid")
        self.package1CounterLabel = QLabel(self.packageSubWidget)
        self.package1CounterLabel.setObjectName(u"package1CounterLabel")

        self.package1Grid.addWidget(self.package1CounterLabel, 0, 0, 1, 1)

        self.package2GameBgImgCheck = QCheckBox(self.packageSubWidget)
        self.package2GameBgImgCheck.setObjectName(u"package2GameBgImgCheck")

        self.package1Grid.addWidget(self.package2GameBgImgCheck, 1, 1, 1, 1)

        self.package1CounterCheck = QCheckBox(self.packageSubWidget)
        self.package1CounterCheck.setObjectName(u"package1CounterCheck")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.package1CounterCheck.sizePolicy().hasHeightForWidth())
        self.package1CounterCheck.setSizePolicy(sizePolicy)
        self.package1CounterCheck.setText(u"")

        self.package1Grid.addWidget(self.package1CounterCheck, 0, 1, 1, 1)

        self.package2GameBgImgLabel = QLabel(self.packageSubWidget)
        self.package2GameBgImgLabel.setObjectName(u"package2GameBgImgLabel")

        self.package1Grid.addWidget(self.package2GameBgImgLabel, 1, 0, 1, 1)

        self.package1Grid.setColumnStretch(1, 1)

        self.packageSubLayout.addLayout(self.package1Grid)

        self.package2Label = QLabel(self.packageSubWidget)
        self.package2Label.setObjectName(u"package2Label")
        self.package2Label.setProperty(u"sectionHeader", 2)

        self.packageSubLayout.addWidget(self.package2Label)

        self.package2Grid = QGridLayout()
        self.package2Grid.setObjectName(u"package2Grid")
        self.package1GameBoardScaleLabel = QLabel(self.packageSubWidget)
        self.package1GameBoardScaleLabel.setObjectName(u"package1GameBoardScaleLabel")

        self.package2Grid.addWidget(self.package1GameBoardScaleLabel, 2, 1, 1, 1)

        self.package1GameBoardSizeButton = QPushButton(self.packageSubWidget)
        self.package1GameBoardSizeButton.setObjectName(u"package1GameBoardSizeButton")
        icon = QIcon(QIcon.fromTheme(QIcon.ThemeIcon.WindowNew))
        self.package1GameBoardSizeButton.setIcon(icon)

        self.package2Grid.addWidget(self.package1GameBoardSizeButton, 3, 1, 1, 2)

        self.package1GameBoardSizeXBox = QSpinBox(self.packageSubWidget)
        self.package1GameBoardSizeXBox.setObjectName(u"package1GameBoardSizeXBox")
        self.package1GameBoardSizeXBox.setMaximum(10000)

        self.package2Grid.addWidget(self.package1GameBoardSizeXBox, 0, 2, 1, 1)

        self.package1GameBoardLabel = QLabel(self.packageSubWidget)
        self.package1GameBoardLabel.setObjectName(u"package1GameBoardLabel")

        self.package2Grid.addWidget(self.package1GameBoardLabel, 0, 0, 4, 1)

        self.package1GameBoardSizeLabel = QLabel(self.packageSubWidget)
        self.package1GameBoardSizeLabel.setObjectName(u"package1GameBoardSizeLabel")

        self.package2Grid.addWidget(self.package1GameBoardSizeLabel, 0, 1, 2, 1)

        self.package1GameBoardScaleBox = QDoubleSpinBox(self.packageSubWidget)
        self.package1GameBoardScaleBox.setObjectName(u"package1GameBoardScaleBox")
        self.package1GameBoardScaleBox.setDecimals(2)
        self.package1GameBoardScaleBox.setMinimum(0.100000000000000)
        self.package1GameBoardScaleBox.setMaximum(100.000000000000000)
        self.package1GameBoardScaleBox.setSingleStep(0.100000000000000)
        self.package1GameBoardScaleBox.setValue(2.000000000000000)

        self.package2Grid.addWidget(self.package1GameBoardScaleBox, 2, 2, 1, 1)

        self.package1GameBoardSizeYBox = QSpinBox(self.packageSubWidget)
        self.package1GameBoardSizeYBox.setObjectName(u"package1GameBoardSizeYBox")
        self.package1GameBoardSizeYBox.setMaximum(4000)

        self.package2Grid.addWidget(self.package1GameBoardSizeYBox, 1, 2, 1, 1)

        self.package2Grid.setColumnStretch(2, 1)

        self.packageSubLayout.addLayout(self.package2Grid)

        self.packageScroll.setWidget(self.packageSubWidget)

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
        self.gameOptionsWidget.setGeometry(QRect(0, 0, 308, 90))
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
        self.package1Label.setText(QCoreApplication.translate("PackageOptionsWindow", u"General", None))
        self.package1CounterLabel.setText(QCoreApplication.translate("PackageOptionsWindow", u"Display Hit Counter on Game Tiles", None))
        self.package2GameBgImgCheck.setText("")
        self.package2GameBgImgLabel.setText(QCoreApplication.translate("PackageOptionsWindow", u"Display Background Images on Game Tiles", None))
        self.package2Label.setText(QCoreApplication.translate("PackageOptionsWindow", u"<html><head/><body><p>NDI<span style=\" vertical-align:super;\">\u00ae</span></p></body></html>", None))
        self.package1GameBoardScaleLabel.setText(QCoreApplication.translate("PackageOptionsWindow", u"Scale", None))
        self.package1GameBoardSizeButton.setText(QCoreApplication.translate("PackageOptionsWindow", u"Display Window", None))
        self.package1GameBoardSizeXBox.setSuffix(QCoreApplication.translate("PackageOptionsWindow", u"px", None))
        self.package1GameBoardLabel.setText(QCoreApplication.translate("PackageOptionsWindow", u"Game Board", None))
        self.package1GameBoardSizeLabel.setText(QCoreApplication.translate("PackageOptionsWindow", u"Size", None))
        self.package1GameBoardSizeYBox.setSuffix(QCoreApplication.translate("PackageOptionsWindow", u"px", None))
        self.gameLabel.setText(QCoreApplication.translate("PackageOptionsWindow", u"Game Options", None))
    # retranslateUi

