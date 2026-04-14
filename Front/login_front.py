# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'login.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QHBoxLayout, QLabel,
    QMainWindow, QPushButton, QSizePolicy, QStatusBar,
    QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.widget = QWidget(self.centralwidget)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(80, 90, 641, 331))
        self.verticalLayout = QVBoxLayout(self.widget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.welcome_label = QLabel(self.widget)
        self.welcome_label.setObjectName(u"welcome_label")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.welcome_label.sizePolicy().hasHeightForWidth())
        self.welcome_label.setSizePolicy(sizePolicy)
        font = QFont()
        font.setPointSize(20)
        font.setBold(True)
        self.welcome_label.setFont(font)
        self.welcome_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout.addWidget(self.welcome_label)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.login_label = QLabel(self.widget)
        self.login_label.setObjectName(u"login_label")
        font1 = QFont()
        font1.setPointSize(15)
        self.login_label.setFont(font1)

        self.horizontalLayout.addWidget(self.login_label, 0, Qt.AlignmentFlag.AlignRight)

        self.userbox = QComboBox(self.widget)
        self.userbox.addItem("")
        self.userbox.addItem("")
        self.userbox.setObjectName(u"userbox")
        font2 = QFont()
        font2.setPointSize(14)
        self.userbox.setFont(font2)

        self.horizontalLayout.addWidget(self.userbox, 0, Qt.AlignmentFlag.AlignLeft)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.login_btn = QPushButton(self.widget)
        self.login_btn.setObjectName(u"login_btn")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Maximum, QSizePolicy.Policy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.login_btn.sizePolicy().hasHeightForWidth())
        self.login_btn.setSizePolicy(sizePolicy1)

        self.verticalLayout.addWidget(self.login_btn, 0, Qt.AlignmentFlag.AlignHCenter)

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.welcome_label.setText(QCoreApplication.translate("MainWindow", u"Welcome to NAUTIX GUI!", None))
        self.login_label.setText(QCoreApplication.translate("MainWindow", u"Login as: ", None))
        self.userbox.setItemText(0, QCoreApplication.translate("MainWindow", u"Pilot", None))
        self.userbox.setItemText(1, QCoreApplication.translate("MainWindow", u"Co-Pilot", None))

        self.login_btn.setText(QCoreApplication.translate("MainWindow", u"Login", None))
    # retranslateUi

