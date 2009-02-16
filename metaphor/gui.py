from PyQt4.QtGui import *
from PyQt4.QtCore import *
from qtui import Ui_MainWindow
import sys
import os


import syntax
import semantics

class GrammarList(QAbstractListModel):
    def __init__(self, grammars, parent=None, *args):
        QAbstractListModel.__init__(self, parent, *args)
        self.grammars = grammars

    def rowCount(self, parent):
        return len(self.grammars)

    def columnCount(self, parent):
        return 1

    def data(self, index, role):
        if index.isValid() and role == Qt.DisplayRole:
            return QVariant(self.grammars[index.row()])
        else:
            return QVariant()

class QtInterface(QMainWindow):
    def __init__(self):
        QDialog.__init__(self)

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.connections()
        self.env = None
        self.guigrammars=[]

    def connections(self):
        self.connect(self.ui.actionOpen,
                     SIGNAL("activated()"),
                     self.slot_open_file)

        self.connect(self.ui.actionSaveAs,
                     SIGNAL("activated()"),
                     self.slot_saveas_file)

        self.connect(self.ui.actionSave,
                     SIGNAL("activated()"),
                     self.slot_save_current)

        self.connect(self.ui.compile,
                     SIGNAL("clicked()"),
                     self.slot_compile)

    def slot_compile(self):
        file = open(self.filename,'w')
        file.write(self.ui.GrammarEdit.toPlainText())
        file.close()
        file = open(self.filename)
        parser = syntax.Parser(file)
        tree = parser.parse()
        builder = semantics.Builder(tree)
        self.env = semantics.Environment(builder)
        self.grammars = self.env.populate()
        print self.grammars
        self.glist = GrammarList(self.grammars, self)
        self.ui.Grammars.setModel(self.glist)
        print self.glist
#        self.ui.Grammars.show()
        print "Grammars displayed"
#        for grammar in self.grammars:
#            self.guigrammars.append(QListViewItem(self.ui.Grammars, grammar))
        

    def slot_open_file(self):
        self.filename = QFileDialog.getOpenFileName(self, "Open File",os.getcwd(), "*.gr")
        file = open(self.filename)
        data = file.read()
        self.ui.GrammarEdit.setText(data)

    def slot_saveas_file(self):
        self.filename = QFileDialog.getSaveFileName(self, "Save File",os.getcwd(), "*.gr")
        file = open(self.filename,'w','utf-8')
        file.write(self.ui.GrammarEdit.toPlainText())
        file.close()

    def slot_save_current(self):
        pass
        

app = QApplication(sys.argv)
window = QtInterface()


window.show()
sys.exit(app.exec_())
