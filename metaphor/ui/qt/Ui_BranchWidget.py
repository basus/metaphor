# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'branchWidget.ui'
#
# Created: Mon Jul 26 15:37:52 2010
#      by: PyQt4 UI code generator 4.7.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

class Ui_Branch(object):
    def setupUi(self, Branch):
        Branch.setObjectName("Branch")
        Branch.setEnabled(True)
        Branch.resize(180, 300)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Branch.sizePolicy().hasHeightForWidth())
        Branch.setSizePolicy(sizePolicy)
        Branch.setMinimumSize(QtCore.QSize(180, 200))
        Branch.setMaximumSize(QtCore.QSize(180, 16777215))
        self.verticalLayout = QtGui.QVBoxLayout(Branch)
        self.verticalLayout.setSpacing(5)
        self.verticalLayout.setMargin(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setContentsMargins(0, 0, -1, -1)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.nameButton = QtGui.QToolButton(Branch)
        self.nameButton.setEnabled(True)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.nameButton.sizePolicy().hasHeightForWidth())
        self.nameButton.setSizePolicy(sizePolicy)
        self.nameButton.setObjectName("nameButton")
        self.horizontalLayout_2.addWidget(self.nameButton)
        self.deleteBranchButton = QtGui.QToolButton(Branch)
        self.deleteBranchButton.setObjectName("deleteBranchButton")
        self.horizontalLayout_2.addWidget(self.deleteBranchButton)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.scrollArea = QtGui.QScrollArea(Branch)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtGui.QWidget(self.scrollArea)
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 176, 236))
        self.scrollAreaWidgetContents.setAcceptDrops(True)
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.actionsLayout = QtGui.QVBoxLayout(self.scrollAreaWidgetContents)
        self.actionsLayout.setSpacing(2)
        self.actionsLayout.setMargin(0)
        self.actionsLayout.setObjectName("actionsLayout")
        spacerItem = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.actionsLayout.addItem(spacerItem)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.verticalLayout.addWidget(self.scrollArea)
        self.addActionButton = QtGui.QToolButton(Branch)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.addActionButton.sizePolicy().hasHeightForWidth())
        self.addActionButton.setSizePolicy(sizePolicy)
        self.addActionButton.setObjectName("addActionButton")
        self.verticalLayout.addWidget(self.addActionButton)

        self.retranslateUi(Branch)
        QtCore.QObject.connect(self.nameButton, QtCore.SIGNAL("clicked()"), Branch.editName)
        QtCore.QObject.connect(self.addActionButton, QtCore.SIGNAL("clicked()"), Branch.addAction)
        QtCore.QObject.connect(self.deleteBranchButton, QtCore.SIGNAL("clicked()"), Branch.deleteBranch)
        QtCore.QMetaObject.connectSlotsByName(Branch)

    def retranslateUi(self, Branch):
        Branch.setWindowTitle(QtGui.QApplication.translate("Branch", "Branch", None, QtGui.QApplication.UnicodeUTF8))
        self.nameButton.setToolTip(QtGui.QApplication.translate("Branch", "Edit branch name", None, QtGui.QApplication.UnicodeUTF8))
        self.nameButton.setStatusTip(QtGui.QApplication.translate("Branch", "Edit branch name", None, QtGui.QApplication.UnicodeUTF8))
        self.nameButton.setText(QtGui.QApplication.translate("Branch", "New Branch", None, QtGui.QApplication.UnicodeUTF8))
        self.deleteBranchButton.setToolTip(QtGui.QApplication.translate("Branch", "Delete branch", None, QtGui.QApplication.UnicodeUTF8))
        self.deleteBranchButton.setStatusTip(QtGui.QApplication.translate("Branch", "Delete branch", None, QtGui.QApplication.UnicodeUTF8))
        self.deleteBranchButton.setText(QtGui.QApplication.translate("Branch", "X", None, QtGui.QApplication.UnicodeUTF8))
        self.addActionButton.setToolTip(QtGui.QApplication.translate("Branch", "Add action", None, QtGui.QApplication.UnicodeUTF8))
        self.addActionButton.setStatusTip(QtGui.QApplication.translate("Branch", "Add action", None, QtGui.QApplication.UnicodeUTF8))
        self.addActionButton.setText(QtGui.QApplication.translate("Branch", "Add action", None, QtGui.QApplication.UnicodeUTF8))

