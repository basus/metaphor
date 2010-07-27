# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'generateDialog.ui'
#
# Created: Mon Jul 26 11:27:32 2010
#      by: PyQt4 UI code generator 4.7.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

class Ui_GenerateDialog(object):
    def setupUi(self, GenerateDialog):
        GenerateDialog.setObjectName("GenerateDialog")
        GenerateDialog.setWindowModality(QtCore.Qt.ApplicationModal)
        GenerateDialog.resize(501, 358)
        self.verticalLayout_2 = QtGui.QVBoxLayout(GenerateDialog)
        self.verticalLayout_2.setSpacing(-1)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label = QtGui.QLabel(GenerateDialog)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setObjectName("label")
        self.verticalLayout_2.addWidget(self.label)
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setSpacing(5)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_3 = QtGui.QLabel(GenerateDialog)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_2.addWidget(self.label_3)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.generations = QtGui.QSpinBox(GenerateDialog)
        self.generations.setSuffix("")
        self.generations.setMinimum(1)
        self.generations.setMaximum(999999999)
        self.generations.setObjectName("generations")
        self.horizontalLayout_2.addWidget(self.generations)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        spacerItem1 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem1)
        self.label_2 = QtGui.QLabel(GenerateDialog)
        self.label_2.setObjectName("label_2")
        self.verticalLayout.addWidget(self.label_2)
        self.statusBox = QtGui.QTextBrowser(GenerateDialog)
        self.statusBox.setObjectName("statusBox")
        self.verticalLayout.addWidget(self.statusBox)
        self.verticalLayout_2.addLayout(self.verticalLayout)
        self.buttonBox = QtGui.QDialogButtonBox(GenerateDialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Close|QtGui.QDialogButtonBox.Save)
        self.buttonBox.setCenterButtons(False)
        self.buttonBox.setObjectName("buttonBox")
        self.verticalLayout_2.addWidget(self.buttonBox)

        self.retranslateUi(GenerateDialog)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL("accepted()"), GenerateDialog.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL("rejected()"), GenerateDialog.reject)
        QtCore.QMetaObject.connectSlotsByName(GenerateDialog)

    def retranslateUi(self, GenerateDialog):
        GenerateDialog.setWindowTitle(QtGui.QApplication.translate("GenerateDialog", "Generate Image", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("GenerateDialog", "Generate image", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("GenerateDialog", "Generations", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("GenerateDialog", "Image Generation Status", None, QtGui.QApplication.UnicodeUTF8))

