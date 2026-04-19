# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'login2.ui'
##
## Created by: Qt User Interface Compiler version 6.10.2
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
from PySide6.QtWidgets import (QApplication, QComboBox, QDialog, QFrame,
    QLabel, QPushButton, QSizePolicy, QSpacerItem,
    QVBoxLayout, QWidget)

class Ui_LoginWindow(object):
    def setupUi(self, LoginWindow):
        if not LoginWindow.objectName():
            LoginWindow.setObjectName(u"LoginWindow")
        LoginWindow.resize(480, 520)
        LoginWindow.setStyleSheet(u"QDialog {\n"
"    background-color: #0f1117;\n"
"}\n"
"QFrame#cardFrame {\n"
"    background-color: #1a1d27;\n"
"    border: 1px solid #2a2d3a;\n"
"    border-radius: 16px;\n"
"}\n"
"QLabel#labelTitle {\n"
"    color: #ffffff;\n"
"    font-size: 22px;\n"
"    font-weight: 700;\n"
"    letter-spacing: 1px;\n"
"}\n"
"QLabel#labelSubtitle {\n"
"    color: #6b7280;\n"
"    font-size: 12px;\n"
"    letter-spacing: 2px;\n"
"}\n"
"QFrame#divider {\n"
"    background-color: #00c8ff;\n"
"    border: none;\n"
"    max-height: 2px;\n"
"    border-radius: 1px;\n"
"}\n"
"QLabel#labelRole {\n"
"    color: #9ca3af;\n"
"    font-size: 11px;\n"
"    font-weight: 600;\n"
"    letter-spacing: 1px;\n"
"}\n"
"QLabel#labelIcon {\n"
"    font-size: 32px;\n"
"    color: #ffffff;\n"
"}\n"
"QComboBox#comboBoxRole {\n"
"    background-color: #0f1117;\n"
"    color: #e5e7eb;\n"
"    border: 1px solid #2a2d3a;\n"
"    border-radius: 8px;\n"
"    padding: 10px 16px;\n"
"    font-size: 14px;\n"
"    min-height: 20px;\n"
"}\n"
"QComboBox#com"
                        "boBoxRole:hover {\n"
"    border: 1px solid #00c8ff;\n"
"}\n"
"QComboBox#comboBoxRole:focus {\n"
"    border: 1px solid #00c8ff;\n"
"}\n"
"QComboBox#comboBoxRole::drop-down {\n"
"    subcontrol-origin: padding;\n"
"    subcontrol-position: top right;\n"
"    width: 36px;\n"
"    border-left: 1px solid #2a2d3a;\n"
"    border-top-right-radius: 8px;\n"
"    border-bottom-right-radius: 8px;\n"
"}\n"
"QComboBox QAbstractItemView {\n"
"    background-color: #1a1d27;\n"
"    color: #e5e7eb;\n"
"    border: 1px solid #2a2d3a;\n"
"    selection-background-color: #003a47;\n"
"    selection-color: #00c8ff;\n"
"    padding: 4px;\n"
"    outline: 0;\n"
"}\n"
"QPushButton#pushButtonLogin {\n"
"    background-color: #00c8ff;\n"
"    color: #0f1117;\n"
"    border: none;\n"
"    border-radius: 8px;\n"
"    padding: 12px 0px;\n"
"    font-size: 14px;\n"
"    font-weight: 700;\n"
"    letter-spacing: 1px;\n"
"    min-height: 20px;\n"
"}\n"
"QPushButton#pushButtonLogin:hover {\n"
"    background-color: #33d4ff;\n"
"}\n"
"QPushB"
                        "utton#pushButtonLogin:pressed {\n"
"    background-color: #0099cc;\n"
"}\n"
"QLabel#labelFooter {\n"
"    color: #374151;\n"
"    font-size: 10px;\n"
"    letter-spacing: 1px;\n"
"}")
        self.outerLayout = QVBoxLayout(LoginWindow)
        self.outerLayout.setSpacing(0)
        self.outerLayout.setObjectName(u"outerLayout")
        self.outerLayout.setContentsMargins(60, 50, 60, 50)
        self.cardFrame = QFrame(LoginWindow)
        self.cardFrame.setObjectName(u"cardFrame")
        self.cardFrame.setFrameShape(QFrame.Shape.StyledPanel)
        self.cardFrame.setFrameShadow(QFrame.Shadow.Raised)
        self.cardLayout = QVBoxLayout(self.cardFrame)
        self.cardLayout.setSpacing(0)
        self.cardLayout.setObjectName(u"cardLayout")
        self.cardLayout.setContentsMargins(36, 36, 36, 36)
        self.labelIcon = QLabel(self.cardFrame)
        self.labelIcon.setObjectName(u"labelIcon")
        self.labelIcon.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.cardLayout.addWidget(self.labelIcon)

        self.sp1 = QSpacerItem(0, 10, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.cardLayout.addItem(self.sp1)

        self.labelTitle = QLabel(self.cardFrame)
        self.labelTitle.setObjectName(u"labelTitle")
        self.labelTitle.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.cardLayout.addWidget(self.labelTitle)

        self.sp2 = QSpacerItem(0, 6, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.cardLayout.addItem(self.sp2)

        self.labelSubtitle = QLabel(self.cardFrame)
        self.labelSubtitle.setObjectName(u"labelSubtitle")
        self.labelSubtitle.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.cardLayout.addWidget(self.labelSubtitle)

        self.sp3 = QSpacerItem(0, 18, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.cardLayout.addItem(self.sp3)

        self.divider = QFrame(self.cardFrame)
        self.divider.setObjectName(u"divider")
        self.divider.setFrameShape(QFrame.Shape.HLine)
        self.divider.setFrameShadow(QFrame.Shadow.Plain)

        self.cardLayout.addWidget(self.divider)

        self.sp4 = QSpacerItem(0, 24, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.cardLayout.addItem(self.sp4)

        self.labelRole = QLabel(self.cardFrame)
        self.labelRole.setObjectName(u"labelRole")

        self.cardLayout.addWidget(self.labelRole)

        self.sp5 = QSpacerItem(0, 8, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.cardLayout.addItem(self.sp5)

        self.userbox = QComboBox(self.cardFrame)
        self.userbox.addItem("")
        self.userbox.addItem("")
        self.userbox.setObjectName(u"userbox")

        self.cardLayout.addWidget(self.userbox)

        self.sp6 = QSpacerItem(0, 20, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.cardLayout.addItem(self.sp6)

        self.login_btn = QPushButton(self.cardFrame)
        self.login_btn.setObjectName(u"login_btn")
        self.login_btn.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.cardLayout.addWidget(self.login_btn)

        self.sp7 = QSpacerItem(0, 18, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.cardLayout.addItem(self.sp7)

        self.labelFooter = QLabel(self.cardFrame)
        self.labelFooter.setObjectName(u"labelFooter")
        self.labelFooter.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.cardLayout.addWidget(self.labelFooter)


        self.outerLayout.addWidget(self.cardFrame)


        self.retranslateUi(LoginWindow)

        QMetaObject.connectSlotsByName(LoginWindow)
    # setupUi

    def retranslateUi(self, LoginWindow):
        LoginWindow.setWindowTitle(QCoreApplication.translate("LoginWindow", u"NAUTIX GUI", None))
        self.labelIcon.setText(QCoreApplication.translate("LoginWindow", u"\u2693", None))
        self.labelTitle.setText(QCoreApplication.translate("LoginWindow", u"NAUTIX GUI", None))
        self.labelSubtitle.setText(QCoreApplication.translate("LoginWindow", u"ROV CONTROL SYSTEM", None))
        self.labelRole.setText(QCoreApplication.translate("LoginWindow", u"SELECT ROLE", None))
        self.userbox.setItemText(0, QCoreApplication.translate("LoginWindow", u"Pilot", None))
        self.userbox.setItemText(1, QCoreApplication.translate("LoginWindow", u"Copilot", None))

        self.login_btn.setText(QCoreApplication.translate("LoginWindow", u"LOGIN", None))
        self.labelFooter.setText(QCoreApplication.translate("LoginWindow", u"NAUTIX v1.0  \u00b7  AUTHORIZED ACCESS ONLY", None))
    # retranslateUi

