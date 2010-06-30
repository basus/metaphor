# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'metaphor/metaphor.ui'
#
# Created: Thu Feb 19 21:31:26 2009
#      by: PyQt4 UI code generator 4.3.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
import highlight

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(QtCore.QSize(QtCore.QRect(0,0,980,837).size()).expandedTo(MainWindow.minimumSizeHint()))

        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.gridlayout = QtGui.QGridLayout(self.centralwidget)
        self.gridlayout.setObjectName("gridlayout")

        self.frame = QtGui.QFrame(self.centralwidget)
        self.frame.setMinimumSize(QtCore.QSize(150,500))
        self.frame.setMaximumSize(QtCore.QSize(200,16777215))
        self.frame.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtGui.QFrame.Raised)
        self.frame.setObjectName("frame")

        self.vboxlayout = QtGui.QVBoxLayout(self.frame)
        self.vboxlayout.setObjectName("vboxlayout")

        self.label = QtGui.QLabel(self.frame)
        self.label.setObjectName("label")
        self.vboxlayout.addWidget(self.label)

        self.Contexts = QtGui.QListWidget(self.frame)
        self.Contexts.setObjectName("Contexts")
        self.vboxlayout.addWidget(self.Contexts)

        self.label_2 = QtGui.QLabel(self.frame)
        self.label_2.setObjectName("label_2")
        self.vboxlayout.addWidget(self.label_2)

        self.Grammars = QtGui.QListWidget(self.frame)
        self.Grammars.setObjectName("Grammars")
        self.vboxlayout.addWidget(self.Grammars)

        self.label_3 = QtGui.QLabel(self.frame)
        self.label_3.setObjectName("label_3")
        self.vboxlayout.addWidget(self.label_3)

        self.Generations = QtGui.QSpinBox(self.frame)
        self.Generations.setMinimum(2)
        self.Generations.setObjectName("Generations")
        self.vboxlayout.addWidget(self.Generations)

        self.label_4 = QtGui.QLabel(self.frame)
        self.label_4.setObjectName("label_4")
        self.vboxlayout.addWidget(self.label_4)

        self.OutputName = QtGui.QLineEdit(self.frame)
        self.OutputName.setObjectName("OutputName")
        self.vboxlayout.addWidget(self.OutputName)
        self.gridlayout.addWidget(self.frame,0,0,1,1)

        self.GrammarEdit = QtGui.QTextEdit(self.centralwidget)
        self.GrammarEdit.setMinimumSize(QtCore.QSize(700,500))
        self.GrammarEdit.setObjectName("GrammarEdit")
        self.GrammarEdit.setCurrentFont(QtGui.QFont('monospace'))
        self.GrammarEdit.setFontPointSize(9)
        self.highlight = highlight.Metaphor(self.GrammarEdit.document())
        self.gridlayout.addWidget(self.GrammarEdit,0,1,1,1)

        self.groupBox_2 = QtGui.QGroupBox(self.centralwidget)
        self.groupBox_2.setMinimumSize(QtCore.QSize(150,0))
        self.groupBox_2.setMaximumSize(QtCore.QSize(16777215,250))
        self.groupBox_2.setObjectName("groupBox_2")

        self.vboxlayout1 = QtGui.QVBoxLayout(self.groupBox_2)
        self.vboxlayout1.setObjectName("vboxlayout1")

        self.compile = QtGui.QPushButton(self.groupBox_2)
        self.compile.setObjectName("compile")
        self.vboxlayout1.addWidget(self.compile)

        self.generate = QtGui.QPushButton(self.groupBox_2)
        self.generate.setObjectName("generate")
        self.vboxlayout1.addWidget(self.generate)

        self.render = QtGui.QPushButton(self.groupBox_2)
        self.render.setObjectName("render")
        self.vboxlayout1.addWidget(self.render)
        self.gridlayout.addWidget(self.groupBox_2,1,0,1,1)

        self.UserOut = QtGui.QTabWidget(self.centralwidget)
        self.UserOut.setMaximumSize(QtCore.QSize(16777215,250))
        self.UserOut.setObjectName("UserOut")

        self.messages = QtGui.QWidget()
        self.messages.setObjectName("messages")

        self.vboxlayout2 = QtGui.QVBoxLayout(self.messages)
        self.vboxlayout2.setObjectName("vboxlayout2")

        self.MessageView = QtGui.QTextBrowser(self.messages)
        self.MessageView.setObjectName("MessageView")
        self.vboxlayout2.addWidget(self.MessageView)
        self.UserOut.addTab(self.messages,"")

        self.error = QtGui.QWidget()
        self.error.setObjectName("error")

        self.vboxlayout3 = QtGui.QVBoxLayout(self.error)
        self.vboxlayout3.setObjectName("vboxlayout3")

        self.ErrorView = QtGui.QTextBrowser(self.error)
        self.ErrorView.setObjectName("ErrorView")
        self.vboxlayout3.addWidget(self.ErrorView)
        self.UserOut.addTab(self.error,"")

        self.strings = QtGui.QWidget()
        self.strings.setObjectName("strings")

        self.vboxlayout4 = QtGui.QVBoxLayout(self.strings)
        self.vboxlayout4.setObjectName("vboxlayout4")

        self.StringView = QtGui.QTextBrowser(self.strings)
        self.StringView.setObjectName("StringView")
        self.vboxlayout4.addWidget(self.StringView)
        self.UserOut.addTab(self.strings,"")
        self.gridlayout.addWidget(self.UserOut,1,1,1,1)
        MainWindow.setCentralWidget(self.centralwidget)

        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0,0,980,22))
        self.menubar.setObjectName("menubar")

        self.menuFile = QtGui.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        MainWindow.setMenuBar(self.menubar)

        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.toolBar = QtGui.QToolBar(MainWindow)
        self.toolBar.setObjectName("toolBar")
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea,self.toolBar)

        self.actionOpen = QtGui.QAction(MainWindow)
        self.actionOpen.setIcon(QtGui.QIcon(":/general/fileopen.png"))
        self.actionOpen.setObjectName("actionOpen")

        self.actionNew = QtGui.QAction(MainWindow)
        self.actionNew.setIcon(QtGui.QIcon(":/general/filenew.png"))
        self.actionNew.setObjectName("actionNew")

        self.actionSaveAs = QtGui.QAction(MainWindow)
        self.actionSaveAs.setIcon(QtGui.QIcon(":/general/filesaveas.png"))
        self.actionSaveAs.setObjectName("actionSaveAs")

        self.actionSave = QtGui.QAction(MainWindow)
        self.actionSave.setIcon(QtGui.QIcon(":/general/filesave.png"))
        self.actionSave.setObjectName("actionSave")

        self.actionClose = QtGui.QAction(MainWindow)
        self.actionClose.setIcon(QtGui.QIcon(":/general/exit.png"))
        self.actionClose.setObjectName("actionClose")
        self.menuFile.addAction(self.actionNew)
        self.menuFile.addAction(self.actionOpen)
        self.menuFile.addAction(self.actionSave)
        self.menuFile.addAction(self.actionSaveAs)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionClose)
        self.menubar.addAction(self.menuFile.menuAction())
        self.toolBar.addAction(self.actionNew)
        self.toolBar.addAction(self.actionOpen)
        self.toolBar.addAction(self.actionSaveAs)
        self.toolBar.addAction(self.actionSave)
        self.toolBar.addAction(self.actionClose)

        self.retranslateUi(MainWindow)
        self.UserOut.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtGui.QApplication.translate("MainWindow", "MainWindow", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("MainWindow", "Contexts", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("MainWindow", "Grammars", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("MainWindow", "Generations", None, QtGui.QApplication.UnicodeUTF8))
        self.label_4.setText(QtGui.QApplication.translate("MainWindow", "Save Image As:", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox_2.setTitle(QtGui.QApplication.translate("MainWindow", "Actions", None, QtGui.QApplication.UnicodeUTF8))
        self.compile.setText(QtGui.QApplication.translate("MainWindow", "Compile", None, QtGui.QApplication.UnicodeUTF8))
        self.generate.setText(QtGui.QApplication.translate("MainWindow", "Generate", None, QtGui.QApplication.UnicodeUTF8))
        self.render.setText(QtGui.QApplication.translate("MainWindow", "Render", None, QtGui.QApplication.UnicodeUTF8))
        self.UserOut.setTabText(self.UserOut.indexOf(self.messages), QtGui.QApplication.translate("MainWindow", "Messages", None, QtGui.QApplication.UnicodeUTF8))
        self.UserOut.setTabText(self.UserOut.indexOf(self.error), QtGui.QApplication.translate("MainWindow", "Error", None, QtGui.QApplication.UnicodeUTF8))
        self.UserOut.setTabText(self.UserOut.indexOf(self.strings), QtGui.QApplication.translate("MainWindow", "Strings", None, QtGui.QApplication.UnicodeUTF8))
        self.menuFile.setTitle(QtGui.QApplication.translate("MainWindow", "File", None, QtGui.QApplication.UnicodeUTF8))
        self.toolBar.setWindowTitle(QtGui.QApplication.translate("MainWindow", "toolBar", None, QtGui.QApplication.UnicodeUTF8))
        self.actionOpen.setText(QtGui.QApplication.translate("MainWindow", "Open", None, QtGui.QApplication.UnicodeUTF8))
        self.actionOpen.setShortcut(QtGui.QApplication.translate("MainWindow", "Ctrl+O", None, QtGui.QApplication.UnicodeUTF8))
        self.actionNew.setText(QtGui.QApplication.translate("MainWindow", "New", None, QtGui.QApplication.UnicodeUTF8))
        self.actionNew.setShortcut(QtGui.QApplication.translate("MainWindow", "Ctrl+N", None, QtGui.QApplication.UnicodeUTF8))
        self.actionSaveAs.setText(QtGui.QApplication.translate("MainWindow", "Save As", None, QtGui.QApplication.UnicodeUTF8))
        self.actionSaveAs.setIconText(QtGui.QApplication.translate("MainWindow", "Save As", None, QtGui.QApplication.UnicodeUTF8))
        self.actionSaveAs.setShortcut(QtGui.QApplication.translate("MainWindow", "Ctrl+Shift+S", None, QtGui.QApplication.UnicodeUTF8))
        self.actionSave.setText(QtGui.QApplication.translate("MainWindow", "Save", None, QtGui.QApplication.UnicodeUTF8))
        self.actionSave.setShortcut(QtGui.QApplication.translate("MainWindow", "Ctrl+S", None, QtGui.QApplication.UnicodeUTF8))
        self.actionClose.setText(QtGui.QApplication.translate("MainWindow", "Close", None, QtGui.QApplication.UnicodeUTF8))
        self.actionClose.setShortcut(QtGui.QApplication.translate("MainWindow", "Ctrl+Q", None, QtGui.QApplication.UnicodeUTF8))

import metaphor_rc
