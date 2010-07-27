# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'axiomWidget.ui'
#
# Created: Mon Jul 26 15:36:36 2010
#      by: PyQt4 UI code generator 4.7.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

class Ui_Axiom(object):
    def setupUi(self, Axiom):
        Axiom.setObjectName("Axiom")
        Axiom.resize(97, 50)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Axiom.sizePolicy().hasHeightForWidth())
        Axiom.setSizePolicy(sizePolicy)
        Axiom.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.verticalLayout = QtGui.QVBoxLayout(Axiom)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setMargin(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.editButton = QtGui.QToolButton(Axiom)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.editButton.sizePolicy().hasHeightForWidth())
        self.editButton.setSizePolicy(sizePolicy)
        self.editButton.setObjectName("editButton")
        self.verticalLayout.addWidget(self.editButton)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.leftButton = QtGui.QToolButton(Axiom)
        self.leftButton.setObjectName("leftButton")
        self.horizontalLayout.addWidget(self.leftButton)
        self.deleteButtom = QtGui.QToolButton(Axiom)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.deleteButtom.sizePolicy().hasHeightForWidth())
        self.deleteButtom.setSizePolicy(sizePolicy)
        self.deleteButtom.setObjectName("deleteButtom")
        self.horizontalLayout.addWidget(self.deleteButtom)
        self.rightButton = QtGui.QToolButton(Axiom)
        self.rightButton.setObjectName("rightButton")
        self.horizontalLayout.addWidget(self.rightButton)
        self.verticalLayout.addLayout(self.horizontalLayout)

        self.retranslateUi(Axiom)
        QtCore.QObject.connect(self.editButton, QtCore.SIGNAL("clicked()"), Axiom.editAxiom)
        QtCore.QObject.connect(self.leftButton, QtCore.SIGNAL("clicked()"), Axiom.moveLeft)
        QtCore.QObject.connect(self.rightButton, QtCore.SIGNAL("clicked()"), Axiom.moveRight)
        QtCore.QObject.connect(self.deleteButtom, QtCore.SIGNAL("clicked()"), Axiom.deleteAxiom)
        QtCore.QMetaObject.connectSlotsByName(Axiom)

    def retranslateUi(self, Axiom):
        Axiom.setWindowTitle(QtGui.QApplication.translate("Axiom", "Axiom", None, QtGui.QApplication.UnicodeUTF8))
        self.editButton.setToolTip(QtGui.QApplication.translate("Axiom", "Edit axiom", None, QtGui.QApplication.UnicodeUTF8))
        self.editButton.setStatusTip(QtGui.QApplication.translate("Axiom", "Edit axiom", None, QtGui.QApplication.UnicodeUTF8))
        self.editButton.setText(QtGui.QApplication.translate("Axiom", "New Axiom", None, QtGui.QApplication.UnicodeUTF8))
        self.leftButton.setToolTip(QtGui.QApplication.translate("Axiom", "Move axiom left", None, QtGui.QApplication.UnicodeUTF8))
        self.leftButton.setStatusTip(QtGui.QApplication.translate("Axiom", "Move axiom left", None, QtGui.QApplication.UnicodeUTF8))
        self.leftButton.setText(QtGui.QApplication.translate("Axiom", "<", None, QtGui.QApplication.UnicodeUTF8))
        self.deleteButtom.setToolTip(QtGui.QApplication.translate("Axiom", "Delete axiom", None, QtGui.QApplication.UnicodeUTF8))
        self.deleteButtom.setStatusTip(QtGui.QApplication.translate("Axiom", "Delete axiom", None, QtGui.QApplication.UnicodeUTF8))
        self.deleteButtom.setText(QtGui.QApplication.translate("Axiom", "X", None, QtGui.QApplication.UnicodeUTF8))
        self.rightButton.setToolTip(QtGui.QApplication.translate("Axiom", "Move axiom right", None, QtGui.QApplication.UnicodeUTF8))
        self.rightButton.setStatusTip(QtGui.QApplication.translate("Axiom", "Move axiom right", None, QtGui.QApplication.UnicodeUTF8))
        self.rightButton.setText(QtGui.QApplication.translate("Axiom", ">", None, QtGui.QApplication.UnicodeUTF8))

