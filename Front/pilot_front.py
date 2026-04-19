# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'pilot.ui'
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
    QLabel, QMainWindow, QSizePolicy, QSpacerItem,
    QStatusBar, QVBoxLayout, QWidget)

from Front.circularprogress import CircularProgress
import resources_rc

class Ui_Pilot_Window(object):
    def setupUi(self, Pilot_Window):
        if not Pilot_Window.objectName():
            Pilot_Window.setObjectName(u"Pilot_Window")
        Pilot_Window.resize(966, 855)
        Pilot_Window.setStyleSheet(u"QMainWindow {\n"
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
        self.centralwidget = QWidget(Pilot_Window)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout_8 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_5 = QVBoxLayout()
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_5)

        self.sec_feed1_label = QLabel(self.centralwidget)
        self.sec_feed1_label.setObjectName(u"sec_feed1_label")

        self.horizontalLayout_4.addWidget(self.sec_feed1_label)

        self.box2 = QComboBox(self.centralwidget)
        self.box2.addItem("")
        self.box2.addItem("")
        self.box2.addItem("")
        self.box2.addItem("")
        self.box2.setObjectName(u"box2")

        self.horizontalLayout_4.addWidget(self.box2)

        self.horizontalSpacer_6 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_6)


        self.verticalLayout_3.addLayout(self.horizontalLayout_4)

        self.Cam2 = QLabel(self.centralwidget)
        self.Cam2.setObjectName(u"Cam2")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Cam2.sizePolicy().hasHeightForWidth())
        self.Cam2.setSizePolicy(sizePolicy)
        self.Cam2.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_3.addWidget(self.Cam2)

        self.verticalLayout_3.setStretch(1, 6)

        self.horizontalLayout_3.addLayout(self.verticalLayout_3)

        self.frame_3 = QFrame(self.centralwidget)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setFrameShape(QFrame.Shape.VLine)
        self.frame_3.setFrameShadow(QFrame.Shadow.Raised)

        self.horizontalLayout_3.addWidget(self.frame_3)

        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer_3)

        self.sec_feed2_label = QLabel(self.centralwidget)
        self.sec_feed2_label.setObjectName(u"sec_feed2_label")

        self.horizontalLayout_5.addWidget(self.sec_feed2_label)

        self.box3 = QComboBox(self.centralwidget)
        self.box3.addItem("")
        self.box3.addItem("")
        self.box3.addItem("")
        self.box3.addItem("")
        self.box3.setObjectName(u"box3")

        self.horizontalLayout_5.addWidget(self.box3)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer_4)


        self.verticalLayout_4.addLayout(self.horizontalLayout_5)

        self.Cam3 = QLabel(self.centralwidget)
        self.Cam3.setObjectName(u"Cam3")
        sizePolicy.setHeightForWidth(self.Cam3.sizePolicy().hasHeightForWidth())
        self.Cam3.setSizePolicy(sizePolicy)
        self.Cam3.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_4.addWidget(self.Cam3)

        self.verticalLayout_4.setStretch(1, 6)

        self.horizontalLayout_3.addLayout(self.verticalLayout_4)

        self.frame_4 = QFrame(self.centralwidget)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setFrameShape(QFrame.Shape.VLine)
        self.frame_4.setFrameShadow(QFrame.Shadow.Raised)

        self.horizontalLayout_3.addWidget(self.frame_4)


        self.verticalLayout_5.addLayout(self.horizontalLayout_3)

        self.frame_5 = QFrame(self.centralwidget)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setFrameShape(QFrame.Shape.HLine)
        self.frame_5.setFrameShadow(QFrame.Shadow.Raised)

        self.verticalLayout_5.addWidget(self.frame_5)

        self.verticalLayout_7 = QVBoxLayout()
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalSpacer_7 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_7.addItem(self.horizontalSpacer_7)

        self.prim_feed_label = QLabel(self.centralwidget)
        self.prim_feed_label.setObjectName(u"prim_feed_label")

        self.horizontalLayout_7.addWidget(self.prim_feed_label)

        self.box1 = QComboBox(self.centralwidget)
        self.box1.addItem("")
        self.box1.addItem("")
        self.box1.addItem("")
        self.box1.addItem("")
        self.box1.setObjectName(u"box1")

        self.horizontalLayout_7.addWidget(self.box1)

        self.horizontalSpacer_8 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_7.addItem(self.horizontalSpacer_8)


        self.verticalLayout_7.addLayout(self.horizontalLayout_7)

        self.Cam1 = QLabel(self.centralwidget)
        self.Cam1.setObjectName(u"Cam1")
        sizePolicy.setHeightForWidth(self.Cam1.sizePolicy().hasHeightForWidth())
        self.Cam1.setSizePolicy(sizePolicy)
        self.Cam1.setMaximumSize(QSize(16777215, 16777215))
        self.Cam1.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_7.addWidget(self.Cam1)

        self.verticalLayout_7.setStretch(1, 6)

        self.verticalLayout_5.addLayout(self.verticalLayout_7)

        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Maximum)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy1)
        self.frame.setMaximumSize(QSize(16777215, 150))
        self.frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_6 = QHBoxLayout(self.frame)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label = QLabel(self.frame)
        self.label.setObjectName(u"label")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy2)
        self.label.setMaximumSize(QSize(50, 50))
        self.label.setPixmap(QPixmap(u":/Front/icons/circle.png"))
        self.label.setScaledContents(True)

        self.horizontalLayout_2.addWidget(self.label)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.thrustup_label = QLabel(self.frame)
        self.thrustup_label.setObjectName(u"thrustup_label")
        sizePolicy2.setHeightForWidth(self.thrustup_label.sizePolicy().hasHeightForWidth())
        self.thrustup_label.setSizePolicy(sizePolicy2)
        self.thrustup_label.setMinimumSize(QSize(60, 50))
        self.thrustup_label.setMaximumSize(QSize(60, 50))
        self.thrustup_label.setPixmap(QPixmap(u":/Front/icons/light_green.png"))
        self.thrustup_label.setScaledContents(True)

        self.verticalLayout.addWidget(self.thrustup_label)

        self.frame_2 = QFrame(self.frame)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.Shape.HLine)
        self.frame_2.setFrameShadow(QFrame.Shadow.Raised)

        self.verticalLayout.addWidget(self.frame_2)

        self.thrustdown_label = QLabel(self.frame)
        self.thrustdown_label.setObjectName(u"thrustdown_label")
        sizePolicy2.setHeightForWidth(self.thrustdown_label.sizePolicy().hasHeightForWidth())
        self.thrustdown_label.setSizePolicy(sizePolicy2)
        self.thrustdown_label.setMinimumSize(QSize(60, 50))
        self.thrustdown_label.setMaximumSize(QSize(60, 50))
        self.thrustdown_label.setPixmap(QPixmap(u":/Front/icons/light_red.png"))
        self.thrustdown_label.setScaledContents(True)

        self.verticalLayout.addWidget(self.thrustdown_label)


        self.horizontalLayout_2.addLayout(self.verticalLayout)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_2)

        self.verticalLayout_6 = QVBoxLayout()
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.acw_label = QLabel(self.frame)
        self.acw_label.setObjectName(u"acw_label")
        sizePolicy3 = QSizePolicy(QSizePolicy.Policy.Maximum, QSizePolicy.Policy.Maximum)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.acw_label.sizePolicy().hasHeightForWidth())
        self.acw_label.setSizePolicy(sizePolicy3)
        self.acw_label.setMaximumSize(QSize(100, 100))
        self.acw_label.setPixmap(QPixmap(u":/Front/icons/acw_arrow.png"))
        self.acw_label.setScaledContents(True)

        self.verticalLayout_6.addWidget(self.acw_label)

        self.cw_label = QLabel(self.frame)
        self.cw_label.setObjectName(u"cw_label")
        sizePolicy3.setHeightForWidth(self.cw_label.sizePolicy().hasHeightForWidth())
        self.cw_label.setSizePolicy(sizePolicy3)
        self.cw_label.setMaximumSize(QSize(100, 100))
        self.cw_label.setPixmap(QPixmap(u":/Front/icons/cw_arrow.png"))
        self.cw_label.setScaledContents(True)

        self.verticalLayout_6.addWidget(self.cw_label)


        self.horizontalLayout_2.addLayout(self.verticalLayout_6)

        self.horizontalSpacer_9 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_9)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.Hgripper_label = QLabel(self.frame)
        self.Hgripper_label.setObjectName(u"Hgripper_label")
        sizePolicy2.setHeightForWidth(self.Hgripper_label.sizePolicy().hasHeightForWidth())
        self.Hgripper_label.setSizePolicy(sizePolicy2)
        self.Hgripper_label.setMinimumSize(QSize(70, 70))
        self.Hgripper_label.setMaximumSize(QSize(70, 70))
        self.Hgripper_label.setStyleSheet(u"")
        self.Hgripper_label.setPixmap(QPixmap(u":/Front/icons/open_Hgripper.png"))
        self.Hgripper_label.setScaledContents(True)

        self.horizontalLayout.addWidget(self.Hgripper_label)

        self.Vgripper_label = QLabel(self.frame)
        self.Vgripper_label.setObjectName(u"Vgripper_label")
        sizePolicy2.setHeightForWidth(self.Vgripper_label.sizePolicy().hasHeightForWidth())
        self.Vgripper_label.setSizePolicy(sizePolicy2)
        self.Vgripper_label.setMinimumSize(QSize(70, 70))
        self.Vgripper_label.setMaximumSize(QSize(70, 70))
        self.Vgripper_label.setPixmap(QPixmap(u":/Front/icons/open_Vgripper.png"))
        self.Vgripper_label.setScaledContents(True)

        self.horizontalLayout.addWidget(self.Vgripper_label)


        self.horizontalLayout_2.addLayout(self.horizontalLayout)

        self.horizontalSpacer_10 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_10)

        self.Speed_bar = CircularProgress(self.frame)
        self.Speed_bar.setObjectName(u"Speed_bar")
        sizePolicy3.setHeightForWidth(self.Speed_bar.sizePolicy().hasHeightForWidth())
        self.Speed_bar.setSizePolicy(sizePolicy3)
        self.Speed_bar.setMinimumSize(QSize(100, 100))
        self.Speed_bar.setMaximumSize(QSize(100, 100))
        self.label_8 = QLabel(self.Speed_bar)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setGeometry(QRect(0, 10, 91, 41))
        font = QFont()
        font.setBold(True)
        self.label_8.setFont(font)
        self.label_8.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_2.addWidget(self.Speed_bar)

        self.horizontalSpacer_11 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_11)

        self.Gain_bar = CircularProgress(self.frame)
        self.Gain_bar.setObjectName(u"Gain_bar")
        sizePolicy3.setHeightForWidth(self.Gain_bar.sizePolicy().hasHeightForWidth())
        self.Gain_bar.setSizePolicy(sizePolicy3)
        self.Gain_bar.setMinimumSize(QSize(100, 100))
        self.Gain_bar.setMaximumSize(QSize(100, 100))
        self.Gain_bar.setStyleSheet(u"background-color: transparent;")
        self.label_12 = QLabel(self.Gain_bar)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setGeometry(QRect(0, 10, 91, 41))
        self.label_12.setFont(font)
        self.label_12.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_2.addWidget(self.Gain_bar)

        self.horizontalSpacer_12 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_12)

        self.Stabilizer_label = QLabel(self.frame)
        self.Stabilizer_label.setObjectName(u"Stabilizer_label")
        sizePolicy1.setHeightForWidth(self.Stabilizer_label.sizePolicy().hasHeightForWidth())
        self.Stabilizer_label.setSizePolicy(sizePolicy1)
        self.Stabilizer_label.setMinimumSize(QSize(0, 0))
        self.Stabilizer_label.setMaximumSize(QSize(16777215, 50))
        self.Stabilizer_label.setFont(font)
        self.Stabilizer_label.setStyleSheet(u"background-color: rgb(255, 0, 0);")
        self.Stabilizer_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_2.addWidget(self.Stabilizer_label)


        self.horizontalLayout_6.addLayout(self.horizontalLayout_2)


        self.verticalLayout_5.addWidget(self.frame)

        self.verticalLayout_5.setStretch(0, 1)
        self.verticalLayout_5.setStretch(2, 2)

        self.verticalLayout_2.addLayout(self.verticalLayout_5)

        self.verticalLayout_2.setStretch(0, 10)

        self.verticalLayout_8.addLayout(self.verticalLayout_2)

        Pilot_Window.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(Pilot_Window)
        self.statusbar.setObjectName(u"statusbar")
        Pilot_Window.setStatusBar(self.statusbar)

        self.retranslateUi(Pilot_Window)

        self.box2.setCurrentIndex(1)
        self.box3.setCurrentIndex(2)


        QMetaObject.connectSlotsByName(Pilot_Window)
    # setupUi

    def retranslateUi(self, Pilot_Window):
        Pilot_Window.setWindowTitle(QCoreApplication.translate("Pilot_Window", u"MainWindow", None))
        self.sec_feed1_label.setText(QCoreApplication.translate("Pilot_Window", u"Secondary Feed 1:", None))
        self.box2.setItemText(0, QCoreApplication.translate("Pilot_Window", u"Cam 1", None))
        self.box2.setItemText(1, QCoreApplication.translate("Pilot_Window", u"Cam 2", None))
        self.box2.setItemText(2, QCoreApplication.translate("Pilot_Window", u"Cam 3", None))
        self.box2.setItemText(3, QCoreApplication.translate("Pilot_Window", u"Cam 4", None))

        self.Cam2.setText(QCoreApplication.translate("Pilot_Window", u"Cam 2", None))
        self.sec_feed2_label.setText(QCoreApplication.translate("Pilot_Window", u"Secondary Feed 2:", None))
        self.box3.setItemText(0, QCoreApplication.translate("Pilot_Window", u"Cam 1", None))
        self.box3.setItemText(1, QCoreApplication.translate("Pilot_Window", u"Cam 2", None))
        self.box3.setItemText(2, QCoreApplication.translate("Pilot_Window", u"Cam 3", None))
        self.box3.setItemText(3, QCoreApplication.translate("Pilot_Window", u"Cam 4", None))

        self.Cam3.setText(QCoreApplication.translate("Pilot_Window", u"Cam 3", None))
        self.prim_feed_label.setText(QCoreApplication.translate("Pilot_Window", u"Primary Feed:", None))
        self.box1.setItemText(0, QCoreApplication.translate("Pilot_Window", u"Cam 1", None))
        self.box1.setItemText(1, QCoreApplication.translate("Pilot_Window", u"Cam 2", None))
        self.box1.setItemText(2, QCoreApplication.translate("Pilot_Window", u"Cam 3", None))
        self.box1.setItemText(3, QCoreApplication.translate("Pilot_Window", u"Cam 4", None))

        self.Cam1.setText(QCoreApplication.translate("Pilot_Window", u"Cam 1", None))
        self.label.setText("")
        self.thrustup_label.setText("")
        self.thrustdown_label.setText("")
        self.acw_label.setText("")
        self.cw_label.setText("")
        self.Hgripper_label.setText("")
        self.Vgripper_label.setText("")
        self.label_8.setText(QCoreApplication.translate("Pilot_Window", u"Speed", None))
        self.label_12.setText(QCoreApplication.translate("Pilot_Window", u"Gain", None))
        self.Stabilizer_label.setText(QCoreApplication.translate("Pilot_Window", u"Stabilizer", None))
    # retranslateUi

