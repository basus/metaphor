# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'editBranchDialog.ui'
#
# Created: Tue Jul 20 15:06:30 2010
#      by: PyQt4 UI code generator 4.7.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

class Ui_EditBranchDialog(object):
    def setupUi(self, EditBranchDialog):
        EditBranchDialog.setObjectName("EditBranchDialog")
        EditBranchDialog.setWindowModality(QtCore.Qt.ApplicationModal)
        EditBranchDialog.resize(300, 140)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(EditBranchDialog.sizePolicy().hasHeightForWidth())
        EditBranchDialog.setSizePolicy(sizePolicy)
        EditBranchDialog.setMinimumSize(QtCore.QSize(300, 140))
        EditBranchDialog.setMaximumSize(QtCore.QSize(300, 140))
        self.verticalLayout = QtGui.QVBoxLayout(EditBranchDialog)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtGui.QLabel(EditBranchDialog)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.nameInput = QtGui.QLineEdit(EditBranchDialog)
        self.nameInput.setObjectName("nameInput")
        self.horizontalLayout.addWidget(self.nameInput)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_2 = QtGui.QLabel(EditBranchDialog)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_2.addWidget(self.label_2)
        self.weightInput = QtGui.QSpinBox(EditBranchDialog)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.weightInput.sizePolicy().hasHeightForWidth())
        self.weightInput.setSizePolicy(sizePolicy)
        self.weightInput.setProperty("value", 1)
        self.weightInput.setObjectName("weightInput")
        self.horizontalLayout_2.addWidget(self.weightInput)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.buttonBox = QtGui.QDialogButtonBox(EditBranchDialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.verticalLayout.addWidget(self.buttonBox)

        self.retranslateUi(EditBranchDialog)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL("accepted()"), EditBranchDialog.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL("rejected()"), EditBranchDialog.reject)
        QtCore.QMetaObject.connectSlotsByName(EditBranchDialog)

    def retranslateUi(self, EditBranchDialog):
        EditBranchDialog.setWindowTitle(QtGui.QApplication.translate("EditBranchDialog", "Edit Branch", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("EditBranchDialog", "Branch Name:", None, QtGui.QApplication.UnicodeUTF8))
        self.nameInput.setText(QtGui.QApplication.translate("EditBranchDialog", "default_name", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("EditBranchDialog", "Weight:", None, QtGui.QApplication.UnicodeUTF8))

