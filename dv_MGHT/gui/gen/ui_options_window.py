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

class Ui_OptionsWindow(object):
    def setupUi(self, OptionsWindow):
        if not OptionsWindow.objectName():
            OptionsWindow.setObjectName(u"OptionsWindow")
        OptionsWindow.resize(362, 400)
        OptionsWindow.setStyleSheet(u"QLabel {\n"
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
        self.windowLayout = QVBoxLayout(OptionsWindow)
        self.windowLayout.setObjectName(u"windowLayout")
        self.mainLayoutWidget = QVBoxLayout()
        self.mainLayoutWidget.setObjectName(u"mainLayoutWidget")
        self.optionsScroll = QScrollArea(OptionsWindow)
        self.optionsScroll.setObjectName(u"optionsScroll")
        self.optionsScroll.setFrameShape(QFrame.Shape.NoFrame)
        self.optionsScroll.setWidgetResizable(True)
        self.optionsWidget = QWidget()
        self.optionsWidget.setObjectName(u"optionsWidget")
        self.optionsWidget.setGeometry(QRect(0, -34, 330, 390))
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
        self.statusForceFailedLabel = QLabel(self.optionsWidget)
        self.statusForceFailedLabel.setObjectName(u"statusForceFailedLabel")

        self.statusColorGrid.addWidget(self.statusForceFailedLabel, 5, 0, 1, 1)

        self.statusSelectedLabel = QLabel(self.optionsWidget)
        self.statusSelectedLabel.setObjectName(u"statusSelectedLabel")

        self.statusColorGrid.addWidget(self.statusSelectedLabel, 1, 0, 1, 1)

        self.statusUpcomingLabel = QLabel(self.optionsWidget)
        self.statusUpcomingLabel.setObjectName(u"statusUpcomingLabel")

        self.statusColorGrid.addWidget(self.statusUpcomingLabel, 0, 0, 1, 1)

        self.statusCurrentLabel = QLabel(self.optionsWidget)
        self.statusCurrentLabel.setObjectName(u"statusCurrentLabel")

        self.statusColorGrid.addWidget(self.statusCurrentLabel, 2, 0, 1, 1)

        self.statusCurrentButton = QToolButton(self.optionsWidget)
        self.statusCurrentButton.setObjectName(u"statusCurrentButton")
        self.statusCurrentButton.setText(u"...")

        self.statusColorGrid.addWidget(self.statusCurrentButton, 2, 2, 1, 1)

        self.statusForceFailedButton = QToolButton(self.optionsWidget)
        self.statusForceFailedButton.setObjectName(u"statusForceFailedButton")
        self.statusForceFailedButton.setText(u"...")

        self.statusColorGrid.addWidget(self.statusForceFailedButton, 5, 2, 1, 1)

        self.statusFailedLabel = QLabel(self.optionsWidget)
        self.statusFailedLabel.setObjectName(u"statusFailedLabel")

        self.statusColorGrid.addWidget(self.statusFailedLabel, 4, 0, 1, 1)

        self.statusFailedButton = QToolButton(self.optionsWidget)
        self.statusFailedButton.setObjectName(u"statusFailedButton")

        self.statusColorGrid.addWidget(self.statusFailedButton, 4, 2, 1, 1)

        self.statusSuccessButton = QToolButton(self.optionsWidget)
        self.statusSuccessButton.setObjectName(u"statusSuccessButton")
        self.statusSuccessButton.setText(u"...")

        self.statusColorGrid.addWidget(self.statusSuccessButton, 3, 2, 1, 1)

        self.statusUpcomingButton = QToolButton(self.optionsWidget)
        self.statusUpcomingButton.setObjectName(u"statusUpcomingButton")
        self.statusUpcomingButton.setText(u"...")

        self.statusColorGrid.addWidget(self.statusUpcomingButton, 0, 2, 1, 1)

        self.statusSelectedButton = QToolButton(self.optionsWidget)
        self.statusSelectedButton.setObjectName(u"statusSelectedButton")
        self.statusSelectedButton.setText(u"...")

        self.statusColorGrid.addWidget(self.statusSelectedButton, 1, 2, 1, 1)

        self.statusSuccessLabel = QLabel(self.optionsWidget)
        self.statusSuccessLabel.setObjectName(u"statusSuccessLabel")

        self.statusColorGrid.addWidget(self.statusSuccessLabel, 3, 0, 1, 1)

        self.statusUpcomingRevert = QToolButton(self.optionsWidget)
        self.statusUpcomingRevert.setObjectName(u"statusUpcomingRevert")
        icon = QIcon(QIcon.fromTheme(QIcon.ThemeIcon.DocumentRevert))
        self.statusUpcomingRevert.setIcon(icon)

        self.statusColorGrid.addWidget(self.statusUpcomingRevert, 0, 1, 1, 1)

        self.statusSelectedRevert = QToolButton(self.optionsWidget)
        self.statusSelectedRevert.setObjectName(u"statusSelectedRevert")
        self.statusSelectedRevert.setIcon(icon)

        self.statusColorGrid.addWidget(self.statusSelectedRevert, 1, 1, 1, 1)

        self.statusCurrentRevert = QToolButton(self.optionsWidget)
        self.statusCurrentRevert.setObjectName(u"statusCurrentRevert")
        self.statusCurrentRevert.setIcon(icon)

        self.statusColorGrid.addWidget(self.statusCurrentRevert, 2, 1, 1, 1)

        self.statusSuccessRevert = QToolButton(self.optionsWidget)
        self.statusSuccessRevert.setObjectName(u"statusSuccessRevert")
        self.statusSuccessRevert.setIcon(icon)

        self.statusColorGrid.addWidget(self.statusSuccessRevert, 3, 1, 1, 1)

        self.statusFailedRevert = QToolButton(self.optionsWidget)
        self.statusFailedRevert.setObjectName(u"statusFailedRevert")
        self.statusFailedRevert.setIcon(icon)

        self.statusColorGrid.addWidget(self.statusFailedRevert, 4, 1, 1, 1)

        self.statusForceFailedRevert = QToolButton(self.optionsWidget)
        self.statusForceFailedRevert.setObjectName(u"statusForceFailedRevert")
        self.statusForceFailedRevert.setIcon(icon)

        self.statusColorGrid.addWidget(self.statusForceFailedRevert, 5, 1, 1, 1)

        self.statusColorGrid.setColumnStretch(0, 1)

        self.statusColorLayout.addLayout(self.statusColorGrid)


        self.optionsLayout.addLayout(self.statusColorLayout)

        self.hotkeyLayout = QVBoxLayout()
        self.hotkeyLayout.setObjectName(u"hotkeyLayout")
        self.hotkeyLabel = QLabel(self.optionsWidget)
        self.hotkeyLabel.setObjectName(u"hotkeyLabel")
        self.hotkeyLabel.setProperty(u"sectionHeader", 1)

        self.hotkeyLayout.addWidget(self.hotkeyLabel)

        self.hotkeyGrid = QGridLayout()
        self.hotkeyGrid.setObjectName(u"hotkeyGrid")
        self.hotkeyGlobalLabel = QLabel(self.optionsWidget)
        self.hotkeyGlobalLabel.setObjectName(u"hotkeyGlobalLabel")

        self.hotkeyGrid.addWidget(self.hotkeyGlobalLabel, 0, 0, 1, 1)

        self.checkBox = QCheckBox(self.optionsWidget)
        self.checkBox.setObjectName(u"checkBox")

        self.hotkeyGrid.addWidget(self.checkBox, 0, 1, 1, 1)

        self.hotkeyGrid.setColumnStretch(0, 1)

        self.hotkeyLayout.addLayout(self.hotkeyGrid)


        self.optionsLayout.addLayout(self.hotkeyLayout)

        self.optionsScroll.setWidget(self.optionsWidget)

        self.mainLayoutWidget.addWidget(self.optionsScroll)


        self.windowLayout.addLayout(self.mainLayoutWidget)

        self.buttonBox = QDialogButtonBox(OptionsWindow)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setStandardButtons(QDialogButtonBox.StandardButton.Save)

        self.windowLayout.addWidget(self.buttonBox)

#if QT_CONFIG(shortcut)
        self.general2RandomizeOrderLabel.setBuddy(self.general2RandomizeOrderCheck)
        self.general1DarkModeLabel.setBuddy(self.general1DarkModeCheck)
        self.statusForceFailedLabel.setBuddy(self.statusForceFailedButton)
        self.statusSelectedLabel.setBuddy(self.statusSelectedButton)
        self.statusUpcomingLabel.setBuddy(self.statusUpcomingButton)
        self.statusCurrentLabel.setBuddy(self.statusCurrentButton)
        self.statusFailedLabel.setBuddy(self.statusFailedButton)
        self.statusSuccessLabel.setBuddy(self.statusSuccessButton)
#endif // QT_CONFIG(shortcut)

        self.retranslateUi(OptionsWindow)
        self.buttonBox.accepted.connect(OptionsWindow.accept)
        self.buttonBox.rejected.connect(OptionsWindow.reject)

        QMetaObject.connectSlotsByName(OptionsWindow)
    # setupUi

    def retranslateUi(self, OptionsWindow):
        OptionsWindow.setWindowTitle(QCoreApplication.translate("OptionsWindow", u"Dialog", None))
        self.generalLabel.setText(QCoreApplication.translate("OptionsWindow", u"General Options", None))
        self.general2RandomizeOrderLabel.setText(QCoreApplication.translate("OptionsWindow", u"Randomize Order Open on Startup", None))
        self.general1DarkModeLabel.setText(QCoreApplication.translate("OptionsWindow", u"Dark Mode", None))
        self.statusColorLabel.setText(QCoreApplication.translate("OptionsWindow", u"Status Color Options", None))
        self.statusForceFailedLabel.setText(QCoreApplication.translate("OptionsWindow", u"Force Failed", None))
        self.statusSelectedLabel.setText(QCoreApplication.translate("OptionsWindow", u"Selected", None))
        self.statusUpcomingLabel.setText(QCoreApplication.translate("OptionsWindow", u"Upcoming", None))
        self.statusCurrentLabel.setText(QCoreApplication.translate("OptionsWindow", u"Current", None))
        self.statusFailedLabel.setText(QCoreApplication.translate("OptionsWindow", u"Failure", None))
        self.statusFailedButton.setText(QCoreApplication.translate("OptionsWindow", u"...", None))
        self.statusSuccessLabel.setText(QCoreApplication.translate("OptionsWindow", u"Successful", None))
        self.statusUpcomingRevert.setText(QCoreApplication.translate("OptionsWindow", u"Reset", None))
        self.statusSelectedRevert.setText(QCoreApplication.translate("OptionsWindow", u"Reset", None))
        self.statusCurrentRevert.setText(QCoreApplication.translate("OptionsWindow", u"Reset", None))
        self.statusSuccessRevert.setText(QCoreApplication.translate("OptionsWindow", u"Reset", None))
        self.statusFailedRevert.setText(QCoreApplication.translate("OptionsWindow", u"Reset", None))
        self.statusForceFailedRevert.setText(QCoreApplication.translate("OptionsWindow", u"Reset", None))
#if QT_CONFIG(tooltip)
        self.hotkeyLabel.setToolTip(QCoreApplication.translate("OptionsWindow", u"Hotkey Options\n"
"(Only takes effect after application restart)", None))
#endif // QT_CONFIG(tooltip)
        self.hotkeyLabel.setText(QCoreApplication.translate("OptionsWindow", u"Hotkey Options*", None))
#if QT_CONFIG(tooltip)
        self.hotkeyGlobalLabel.setToolTip(QCoreApplication.translate("OptionsWindow", u"Enable Global Hotkeys\n"
"(Only takes effect after application restart)\n"
"(Only where applicable)", None))
#endif // QT_CONFIG(tooltip)
        self.hotkeyGlobalLabel.setText(QCoreApplication.translate("OptionsWindow", u"Enable Global Hotkeys*", None))
    # retranslateUi

