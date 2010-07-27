# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'actionWidget.ui'
#
# Created: Mon Jul 26 15:37:16 2010
#      by: PyQt4 UI code generator 4.7.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

class Ui_Action(object):
    def setupUi(self, Action):
        Action.setObjectName("Action")
        Action.resize(104, 24)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Action.sizePolicy().hasHeightForWidth())
        Action.setSizePolicy(sizePolicy)
        Action.setMaximumSize(QtCore.QSize(16777215, 24))
        self.horizontalLayout = QtGui.QHBoxLayout(Action)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setMargin(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.editButton = QtGui.QToolButton(Action)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.editButton.sizePolicy().hasHeightForWidth())
        self.editButton.setSizePolicy(sizePolicy)
        self.editButton.setObjectName("editButton")
        self.horizontalLayout.addWidget(self.editButton)
        self.deleteButton = QtGui.QToolButton(Action)
        self.deleteButton.setObjectName("deleteButton")
        self.horizontalLayout.addWidget(self.deleteButton)

        self.retranslateUi(Action)
        QtCore.QObject.connect(self.editButton, QtCore.SIGNAL("clicked()"), Action.editAction)
        QtCore.QObject.connect(self.deleteButton, QtCore.SIGNAL("clicked()"), Action.deleteAction)
        QtCore.QMetaObject.connectSlotsByName(Action)

    def retranslateUi(self, Action):
        Action.setWindowTitle(QtGui.QApplication.translate("Action", "Action", None, QtGui.QApplication.UnicodeUTF8))
        self.editButton.setToolTip(QtGui.QApplication.translate("Action", "Edit action", None, QtGui.QApplication.UnicodeUTF8))
        self.editButton.setStatusTip(QtGui.QApplication.translate("Action", "Edit action", None, QtGui.QApplication.UnicodeUTF8))
        self.editButton.setText(QtGui.QApplication.translate("Action", "New Action", None, QtGui.QApplication.UnicodeUTF8))
        self.deleteButton.setToolTip(QtGui.QApplication.translate("Action", "Delete action", None, QtGui.QApplication.UnicodeUTF8))
        self.deleteButton.setStatusTip(QtGui.QApplication.translate("Action", "Delete action", None, QtGui.QApplication.UnicodeUTF8))
        self.deleteButton.setText(QtGui.QApplication.translate("Action", "X", None, QtGui.QApplication.UnicodeUTF8))

