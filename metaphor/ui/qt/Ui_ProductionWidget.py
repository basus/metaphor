# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'productionWidget.ui'
#
# Created: Mon Jul 26 15:36:18 2010
#      by: PyQt4 UI code generator 4.7.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

class Ui_Production(object):
    def setupUi(self, Production):
        Production.setObjectName("Production")
        Production.resize(111, 50)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Production.sizePolicy().hasHeightForWidth())
        Production.setSizePolicy(sizePolicy)
        self.verticalLayout = QtGui.QVBoxLayout(Production)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setMargin(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.productionName = QtGui.QToolButton(Production)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.productionName.sizePolicy().hasHeightForWidth())
        self.productionName.setSizePolicy(sizePolicy)
        self.productionName.setObjectName("productionName")
        self.verticalLayout.addWidget(self.productionName)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setContentsMargins(-1, -1, -1, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.editButton = QtGui.QToolButton(Production)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.editButton.sizePolicy().hasHeightForWidth())
        self.editButton.setSizePolicy(sizePolicy)
        self.editButton.setObjectName("editButton")
        self.horizontalLayout.addWidget(self.editButton)
        self.deleteButton = QtGui.QToolButton(Production)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.deleteButton.sizePolicy().hasHeightForWidth())
        self.deleteButton.setSizePolicy(sizePolicy)
        self.deleteButton.setObjectName("deleteButton")
        self.horizontalLayout.addWidget(self.deleteButton)
        self.verticalLayout.addLayout(self.horizontalLayout)

        self.retranslateUi(Production)
        QtCore.QObject.connect(self.editButton, QtCore.SIGNAL("clicked()"), Production.editName)
        QtCore.QObject.connect(self.deleteButton, QtCore.SIGNAL("clicked()"), Production.deleteProd)
        QtCore.QObject.connect(self.productionName, QtCore.SIGNAL("clicked()"), Production.showProd)
        QtCore.QMetaObject.connectSlotsByName(Production)

    def retranslateUi(self, Production):
        Production.setWindowTitle(QtGui.QApplication.translate("Production", "Production", None, QtGui.QApplication.UnicodeUTF8))
        self.productionName.setToolTip(QtGui.QApplication.translate("Production", "Show production", None, QtGui.QApplication.UnicodeUTF8))
        self.productionName.setStatusTip(QtGui.QApplication.translate("Production", "Show production", None, QtGui.QApplication.UnicodeUTF8))
        self.productionName.setText(QtGui.QApplication.translate("Production", "Production Name", None, QtGui.QApplication.UnicodeUTF8))
        self.editButton.setToolTip(QtGui.QApplication.translate("Production", "Edit production name", None, QtGui.QApplication.UnicodeUTF8))
        self.editButton.setStatusTip(QtGui.QApplication.translate("Production", "Edit production name", None, QtGui.QApplication.UnicodeUTF8))
        self.editButton.setText(QtGui.QApplication.translate("Production", "Edit", None, QtGui.QApplication.UnicodeUTF8))
        self.deleteButton.setToolTip(QtGui.QApplication.translate("Production", "Delete production", None, QtGui.QApplication.UnicodeUTF8))
        self.deleteButton.setStatusTip(QtGui.QApplication.translate("Production", "Delete production", None, QtGui.QApplication.UnicodeUTF8))
        self.deleteButton.setText(QtGui.QApplication.translate("Production", "Delete", None, QtGui.QApplication.UnicodeUTF8))

