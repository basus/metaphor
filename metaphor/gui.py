from PyQt4.QtGui import *
from PyQt4.QtCore import *
from qtui import Ui_MainWindow
import sys
import os


import syntax
import semantics

class GrammarListModel(QAbstractListModel):
    """ """
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
        
class ContextListModel(QAbstractListModel):
    """ """
    def __init__(self, contexts, parent=None, *args):
        QAbstractListModel.__init__(self, parent, *args)
        self.contexts = contexts

    def rowCount(self, parent):
        return len(self.contexts)

    def columnCount(self, parent):
        return 1
    
    def data(self, index, role):
        if index.isValid() and role == Qt.DisplayRole:
            return QVariant(self.contexts[index.row()])
        else:
            return QVariant()

        
class QtInterface(QMainWindow):
    def __init__(self):
        QDialog.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ctxpath = os.getcwd() + '/contexts/'
        self.ctxfiles = []
        self.env = None
        self.guigrammars=[]
        self.savefile = 'test.png'
        self.detect_contexts()
        self.connections()

    def detect_contexts(self):
        """Looks up a folder and lists all available contexts """
        for ctxfile in os.listdir(self.ctxpath):
            if ctxfile.endswith('.py'):
                self.ctxfiles.append(ctxfile)
        self.contextlist = ContextListModel(self.ctxfiles, self)
        self.ui.Contexts.setModel(self.contextlist)
        
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

        self.connect(self.ui.render,
                     SIGNAL("clicked()"),
                     self.slot_render)
        
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
        self.glist = GrammarListModel(self.grammars, self)
        self.ui.Grammars.setModel(self.glist)

    def slot_render(self):
        print self.ui.Grammars.currentItem()
        print currentcontext
        ctxfile = self.ctxpath + currentcontext
        handler = context.ContextHandler(ctxfile)
        handler.load_context()
        string = self.env.grammars[self.current_grammar].generate(self.ui.Generations.value())
        ctxstring = self.env.grammars[self.current_grammar].translate()
        handler.render()
        handler.save(self.savefile)

    def slot_setcontext(self, selected, deselected):
        print selected
        self.current_context = selected
        
    def slot_setgrammar(self, selected, deselected):
        print selected
        self.current_grammar = selected
        
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
