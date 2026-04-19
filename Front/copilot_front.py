# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'copilot.ui'
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
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QLCDNumber,
    QLabel, QMainWindow, QPushButton, QSizePolicy,
    QSpacerItem, QStatusBar, QVBoxLayout, QWidget)

from Front.circularprogress import CircularProgress
import resources_rc

class Ui_CoPilot_Window(object):
    def setupUi(self, CoPilot_Window):
        if not CoPilot_Window.objectName():
            CoPilot_Window.setObjectName(u"CoPilot_Window")
        CoPilot_Window.resize(1128, 800)
        CoPilot_Window.setStyleSheet(u"QMainWindow {\n"
"    background-color: #0f1117;\n"
"}\n"
"\n"
"QFrame#frame {\n"
"    background-color: #1a1d27;\n"
"    border: 1px solid #2a2d3a;\n"
"    border-radius: 14px;\n"
"}\n"
"\n"
"/* Labels */\n"
"QLabel {\n"
"    color: #e5e7eb;\n"
"    font-size: 13px;\n"
"}\n"
"\n"
"QLabel#prim_feed_label {\n"
"    color: #9ca3af;\n"
"    font-weight: 600;\n"
"}\n"
"\n"
"QLabel#Stabilizer_label {\n"
"    background-color: #00c8ff;\n"
"    color: #0f1117;\n"
"    font-weight: bold;\n"
"    border-radius: 8px;\n"
"}\n"
"\n"
"/* ComboBox */\n"
"QComboBox {\n"
"    background-color: #0f1117;\n"
"    color: #e5e7eb;\n"
"    border: 1px solid #2a2d3a;\n"
"    border-radius: 8px;\n"
"    padding: 6px 10px;\n"
"}\n"
"\n"
"QComboBox:hover {\n"
"    border: 1px solid #00c8ff;\n"
"}\n"
"\n"
"QComboBox QAbstractItemView {\n"
"    background-color: #1a1d27;\n"
"    color: #e5e7eb;\n"
"    selection-background-color: #003a47;\n"
"    selection-color: #00c8ff;\n"
"}\n"
"\n"
"QComboBox::drop-down {\n"
"    width: 36px;\n"
"}\n"
""
                        "\n"
"/* Buttons */\n"
"QPushButton {\n"
"    background-color: #00c8ff;\n"
"    color: #0f1117;\n"
"    border-radius: 8px;\n"
"    padding: 6px 10px;\n"
"    font-weight: 600;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #33d4ff;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #0099cc;\n"
"}\n"
"\n"
"/* LCD */\n"
"QLCDNumber {\n"
"    background-color: #0f1117;\n"
"    color: #00c8ff;\n"
"    border: 1px solid #2a2d3a;\n"
"    border-radius: 8px;\n"
"}\n"
"\n"
"/* Frames inside UI */\n"
"QFrame {\n"
"    background-color: transparent;\n"
"}")
        self.centralwidget = QWidget(CoPilot_Window)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_8 = QVBoxLayout()
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.horizontalLayout_12 = QHBoxLayout()
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.horizontalSpacer_7 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_12.addItem(self.horizontalSpacer_7)

        self.prim_feed_label = QLabel(self.centralwidget)
        self.prim_feed_label.setObjectName(u"prim_feed_label")

        self.horizontalLayout_12.addWidget(self.prim_feed_label)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.cambtn1 = QPushButton(self.centralwidget)
        self.cambtn1.setObjectName(u"cambtn1")

        self.horizontalLayout_3.addWidget(self.cambtn1)

        self.cambtn2 = QPushButton(self.centralwidget)
        self.cambtn2.setObjectName(u"cambtn2")

        self.horizontalLayout_3.addWidget(self.cambtn2)

        self.cambtn3 = QPushButton(self.centralwidget)
        self.cambtn3.setObjectName(u"cambtn3")

        self.horizontalLayout_3.addWidget(self.cambtn3)

        self.cambtn4 = QPushButton(self.centralwidget)
        self.cambtn4.setObjectName(u"cambtn4")

        self.horizontalLayout_3.addWidget(self.cambtn4)


        self.horizontalLayout_12.addLayout(self.horizontalLayout_3)

        self.horizontalSpacer_8 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_12.addItem(self.horizontalSpacer_8)


        self.verticalLayout_8.addLayout(self.horizontalLayout_12)

        self.Camera = QLabel(self.centralwidget)
        self.Camera.setObjectName(u"Camera")
        self.Camera.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_8.addWidget(self.Camera)

        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy)
        self.frame.setMaximumSize(QSize(16777215, 150))
        self.frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.label = QLabel(self.frame)
        self.label.setObjectName(u"label")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy1)
        self.label.setMaximumSize(QSize(50, 50))
        self.label.setPixmap(QPixmap(u":/Front/icons/circle.png"))
        self.label.setScaledContents(True)

        self.horizontalLayout_4.addWidget(self.label)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer)

        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.thrustup_label = QLabel(self.frame)
        self.thrustup_label.setObjectName(u"thrustup_label")
        sizePolicy1.setHeightForWidth(self.thrustup_label.sizePolicy().hasHeightForWidth())
        self.thrustup_label.setSizePolicy(sizePolicy1)
        self.thrustup_label.setMinimumSize(QSize(60, 50))
        self.thrustup_label.setMaximumSize(QSize(60, 50))
        self.thrustup_label.setPixmap(QPixmap(u":/Front/icons/light_green.png"))
        self.thrustup_label.setScaledContents(True)

        self.verticalLayout_4.addWidget(self.thrustup_label)

        self.frame_4 = QFrame(self.frame)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setFrameShape(QFrame.Shape.HLine)
        self.frame_4.setFrameShadow(QFrame.Shadow.Raised)

        self.verticalLayout_4.addWidget(self.frame_4)

        self.thrustdown_label = QLabel(self.frame)
        self.thrustdown_label.setObjectName(u"thrustdown_label")
        sizePolicy1.setHeightForWidth(self.thrustdown_label.sizePolicy().hasHeightForWidth())
        self.thrustdown_label.setSizePolicy(sizePolicy1)
        self.thrustdown_label.setMinimumSize(QSize(60, 50))
        self.thrustdown_label.setMaximumSize(QSize(60, 50))
        self.thrustdown_label.setPixmap(QPixmap(u":/Front/icons/light_red.png"))
        self.thrustdown_label.setScaledContents(True)

        self.verticalLayout_4.addWidget(self.thrustdown_label)


        self.horizontalLayout_4.addLayout(self.verticalLayout_4)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_2)

        self.verticalLayout_6 = QVBoxLayout()
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.acw_label = QLabel(self.frame)
        self.acw_label.setObjectName(u"acw_label")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Maximum, QSizePolicy.Policy.Maximum)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.acw_label.sizePolicy().hasHeightForWidth())
        self.acw_label.setSizePolicy(sizePolicy2)
        self.acw_label.setMaximumSize(QSize(100, 100))
        self.acw_label.setPixmap(QPixmap(u":/Front/icons/acw_arrow.png"))
        self.acw_label.setScaledContents(True)

        self.verticalLayout_6.addWidget(self.acw_label)

        self.cw_label = QLabel(self.frame)
        self.cw_label.setObjectName(u"cw_label")
        sizePolicy2.setHeightForWidth(self.cw_label.sizePolicy().hasHeightForWidth())
        self.cw_label.setSizePolicy(sizePolicy2)
        self.cw_label.setMaximumSize(QSize(100, 100))
        self.cw_label.setPixmap(QPixmap(u":/Front/icons/cw_arrow.png"))
        self.cw_label.setScaledContents(True)

        self.verticalLayout_6.addWidget(self.cw_label)


        self.horizontalLayout_4.addLayout(self.verticalLayout_6)

        self.horizontalSpacer_9 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_9)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.Hgripper_label = QLabel(self.frame)
        self.Hgripper_label.setObjectName(u"Hgripper_label")
        sizePolicy1.setHeightForWidth(self.Hgripper_label.sizePolicy().hasHeightForWidth())
        self.Hgripper_label.setSizePolicy(sizePolicy1)
        self.Hgripper_label.setMinimumSize(QSize(70, 70))
        self.Hgripper_label.setMaximumSize(QSize(70, 70))
        self.Hgripper_label.setStyleSheet(u"")
        self.Hgripper_label.setPixmap(QPixmap(u":/Front/icons/open_Hgripper.png"))
        self.Hgripper_label.setScaledContents(True)

        self.horizontalLayout_5.addWidget(self.Hgripper_label)

        self.Vgripper_label = QLabel(self.frame)
        self.Vgripper_label.setObjectName(u"Vgripper_label")
        sizePolicy1.setHeightForWidth(self.Vgripper_label.sizePolicy().hasHeightForWidth())
        self.Vgripper_label.setSizePolicy(sizePolicy1)
        self.Vgripper_label.setMinimumSize(QSize(70, 70))
        self.Vgripper_label.setMaximumSize(QSize(70, 70))
        self.Vgripper_label.setPixmap(QPixmap(u":/Front/icons/open_Vgripper.png"))
        self.Vgripper_label.setScaledContents(True)

        self.horizontalLayout_5.addWidget(self.Vgripper_label)


        self.horizontalLayout_4.addLayout(self.horizontalLayout_5)

        self.horizontalSpacer_10 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_10)

        self.Speed_bar = CircularProgress(self.frame)
        self.Speed_bar.setObjectName(u"Speed_bar")
        sizePolicy2.setHeightForWidth(self.Speed_bar.sizePolicy().hasHeightForWidth())
        self.Speed_bar.setSizePolicy(sizePolicy2)
        self.Speed_bar.setMinimumSize(QSize(100, 100))
        self.Speed_bar.setMaximumSize(QSize(100, 100))
        self.label_9 = QLabel(self.Speed_bar)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setGeometry(QRect(0, 10, 91, 41))
        font = QFont()
        font.setBold(True)
        self.label_9.setFont(font)
        self.label_9.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_4.addWidget(self.Speed_bar)

        self.horizontalSpacer_11 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_11)

        self.Gain_bar = CircularProgress(self.frame)
        self.Gain_bar.setObjectName(u"Gain_bar")
        sizePolicy2.setHeightForWidth(self.Gain_bar.sizePolicy().hasHeightForWidth())
        self.Gain_bar.setSizePolicy(sizePolicy2)
        self.Gain_bar.setMinimumSize(QSize(100, 100))
        self.Gain_bar.setMaximumSize(QSize(100, 100))
        self.Gain_bar.setStyleSheet(u"background-color: transparent;")
        self.label_13 = QLabel(self.Gain_bar)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setGeometry(QRect(0, 10, 91, 41))
        self.label_13.setFont(font)
        self.label_13.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_4.addWidget(self.Gain_bar)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_3)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.lcdNumber = QLCDNumber(self.frame)
        self.lcdNumber.setObjectName(u"lcdNumber")
        self.lcdNumber.setDigitCount(5)

        self.verticalLayout_2.addWidget(self.lcdNumber)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.start_btn = QPushButton(self.frame)
        self.start_btn.setObjectName(u"start_btn")

        self.horizontalLayout_2.addWidget(self.start_btn)

        self.pausebtn = QPushButton(self.frame)
        self.pausebtn.setObjectName(u"pausebtn")

        self.horizontalLayout_2.addWidget(self.pausebtn)

        self.reset_btn = QPushButton(self.frame)
        self.reset_btn.setObjectName(u"reset_btn")

        self.horizontalLayout_2.addWidget(self.reset_btn)


        self.verticalLayout_2.addLayout(self.horizontalLayout_2)

        self.verticalLayout_2.setStretch(0, 2)
        self.verticalLayout_2.setStretch(1, 1)

        self.horizontalLayout_4.addLayout(self.verticalLayout_2)

        self.horizontalSpacer_12 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_12)

        self.Stabilizer_label = QLabel(self.frame)
        self.Stabilizer_label.setObjectName(u"Stabilizer_label")
        sizePolicy.setHeightForWidth(self.Stabilizer_label.sizePolicy().hasHeightForWidth())
        self.Stabilizer_label.setSizePolicy(sizePolicy)
        self.Stabilizer_label.setMinimumSize(QSize(0, 0))
        self.Stabilizer_label.setMaximumSize(QSize(16777215, 50))
        self.Stabilizer_label.setFont(font)
        self.Stabilizer_label.setStyleSheet(u"background-color: rgb(255, 0, 0);")
        self.Stabilizer_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_4.addWidget(self.Stabilizer_label)


        self.horizontalLayout.addLayout(self.horizontalLayout_4)


        self.verticalLayout_8.addWidget(self.frame)

        self.verticalLayout_8.setStretch(1, 6)

        self.verticalLayout_3.addLayout(self.verticalLayout_8)

        self.verticalLayout_3.setStretch(0, 3)

        self.verticalLayout.addLayout(self.verticalLayout_3)

        CoPilot_Window.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(CoPilot_Window)
        self.statusbar.setObjectName(u"statusbar")
        CoPilot_Window.setStatusBar(self.statusbar)

        self.retranslateUi(CoPilot_Window)

        QMetaObject.connectSlotsByName(CoPilot_Window)
    # setupUi

    def retranslateUi(self, CoPilot_Window):
        CoPilot_Window.setWindowTitle(QCoreApplication.translate("CoPilot_Window", u"MainWindow", None))
        self.prim_feed_label.setText(QCoreApplication.translate("CoPilot_Window", u"Primary Feed:", None))
        self.cambtn1.setText(QCoreApplication.translate("CoPilot_Window", u"1", None))
        self.cambtn2.setText(QCoreApplication.translate("CoPilot_Window", u"2", None))
        self.cambtn3.setText(QCoreApplication.translate("CoPilot_Window", u"3", None))
        self.cambtn4.setText(QCoreApplication.translate("CoPilot_Window", u"4", None))
        self.Camera.setText(QCoreApplication.translate("CoPilot_Window", u"Cam 1", None))
        self.label.setText("")
        self.thrustup_label.setText("")
        self.thrustdown_label.setText("")
        self.acw_label.setText("")
        self.cw_label.setText("")
        self.Hgripper_label.setText("")
        self.Vgripper_label.setText("")
        self.label_9.setText(QCoreApplication.translate("CoPilot_Window", u"Speed", None))
        self.label_13.setText(QCoreApplication.translate("CoPilot_Window", u"Gain", None))
        self.start_btn.setText(QCoreApplication.translate("CoPilot_Window", u"Start", None))
        self.pausebtn.setText(QCoreApplication.translate("CoPilot_Window", u"Pause", None))
        self.reset_btn.setText(QCoreApplication.translate("CoPilot_Window", u"Reset", None))
        self.Stabilizer_label.setText(QCoreApplication.translate("CoPilot_Window", u"Stabilizer", None))
    # retranslateUi

