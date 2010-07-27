# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'productionNameDialog.ui'
#
# Created: Tue Jul 20 15:06:25 2010
#      by: PyQt4 UI code generator 4.7.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

class Ui_ProductionNameDialog(object):
    def setupUi(self, ProductionNameDialog):
        ProductionNameDialog.setObjectName("ProductionNameDialog")
        ProductionNameDialog.setWindowModality(QtCore.Qt.ApplicationModal)
        ProductionNameDialog.resize(300, 100)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(ProductionNameDialog.sizePolicy().hasHeightForWidth())
        ProductionNameDialog.setSizePolicy(sizePolicy)
        ProductionNameDialog.setMinimumSize(QtCore.QSize(300, 100))
        ProductionNameDialog.setMaximumSize(QtCore.QSize(300, 100))
        self.verticalLayout = QtGui.QVBoxLayout(ProductionNameDialog)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtGui.QLabel(ProductionNameDialog)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.nameInput = QtGui.QLineEdit(ProductionNameDialog)
        self.nameInput.setObjectName("nameInput")
        self.horizontalLayout.addWidget(self.nameInput)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.buttonBox = QtGui.QDialogButtonBox(ProductionNameDialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.verticalLayout.addWidget(self.buttonBox)

        self.retranslateUi(ProductionNameDialog)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL("accepted()"), ProductionNameDialog.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL("rejected()"), ProductionNameDialog.reject)
        QtCore.QMetaObject.connectSlotsByName(ProductionNameDialog)

    def retranslateUi(self, ProductionNameDialog):
        ProductionNameDialog.setWindowTitle(QtGui.QApplication.translate("ProductionNameDialog", "Edit Production Name", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("ProductionNameDialog", "Production Name:", None, QtGui.QApplication.UnicodeUTF8))
        self.nameInput.setText(QtGui.QApplication.translate("ProductionNameDialog", "default_name", None, QtGui.QApplication.UnicodeUTF8))

