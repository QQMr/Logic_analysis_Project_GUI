# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Burton_window.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindowBurton(object):
    def setupUi(self, MainWindowBurton):
        MainWindowBurton.setObjectName("MainWindowBurton")
        MainWindowBurton.resize(921, 622)
        self.centralwidget = QtWidgets.QWidget(MainWindowBurton)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.matplot_buttons_hlayout = QtWidgets.QHBoxLayout()
        self.matplot_buttons_hlayout.setObjectName("matplot_buttons_hlayout")
        self.matplot_widget = QtWidgets.QWidget(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.matplot_widget.sizePolicy().hasHeightForWidth())
        self.matplot_widget.setSizePolicy(sizePolicy)
        self.matplot_widget.setObjectName("matplot_widget")
        self.matplot_vlayout = QtWidgets.QVBoxLayout(self.matplot_widget)
        self.matplot_vlayout.setObjectName("matplot_vlayout")
        self.matplot_buttons_hlayout.addWidget(self.matplot_widget)
        self.channels_vline = QtWidgets.QFrame(self.centralwidget)
        self.channels_vline.setFrameShape(QtWidgets.QFrame.VLine)
        self.channels_vline.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.channels_vline.setObjectName("channels_vline")
        self.matplot_buttons_hlayout.addWidget(self.channels_vline)
        self.verticalLayout.addLayout(self.matplot_buttons_hlayout)
        self.hline = QtWidgets.QFrame(self.centralwidget)
        self.hline.setFrameShape(QtWidgets.QFrame.HLine)
        self.hline.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.hline.setObjectName("hline")
        self.verticalLayout.addWidget(self.hline)
        self.cmd_query_hlayout = QtWidgets.QHBoxLayout()
        self.cmd_query_hlayout.setObjectName("cmd_query_hlayout")
        self.serial_combo = QtWidgets.QComboBox(self.centralwidget)
        self.serial_combo.setObjectName("serial_combo")
        self.cmd_query_hlayout.addWidget(self.serial_combo)
        self.acquire_button = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.acquire_button.sizePolicy().hasHeightForWidth())
        self.acquire_button.setSizePolicy(sizePolicy)
        self.acquire_button.setObjectName("acquire_button")
        self.cmd_query_hlayout.addWidget(self.acquire_button)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.cmd_query_hlayout.addItem(spacerItem)
        self.verticalLayout.addLayout(self.cmd_query_hlayout)
        MainWindowBurton.setCentralWidget(self.centralwidget)
        self.statusBar = QtWidgets.QStatusBar(MainWindowBurton)
        self.statusBar.setObjectName("statusBar")
        MainWindowBurton.setStatusBar(self.statusBar)

        self.retranslateUi(MainWindowBurton)
        self.acquire_button.clicked.connect(MainWindowBurton.Acquire)
        QtCore.QMetaObject.connectSlotsByName(MainWindowBurton)

    def retranslateUi(self, MainWindowBurton):
        _translate = QtCore.QCoreApplication.translate
        MainWindowBurton.setWindowTitle(_translate("MainWindowBurton", "IWATSU Digital Oscilloscope DS-8812 BRINGO"))
        self.acquire_button.setText(_translate("MainWindowBurton", "Acquire"))

