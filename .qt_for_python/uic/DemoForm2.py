# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'DemoForm2.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(830, 609)
        self.actionmenus = QAction(MainWindow)
        self.actionmenus.setObjectName(u"actionmenus")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayoutWidget = QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setObjectName(u"horizontalLayoutWidget")
        self.horizontalLayoutWidget.setGeometry(QRect(60, 230, 701, 151))
        self.horizontalLayout = QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.pushButton = QPushButton(self.horizontalLayoutWidget)
        self.pushButton.setObjectName(u"pushButton")
        font = QFont()
        font.setFamily(u"\ub9d1\uc740 \uace0\ub515")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton.setFont(font)

        self.horizontalLayout.addWidget(self.pushButton)

        self.pushButton_2 = QPushButton(self.horizontalLayoutWidget)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setFont(font)

        self.horizontalLayout.addWidget(self.pushButton_2)

        self.pushButton_3 = QPushButton(self.horizontalLayoutWidget)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setFont(font)

        self.horizontalLayout.addWidget(self.pushButton_3)

        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(60, 140, 701, 91))
        font1 = QFont()
        font1.setFamily(u"\ub9d1\uc740 \uace0\ub515")
        font1.setPointSize(28)
        self.label.setFont(font1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 830, 22))
        self.menu = QMenu(self.menubar)
        self.menu.setObjectName(u"menu")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menu.menuAction())
        self.menu.addAction(self.actionmenus)

        self.retranslateUi(MainWindow)
        self.pushButton.clicked.connect(MainWindow.firstClick)
        self.pushButton_2.clicked.connect(MainWindow.secondClick)
        self.pushButton_3.clicked.connect(MainWindow.thirdClick)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.actionmenus.setText(QCoreApplication.translate("MainWindow", u"menus", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"\uccab\ubc88\uc9f8", None))
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"\ub450\ubc88\uc9f8", None))
        self.pushButton_3.setText(QCoreApplication.translate("MainWindow", u"\uc138\ubc88\uc9f8", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.menu.setTitle(QCoreApplication.translate("MainWindow", u"\uc774\uac74 \ubb50\uc2dc\ub2e4\ub0d0", None))
    # retranslateUi

