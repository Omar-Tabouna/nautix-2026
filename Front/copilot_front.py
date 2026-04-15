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
from PySide6.QtWidgets import (QApplication, QComboBox, QFrame, QHBoxLayout,
    QLCDNumber, QLabel, QMainWindow, QPushButton,
    QSizePolicy, QSpacerItem, QStatusBar, QVBoxLayout,
    QWidget)

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
        self.verticalLayout_4 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
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

        self.comboBox_4 = QComboBox(self.centralwidget)
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.comboBox_4.setObjectName(u"comboBox_4")

        self.horizontalLayout_12.addWidget(self.comboBox_4)

        self.horizontalSpacer_8 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_12.addItem(self.horizontalSpacer_8)


        self.verticalLayout_8.addLayout(self.horizontalLayout_12)

        self.Camera = QLabel(self.centralwidget)
        self.Camera.setObjectName(u"Camera")
        self.Camera.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_8.addWidget(self.Camera)

        self.verticalLayout_8.setStretch(1, 6)

        self.verticalLayout_3.addLayout(self.verticalLayout_8)

        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy)
        self.frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QFrame.Shadow.Raised)
        self.widget_3 = QWidget(self.frame)
        self.widget_3.setObjectName(u"widget_3")
        self.widget_3.setGeometry(QRect(20, 60, 71, 71))
        self.outercircle_label = QLabel(self.widget_3)
        self.outercircle_label.setObjectName(u"outercircle_label")
        self.outercircle_label.setGeometry(QRect(10, 10, 50, 50))
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.outercircle_label.sizePolicy().hasHeightForWidth())
        self.outercircle_label.setSizePolicy(sizePolicy1)
        self.outercircle_label.setMaximumSize(QSize(50, 50))
        self.outercircle_label.setPixmap(QPixmap(u":/Front/icons/circle.png"))
        self.outercircle_label.setScaledContents(True)
        self.innercircle_label = QLabel(self.widget_3)
        self.innercircle_label.setObjectName(u"innercircle_label")
        self.innercircle_label.setGeometry(QRect(20, 20, 30, 30))
        sizePolicy1.setHeightForWidth(self.innercircle_label.sizePolicy().hasHeightForWidth())
        self.innercircle_label.setSizePolicy(sizePolicy1)
        self.innercircle_label.setMaximumSize(QSize(200, 200))
        self.innercircle_label.setPixmap(QPixmap(u":/Front/icons/circle2.png"))
        self.innercircle_label.setScaledContents(True)
        self.layoutWidget = QWidget(self.frame)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(90, 30, 61, 142))
        self.verticalLayout = QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.thrustup_label = QLabel(self.layoutWidget)
        self.thrustup_label.setObjectName(u"thrustup_label")
        sizePolicy1.setHeightForWidth(self.thrustup_label.sizePolicy().hasHeightForWidth())
        self.thrustup_label.setSizePolicy(sizePolicy1)
        self.thrustup_label.setMinimumSize(QSize(59, 59))
        self.thrustup_label.setMaximumSize(QSize(59, 59))
        self.thrustup_label.setPixmap(QPixmap(u":/Front/icons/light_green.png"))
        self.thrustup_label.setScaledContents(True)

        self.verticalLayout.addWidget(self.thrustup_label)

        self.frame_2 = QFrame(self.layoutWidget)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.Shape.HLine)
        self.frame_2.setFrameShadow(QFrame.Shadow.Raised)

        self.verticalLayout.addWidget(self.frame_2)

        self.thrustdown_label = QLabel(self.layoutWidget)
        self.thrustdown_label.setObjectName(u"thrustdown_label")
        sizePolicy1.setHeightForWidth(self.thrustdown_label.sizePolicy().hasHeightForWidth())
        self.thrustdown_label.setSizePolicy(sizePolicy1)
        self.thrustdown_label.setMinimumSize(QSize(59, 59))
        self.thrustdown_label.setMaximumSize(QSize(59, 59))
        self.thrustdown_label.setPixmap(QPixmap(u":/Front/icons/light_red.png"))
        self.thrustdown_label.setScaledContents(True)

        self.verticalLayout.addWidget(self.thrustdown_label)

        self.widget = QWidget(self.frame)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(160, 20, 111, 111))
        self.acw_label = QLabel(self.widget)
        self.acw_label.setObjectName(u"acw_label")
        self.acw_label.setGeometry(QRect(20, 10, 71, 71))
        sizePolicy1.setHeightForWidth(self.acw_label.sizePolicy().hasHeightForWidth())
        self.acw_label.setSizePolicy(sizePolicy1)
        self.acw_label.setPixmap(QPixmap(u":/Front/icons/acw_arrow.png"))
        self.acw_label.setScaledContents(True)
        self.cw_label = QLabel(self.widget)
        self.cw_label.setObjectName(u"cw_label")
        self.cw_label.setGeometry(QRect(20, 50, 71, 71))
        sizePolicy1.setHeightForWidth(self.cw_label.sizePolicy().hasHeightForWidth())
        self.cw_label.setSizePolicy(sizePolicy1)
        self.cw_label.setPixmap(QPixmap(u":/Front/icons/cw_arrow.png"))
        self.cw_label.setScaledContents(True)
        self.layoutWidget1 = QWidget(self.frame)
        self.layoutWidget1.setObjectName(u"layoutWidget1")
        self.layoutWidget1.setGeometry(QRect(270, 50, 151, 72))
        self.horizontalLayout = QHBoxLayout(self.layoutWidget1)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.Hgripper_label = QLabel(self.layoutWidget1)
        self.Hgripper_label.setObjectName(u"Hgripper_label")
        sizePolicy1.setHeightForWidth(self.Hgripper_label.sizePolicy().hasHeightForWidth())
        self.Hgripper_label.setSizePolicy(sizePolicy1)
        self.Hgripper_label.setMinimumSize(QSize(70, 70))
        self.Hgripper_label.setMaximumSize(QSize(70, 70))
        self.Hgripper_label.setStyleSheet(u"")
        self.Hgripper_label.setPixmap(QPixmap(u":/Front/icons/open_Hgripper.png"))
        self.Hgripper_label.setScaledContents(True)

        self.horizontalLayout.addWidget(self.Hgripper_label)

        self.Vgripper_label = QLabel(self.layoutWidget1)
        self.Vgripper_label.setObjectName(u"Vgripper_label")
        sizePolicy1.setHeightForWidth(self.Vgripper_label.sizePolicy().hasHeightForWidth())
        self.Vgripper_label.setSizePolicy(sizePolicy1)
        self.Vgripper_label.setMinimumSize(QSize(70, 70))
        self.Vgripper_label.setMaximumSize(QSize(70, 70))
        self.Vgripper_label.setPixmap(QPixmap(u":/Front/icons/open_Vgripper.png"))
        self.Vgripper_label.setScaledContents(True)

        self.horizontalLayout.addWidget(self.Vgripper_label)

        self.Speed_bar = CircularProgress(self.frame)
        self.Speed_bar.setObjectName(u"Speed_bar")
        self.Speed_bar.setGeometry(QRect(430, 20, 141, 141))
        sizePolicy1.setHeightForWidth(self.Speed_bar.sizePolicy().hasHeightForWidth())
        self.Speed_bar.setSizePolicy(sizePolicy1)
        self.label_8 = QLabel(self.Speed_bar)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setGeometry(QRect(10, 30, 91, 41))
        font = QFont()
        font.setBold(True)
        self.label_8.setFont(font)
        self.label_8.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.Gain_bar = CircularProgress(self.frame)
        self.Gain_bar.setObjectName(u"Gain_bar")
        self.Gain_bar.setGeometry(QRect(580, 20, 141, 141))
        sizePolicy1.setHeightForWidth(self.Gain_bar.sizePolicy().hasHeightForWidth())
        self.Gain_bar.setSizePolicy(sizePolicy1)
        self.Gain_bar.setStyleSheet(u"background-color: transparent;")
        self.label_12 = QLabel(self.Gain_bar)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setGeometry(QRect(10, 30, 91, 41))
        self.label_12.setFont(font)
        self.label_12.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.layoutWidget2 = QWidget(self.frame)
        self.layoutWidget2.setObjectName(u"layoutWidget2")
        self.layoutWidget2.setGeometry(QRect(750, 10, 172, 161))
        self.verticalLayout_2 = QVBoxLayout(self.layoutWidget2)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.lcdNumber = QLCDNumber(self.layoutWidget2)
        self.lcdNumber.setObjectName(u"lcdNumber")
        self.lcdNumber.setDigitCount(5)

        self.verticalLayout_2.addWidget(self.lcdNumber)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.start_btn = QPushButton(self.layoutWidget2)
        self.start_btn.setObjectName(u"start_btn")

        self.horizontalLayout_2.addWidget(self.start_btn)

        self.reset_btn = QPushButton(self.layoutWidget2)
        self.reset_btn.setObjectName(u"reset_btn")

        self.horizontalLayout_2.addWidget(self.reset_btn)


        self.verticalLayout_2.addLayout(self.horizontalLayout_2)

        self.verticalLayout_2.setStretch(0, 2)
        self.verticalLayout_2.setStretch(1, 1)
        self.Stabilizer_label = QLabel(self.frame)
        self.Stabilizer_label.setObjectName(u"Stabilizer_label")
        self.Stabilizer_label.setGeometry(QRect(940, 50, 151, 71))
        self.Stabilizer_label.setFont(font)
        self.Stabilizer_label.setStyleSheet(u"background-color: rgb(255, 0, 0);")
        self.Stabilizer_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_3.addWidget(self.frame)

        self.verticalLayout_3.setStretch(0, 3)
        self.verticalLayout_3.setStretch(1, 1)

        self.verticalLayout_4.addLayout(self.verticalLayout_3)

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
        self.comboBox_4.setItemText(0, QCoreApplication.translate("CoPilot_Window", u"Cam 1", None))
        self.comboBox_4.setItemText(1, QCoreApplication.translate("CoPilot_Window", u"Cam 2", None))
        self.comboBox_4.setItemText(2, QCoreApplication.translate("CoPilot_Window", u"Cam 3", None))
        self.comboBox_4.setItemText(3, QCoreApplication.translate("CoPilot_Window", u"Cam 4", None))

        self.Camera.setText(QCoreApplication.translate("CoPilot_Window", u"Cam 1", None))
        self.outercircle_label.setText("")
        self.innercircle_label.setText("")
        self.thrustup_label.setText("")
        self.thrustdown_label.setText("")
        self.acw_label.setText("")
        self.cw_label.setText("")
        self.Hgripper_label.setText("")
        self.Vgripper_label.setText("")
        self.label_8.setText(QCoreApplication.translate("CoPilot_Window", u"Speed", None))
        self.label_12.setText(QCoreApplication.translate("CoPilot_Window", u"Gain", None))
        self.start_btn.setText(QCoreApplication.translate("CoPilot_Window", u"Start", None))
        self.reset_btn.setText(QCoreApplication.translate("CoPilot_Window", u"Reset", None))
        self.Stabilizer_label.setText(QCoreApplication.translate("CoPilot_Window", u"Stabilizer", None))
    # retranslateUi

