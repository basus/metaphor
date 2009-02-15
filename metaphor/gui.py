from PyQt4 import QtGui, QtCore
from qtui import Ui_MainWindow
import sys
import os
import codecs

import syntax
import semantics
                     

class QtInterface(QtGui.QMainWindow):
    def __init__(self):
        QtGui.QDialog.__init__(self)

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.connections()
        self.env = None
        self.guigrammars=[]

    def connections(self):
        self.connect(self.ui.actionOpen,
                     QtCore.SIGNAL("activated()"),
                     self.slot_open_file)

        self.connect(self.ui.actionSaveAs,
                     QtCore.SIGNAL("activated()"),
                     self.slot_saveas_file)

        self.connect(self.ui.actionSave,
                     QtCore.SIGNAL("activated()"),
                     self.slot_save_current)

        self.connect(self.ui.compile,
                     QtCore.SIGNAL("clicked()"),
                     self.slot_compile)

    def slot_compile(self):
        file = open(self.filename,'w')
        print self.ui.GrammarEdit.toPlainText()
        file.write(self.ui.GrammarEdit.toPlainText())
        file.close()
        file = open(self.filename)
        parser = syntax.Parser(file)
        tree = parser.parse()
        builder = semantics.Builder(tree)
        self.env = semantics.Environment(builder)
        self.grammars = self.env.populate()
        for grammar in self.grammars:
            self.guigrammars.append(QtGui.QListViewItem(self.ui.Grammars, grammar))
        

    def slot_open_file(self):
        self.filename = QtGui.QFileDialog.getOpenFileName(self, "Open File",os.getcwd(), "*.gr")
        file = open(self.filename)
        data = file.read()
        self.ui.GrammarEdit.setText(data)

    def slot_saveas_file(self):
        self.filename = QtGui.QFileDialog.getSaveFileName(self, "Save File",os.getcwd(), "*.gr")
        file = open(self.filename,'w','utf-8')
        file.write(self.ui.GrammarEdit.toPlainText())
        file.close()

    def slot_save_current(self):
        pass
        

app = QtGui.QApplication(sys.argv)
window = QtInterface()


window.show()
sys.exit(app.exec_())
