# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/media/share/Users/catte/dev/mayaMatchMoveSolver/python/mmSolver/tools/loadmarker/ui/loadmarker_layout.ui'
#
# Created: Mon Dec 10 00:56:51 2018
#      by: pyside-uic 0.2.14 running on PySide 1.2.0
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(870, 874)
        self.verticalLayout_4 = QtGui.QVBoxLayout(Form)
        self.verticalLayout_4.setSpacing(1)
        self.verticalLayout_4.setContentsMargins(1, 1, 1, 1)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        spacerItem = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Preferred)
        self.verticalLayout.addItem(spacerItem)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.filepath_label = QtGui.QLabel(Form)
        self.filepath_label.setObjectName("filepath_label")
        self.horizontalLayout.addWidget(self.filepath_label)
        self.filepath_lineEdit = QtGui.QLineEdit(Form)
        self.filepath_lineEdit.setObjectName("filepath_lineEdit")
        self.horizontalLayout.addWidget(self.filepath_lineEdit)
        self.filepath_pushButton = QtGui.QPushButton(Form)
        self.filepath_pushButton.setObjectName("filepath_pushButton")
        self.horizontalLayout.addWidget(self.filepath_pushButton)
        spacerItem2 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem2)
        self.verticalLayout.addLayout(self.horizontalLayout)
        spacerItem3 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Preferred)
        self.verticalLayout.addItem(spacerItem3)
        self.verticalLayout_4.addLayout(self.verticalLayout)
        self.verticalLayout_2 = QtGui.QVBoxLayout()
        self.verticalLayout_2.setSpacing(6)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout_4 = QtGui.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        spacerItem4 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem4)
        self.camera_label = QtGui.QLabel(Form)
        self.camera_label.setObjectName("camera_label")
        self.horizontalLayout_4.addWidget(self.camera_label)
        self.camera_comboBox = QtGui.QComboBox(Form)
        self.camera_comboBox.setObjectName("camera_comboBox")
        self.horizontalLayout_4.addWidget(self.camera_comboBox)
        self.cameraUpdate_pushButton = QtGui.QPushButton(Form)
        self.cameraUpdate_pushButton.setObjectName("cameraUpdate_pushButton")
        self.horizontalLayout_4.addWidget(self.cameraUpdate_pushButton)
        spacerItem5 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem5)
        self.verticalLayout_2.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        spacerItem6 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem6)
        self.label_3 = QtGui.QLabel(Form)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_3.addWidget(self.label_3)
        self.spinBox_2 = QtGui.QSpinBox(Form)
        self.spinBox_2.setObjectName("spinBox_2")
        self.horizontalLayout_3.addWidget(self.spinBox_2)
        spacerItem7 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem7)
        self.verticalLayout_2.addLayout(self.horizontalLayout_3)
        self.verticalLayout_4.addLayout(self.verticalLayout_2)
        spacerItem8 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_4.addItem(spacerItem8)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(QtGui.QApplication.translate("Form", "Form", None, QtGui.QApplication.UnicodeUTF8))
        self.filepath_label.setText(QtGui.QApplication.translate("Form", "File Path", None, QtGui.QApplication.UnicodeUTF8))
        self.filepath_pushButton.setText(QtGui.QApplication.translate("Form", "Browse", None, QtGui.QApplication.UnicodeUTF8))
        self.camera_label.setText(QtGui.QApplication.translate("Form", "Camera", None, QtGui.QApplication.UnicodeUTF8))
        self.cameraUpdate_pushButton.setText(QtGui.QApplication.translate("Form", "Update", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("Form", "Option", None, QtGui.QApplication.UnicodeUTF8))

