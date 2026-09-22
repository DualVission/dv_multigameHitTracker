# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'options_window.ui'
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
    QScrollArea, QSizePolicy, QToolButton, QVBoxLayout,
    QWidget)

class Ui_optionsWindow(object):
    def setupUi(self, optionsWindow):
        if not optionsWindow.objectName():
            optionsWindow.setObjectName(u"optionsWindow")
        optionsWindow.resize(362, 400)
        optionsWindow.setStyleSheet(u"QLabel {\n"
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
        self.windowLayout = QVBoxLayout(optionsWindow)
        self.windowLayout.setObjectName(u"windowLayout")
        self.mainLayoutWidget = QVBoxLayout()
        self.mainLayoutWidget.setObjectName(u"mainLayoutWidget")
        self.optionsScroll = QScrollArea(optionsWindow)
        self.optionsScroll.setObjectName(u"optionsScroll")
        self.optionsScroll.setFrameShape(QFrame.Shape.NoFrame)
        self.optionsScroll.setWidgetResizable(True)
        self.optionsWidget = QWidget()
        self.optionsWidget.setObjectName(u"optionsWidget")
        self.optionsWidget.setGeometry(QRect(0, 0, 342, 348))
        self.optionsLayout = QVBoxLayout(self.optionsWidget)
        self.optionsLayout.setObjectName(u"optionsLayout")
        self.generalLayout = QVBoxLayout()
        self.generalLayout.setObjectName(u"generalLayout")
        self.generalLabel = QLabel(self.optionsWidget)
        self.generalLabel.setObjectName(u"generalLabel")
        self.generalLabel.setProperty(u"sectionHeader", 1)

        self.generalLayout.addWidget(self.generalLabel)

        self.generalGrid = QGridLayout()
        self.generalGrid.setObjectName(u"generalGrid")
        self.general2RandomizeOrderLabel = QLabel(self.optionsWidget)
        self.general2RandomizeOrderLabel.setObjectName(u"general2RandomizeOrderLabel")

        self.generalGrid.addWidget(self.general2RandomizeOrderLabel, 1, 0, 1, 1)

        self.general1DarkModeLabel = QLabel(self.optionsWidget)
        self.general1DarkModeLabel.setObjectName(u"general1DarkModeLabel")

        self.generalGrid.addWidget(self.general1DarkModeLabel, 0, 0, 1, 1)

        self.general1DarkModeCheck = QCheckBox(self.optionsWidget)
        self.general1DarkModeCheck.setObjectName(u"general1DarkModeCheck")

        self.generalGrid.addWidget(self.general1DarkModeCheck, 0, 1, 1, 1)

        self.general2RandomizeOrderCheck = QCheckBox(self.optionsWidget)
        self.general2RandomizeOrderCheck.setObjectName(u"general2RandomizeOrderCheck")

        self.generalGrid.addWidget(self.general2RandomizeOrderCheck, 1, 1, 1, 1)

        self.generalGrid.setColumnStretch(0, 1)

        self.generalLayout.addLayout(self.generalGrid)


        self.optionsLayout.addLayout(self.generalLayout)

        self.statusColorLayout = QVBoxLayout()
        self.statusColorLayout.setObjectName(u"statusColorLayout")
        self.statusColorLabel = QLabel(self.optionsWidget)
        self.statusColorLabel.setObjectName(u"statusColorLabel")
        self.statusColorLabel.setProperty(u"sectionHeader", 1)

        self.statusColorLayout.addWidget(self.statusColorLabel)

        self.statusColorGrid = QGridLayout()
        self.statusColorGrid.setObjectName(u"statusColorGrid")
        self.statusSelectedButton = QToolButton(self.optionsWidget)
        self.statusSelectedButton.setObjectName(u"statusSelectedButton")

        self.statusColorGrid.addWidget(self.statusSelectedButton, 1, 1, 1, 1)

        self.statusFailedLabel = QLabel(self.optionsWidget)
        self.statusFailedLabel.setObjectName(u"statusFailedLabel")

        self.statusColorGrid.addWidget(self.statusFailedLabel, 4, 0, 1, 1)

        self.statusFailedButton = QToolButton(self.optionsWidget)
        self.statusFailedButton.setObjectName(u"statusFailedButton")

        self.statusColorGrid.addWidget(self.statusFailedButton, 4, 1, 1, 1)

        self.statusCurrentLabel = QLabel(self.optionsWidget)
        self.statusCurrentLabel.setObjectName(u"statusCurrentLabel")

        self.statusColorGrid.addWidget(self.statusCurrentLabel, 2, 0, 1, 1)

        self.statusForceFailedButton = QToolButton(self.optionsWidget)
        self.statusForceFailedButton.setObjectName(u"statusForceFailedButton")

        self.statusColorGrid.addWidget(self.statusForceFailedButton, 5, 1, 1, 1)

        self.statusSelectedLabel = QLabel(self.optionsWidget)
        self.statusSelectedLabel.setObjectName(u"statusSelectedLabel")

        self.statusColorGrid.addWidget(self.statusSelectedLabel, 1, 0, 1, 1)

        self.statusSuccessLabel = QLabel(self.optionsWidget)
        self.statusSuccessLabel.setObjectName(u"statusSuccessLabel")

        self.statusColorGrid.addWidget(self.statusSuccessLabel, 3, 0, 1, 1)

        self.statusUpcomingLabel = QLabel(self.optionsWidget)
        self.statusUpcomingLabel.setObjectName(u"statusUpcomingLabel")

        self.statusColorGrid.addWidget(self.statusUpcomingLabel, 0, 0, 1, 1)

        self.statusSuccessButton = QToolButton(self.optionsWidget)
        self.statusSuccessButton.setObjectName(u"statusSuccessButton")

        self.statusColorGrid.addWidget(self.statusSuccessButton, 3, 1, 1, 1)

        self.statusForceFailedLabel = QLabel(self.optionsWidget)
        self.statusForceFailedLabel.setObjectName(u"statusForceFailedLabel")

        self.statusColorGrid.addWidget(self.statusForceFailedLabel, 5, 0, 1, 1)

        self.statusCurrentButton = QToolButton(self.optionsWidget)
        self.statusCurrentButton.setObjectName(u"statusCurrentButton")

        self.statusColorGrid.addWidget(self.statusCurrentButton, 2, 1, 1, 1)

        self.statusUpcomingButton = QToolButton(self.optionsWidget)
        self.statusUpcomingButton.setObjectName(u"statusUpcomingButton")

        self.statusColorGrid.addWidget(self.statusUpcomingButton, 0, 1, 1, 1)

        self.statusColorGrid.setColumnStretch(0, 1)

        self.statusColorLayout.addLayout(self.statusColorGrid)


        self.optionsLayout.addLayout(self.statusColorLayout)

        self.optionsScroll.setWidget(self.optionsWidget)

        self.mainLayoutWidget.addWidget(self.optionsScroll)


        self.windowLayout.addLayout(self.mainLayoutWidget)

        self.buttonBox = QDialogButtonBox(optionsWindow)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setStandardButtons(QDialogButtonBox.StandardButton.Save)

        self.windowLayout.addWidget(self.buttonBox)

#if QT_CONFIG(shortcut)
        self.general2RandomizeOrderLabel.setBuddy(self.general2RandomizeOrderCheck)
        self.general1DarkModeLabel.setBuddy(self.general1DarkModeCheck)
        self.statusFailedLabel.setBuddy(self.statusFailedButton)
        self.statusCurrentLabel.setBuddy(self.statusCurrentButton)
        self.statusSelectedLabel.setBuddy(self.statusSelectedButton)
        self.statusSuccessLabel.setBuddy(self.statusSuccessButton)
        self.statusUpcomingLabel.setBuddy(self.statusUpcomingButton)
        self.statusForceFailedLabel.setBuddy(self.statusForceFailedButton)
#endif // QT_CONFIG(shortcut)

        self.retranslateUi(optionsWindow)
        self.buttonBox.accepted.connect(optionsWindow.accept)
        self.buttonBox.rejected.connect(optionsWindow.reject)

        QMetaObject.connectSlotsByName(optionsWindow)
    # setupUi

    def retranslateUi(self, optionsWindow):
        optionsWindow.setWindowTitle(QCoreApplication.translate("optionsWindow", u"Dialog", None))
        self.generalLabel.setText(QCoreApplication.translate("optionsWindow", u"General Options", None))
        self.general2RandomizeOrderLabel.setText(QCoreApplication.translate("optionsWindow", u"Randomize Order Open on Startup", None))
        self.general1DarkModeLabel.setText(QCoreApplication.translate("optionsWindow", u"Dark Mode", None))
        self.statusColorLabel.setText(QCoreApplication.translate("optionsWindow", u"Status Color Options", None))
        self.statusSelectedButton.setText(QCoreApplication.translate("optionsWindow", u"...", None))
        self.statusFailedLabel.setText(QCoreApplication.translate("optionsWindow", u"Failure", None))
        self.statusFailedButton.setText(QCoreApplication.translate("optionsWindow", u"...", None))
        self.statusCurrentLabel.setText(QCoreApplication.translate("optionsWindow", u"Current", None))
        self.statusForceFailedButton.setText(QCoreApplication.translate("optionsWindow", u"...", None))
        self.statusSelectedLabel.setText(QCoreApplication.translate("optionsWindow", u"Selected", None))
        self.statusSuccessLabel.setText(QCoreApplication.translate("optionsWindow", u"Successful", None))
        self.statusUpcomingLabel.setText(QCoreApplication.translate("optionsWindow", u"Upcoming", None))
        self.statusSuccessButton.setText(QCoreApplication.translate("optionsWindow", u"...", None))
        self.statusForceFailedLabel.setText(QCoreApplication.translate("optionsWindow", u"Force Failed", None))
        self.statusCurrentButton.setText(QCoreApplication.translate("optionsWindow", u"...", None))
        self.statusUpcomingButton.setText(QCoreApplication.translate("optionsWindow", u"...", None))
    # retranslateUi

