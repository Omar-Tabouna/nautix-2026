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

        self.verticalLayout_6 = QVBoxLayout()
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_6.addItem(self.horizontalSpacer)

        self.sec_feed3_label = QLabel(self.centralwidget)
        self.sec_feed3_label.setObjectName(u"sec_feed3_label")

        self.horizontalLayout_6.addWidget(self.sec_feed3_label)

        self.box4 = QComboBox(self.centralwidget)
        self.box4.addItem("")
        self.box4.addItem("")
        self.box4.addItem("")
        self.box4.addItem("")
        self.box4.setObjectName(u"box4")

        self.horizontalLayout_6.addWidget(self.box4)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_6.addItem(self.horizontalSpacer_2)


        self.verticalLayout_6.addLayout(self.horizontalLayout_6)

        self.Cam4 = QLabel(self.centralwidget)
        self.Cam4.setObjectName(u"Cam4")
        sizePolicy.setHeightForWidth(self.Cam4.sizePolicy().hasHeightForWidth())
        self.Cam4.setSizePolicy(sizePolicy)
        self.Cam4.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_6.addWidget(self.Cam4)

        self.verticalLayout_6.setStretch(1, 6)

        self.horizontalLayout_3.addLayout(self.verticalLayout_6)


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

        self.verticalLayout_5.setStretch(0, 1)
        self.verticalLayout_5.setStretch(2, 2)

        self.verticalLayout_2.addLayout(self.verticalLayout_5)

        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        sizePolicy.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy)
        self.frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QFrame.Shadow.Raised)
        self.widget_3 = QWidget(self.frame)
        self.widget_3.setObjectName(u"widget_3")
        self.widget_3.setGeometry(QRect(10, 30, 71, 71))
        self.label = QLabel(self.widget_3)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(10, 10, 50, 50))
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy1)
        self.label.setMaximumSize(QSize(50, 50))
        self.label.setPixmap(QPixmap(u":/Front/icons/circle.png"))
        self.label.setScaledContents(True)
        self.label_9 = QLabel(self.widget_3)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setGeometry(QRect(20, 20, 30, 30))
        sizePolicy1.setHeightForWidth(self.label_9.sizePolicy().hasHeightForWidth())
        self.label_9.setSizePolicy(sizePolicy1)
        self.label_9.setMaximumSize(QSize(200, 200))
        self.label_9.setPixmap(QPixmap(u":/Front/icons/circle2.png"))
        self.label_9.setScaledContents(True)
        self.layoutWidget = QWidget(self.frame)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(90, 10, 62, 124))
        self.verticalLayout = QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.thrustup_label = QLabel(self.layoutWidget)
        self.thrustup_label.setObjectName(u"thrustup_label")
        sizePolicy1.setHeightForWidth(self.thrustup_label.sizePolicy().hasHeightForWidth())
        self.thrustup_label.setSizePolicy(sizePolicy1)
        self.thrustup_label.setMinimumSize(QSize(60, 50))
        self.thrustup_label.setMaximumSize(QSize(60, 50))
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
        self.thrustdown_label.setMinimumSize(QSize(60, 50))
        self.thrustdown_label.setMaximumSize(QSize(60, 50))
        self.thrustdown_label.setPixmap(QPixmap(u":/Front/icons/light_red.png"))
        self.thrustdown_label.setScaledContents(True)

        self.verticalLayout.addWidget(self.thrustdown_label)

        self.widget = QWidget(self.frame)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(160, 20, 111, 111))
        self.acw_label = QLabel(self.widget)
        self.acw_label.setObjectName(u"acw_label")
        self.acw_label.setGeometry(QRect(20, -10, 71, 71))
        sizePolicy1.setHeightForWidth(self.acw_label.sizePolicy().hasHeightForWidth())
        self.acw_label.setSizePolicy(sizePolicy1)
        self.acw_label.setPixmap(QPixmap(u":/Front/icons/acw_arrow.png"))
        self.acw_label.setScaledContents(True)
        self.cw_label = QLabel(self.widget)
        self.cw_label.setObjectName(u"cw_label")
        self.cw_label.setGeometry(QRect(20, 30, 71, 71))
        sizePolicy1.setHeightForWidth(self.cw_label.sizePolicy().hasHeightForWidth())
        self.cw_label.setSizePolicy(sizePolicy1)
        self.cw_label.setPixmap(QPixmap(u":/Front/icons/cw_arrow.png"))
        self.cw_label.setScaledContents(True)
        self.layoutWidget1 = QWidget(self.frame)
        self.layoutWidget1.setObjectName(u"layoutWidget1")
        self.layoutWidget1.setGeometry(QRect(270, 30, 151, 72))
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
        self.Speed_bar.setGeometry(QRect(450, 20, 101, 101))
        sizePolicy1.setHeightForWidth(self.Speed_bar.sizePolicy().hasHeightForWidth())
        self.Speed_bar.setSizePolicy(sizePolicy1)
        self.label_8 = QLabel(self.Speed_bar)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setGeometry(QRect(10, 30, 91, 41))
        font = QFont()
        font.setPointSize(16)
        self.label_8.setFont(font)
        self.label_8.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.Gain_bar = CircularProgress(self.frame)
        self.Gain_bar.setObjectName(u"Gain_bar")
        self.Gain_bar.setGeometry(QRect(580, 20, 101, 101))
        sizePolicy1.setHeightForWidth(self.Gain_bar.sizePolicy().hasHeightForWidth())
        self.Gain_bar.setSizePolicy(sizePolicy1)
        self.Gain_bar.setStyleSheet(u"background-color: transparent;")
        self.label_12 = QLabel(self.Gain_bar)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setGeometry(QRect(10, 30, 91, 41))
        self.label_12.setFont(font)
        self.label_12.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.Stabilizer_label = QLabel(self.frame)
        self.Stabilizer_label.setObjectName(u"Stabilizer_label")
        self.Stabilizer_label.setGeometry(QRect(730, 30, 151, 71))
        font1 = QFont()
        font1.setPointSize(24)
        font1.setBold(True)
        self.Stabilizer_label.setFont(font1)
        self.Stabilizer_label.setStyleSheet(u"background-color: rgb(255, 0, 0);")
        self.Stabilizer_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_2.addWidget(self.frame)

        self.verticalLayout_2.setStretch(0, 5)
        self.verticalLayout_2.setStretch(1, 1)

        self.verticalLayout_8.addLayout(self.verticalLayout_2)

        Pilot_Window.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(Pilot_Window)
        self.statusbar.setObjectName(u"statusbar")
        Pilot_Window.setStatusBar(self.statusbar)

        self.retranslateUi(Pilot_Window)

        self.box2.setCurrentIndex(1)
        self.box3.setCurrentIndex(2)
        self.box4.setCurrentIndex(3)


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
        self.sec_feed3_label.setText(QCoreApplication.translate("Pilot_Window", u"Secondary Feed 3:", None))
        self.box4.setItemText(0, QCoreApplication.translate("Pilot_Window", u"Cam 1", None))
        self.box4.setItemText(1, QCoreApplication.translate("Pilot_Window", u"Cam 2", None))
        self.box4.setItemText(2, QCoreApplication.translate("Pilot_Window", u"Cam 3", None))
        self.box4.setItemText(3, QCoreApplication.translate("Pilot_Window", u"Cam 4", None))

        self.Cam4.setText(QCoreApplication.translate("Pilot_Window", u"Cam 4", None))
        self.prim_feed_label.setText(QCoreApplication.translate("Pilot_Window", u"Primary Feed:", None))
        self.box1.setItemText(0, QCoreApplication.translate("Pilot_Window", u"Cam 1", None))
        self.box1.setItemText(1, QCoreApplication.translate("Pilot_Window", u"Cam 2", None))
        self.box1.setItemText(2, QCoreApplication.translate("Pilot_Window", u"Cam 3", None))
        self.box1.setItemText(3, QCoreApplication.translate("Pilot_Window", u"Cam 4", None))

        self.Cam1.setText(QCoreApplication.translate("Pilot_Window", u"Cam 1", None))
        self.label.setText("")
        self.label_9.setText("")
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

