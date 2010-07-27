# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'editActionDialog.ui'
#
# Created: Thu Jul 22 09:14:38 2010
#      by: PyQt4 UI code generator 4.7.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

class Ui_EditActionDialog(object):
    def setupUi(self, EditActionDialog):
        EditActionDialog.setObjectName("EditActionDialog")
        EditActionDialog.setWindowModality(QtCore.Qt.ApplicationModal)
        EditActionDialog.resize(300, 140)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(EditActionDialog.sizePolicy().hasHeightForWidth())
        EditActionDialog.setSizePolicy(sizePolicy)
        EditActionDialog.setMinimumSize(QtCore.QSize(300, 140))
        EditActionDialog.setMaximumSize(QtCore.QSize(300, 140))
        self.layout = QtGui.QVBoxLayout(EditActionDialog)
        self.layout.setObjectName("layout")
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtGui.QLabel(EditActionDialog)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.actionsMenu = QtGui.QComboBox(EditActionDialog)
        self.actionsMenu.setObjectName("actionsMenu")
        self.horizontalLayout.addWidget(self.actionsMenu)
        self.layout.addLayout(self.horizontalLayout)
        self.buttonBox = QtGui.QDialogButtonBox(EditActionDialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.layout.addWidget(self.buttonBox)

        self.retranslateUi(EditActionDialog)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL("accepted()"), EditActionDialog.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL("rejected()"), EditActionDialog.reject)
        QtCore.QMetaObject.connectSlotsByName(EditActionDialog)

    def retranslateUi(self, EditActionDialog):
        EditActionDialog.setWindowTitle(QtGui.QApplication.translate("EditActionDialog", "Edit Action", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("EditActionDialog", "Action Type:", None, QtGui.QApplication.UnicodeUTF8))

