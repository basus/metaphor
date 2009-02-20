from PyQt4.QtGui import *
from PyQt4.QtCore import *
from qtui import Ui_MainWindow
import sys
import os


import syntax
import semantics
import context

        
class QtInterface(QMainWindow):
    def __init__(self):
        QDialog.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ctxpath = os.getcwd() + '/contexts/'
        self.env = None
        self.guigrammars=[]
        self.savefile = 'test.png'
        self.detect_contexts()
        self.connections()

    def detect_contexts(self):
        """Looks up a folder and lists all available contexts """
        for ctxfile in os.listdir(self.ctxpath):
            if ctxfile.endswith('.py'):
                self.ui.Contexts.addItem(ctxfile)
        
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

        self.connect(self.ui.actionClose,
                     SIGNAL("activated()"),
                     qApp,
                     SLOT('quit()'))

        self.connect(self.ui.compile,
                     SIGNAL("clicked()"),
                     self.slot_compile)

        self.connect(self.ui.generate,
                     SIGNAL("clicked()"),
                     self.slot_generate)
        
        self.connect(self.ui.render,
                     SIGNAL("clicked()"),
                     self.slot_render)
        
    def slot_compile(self):
        file = open(self.filename,'w')
        file.write(self.ui.GrammarEdit.toPlainText())
        file.close()
        file = open(self.filename)
        parser = syntax.Parser(file)
        try:
            tree = parser.parse()
            builder = semantics.Builder(tree)
            self.env = semantics.Environment(builder)
            self.grammars = self.env.populate()
            self.ui.Grammars.clear()
            self.ui.Grammars.addItems(self.grammars)
            self.ui.MessageView.insertPlainText("Compilation proceeded without errors\n")
        except Exception, inst:
            print inst
            self.ui.ErrorView.setPlainText("Errors occured: \n")
            self.ui.ErrorView.setPlainText(str(inst))

    def slot_generate(self):
        grammar = str(self.ui.Grammars.currentItem().text())
        string = self.env.grammars[grammar].generate(self.ui.Generations.value())
        self.ui.StringView.setPlainText(str(string))
        self.ui.UserOut.setCurrentIndex(2)

        

    def slot_render(self):
        ctxfile = self.ctxpath + str(self.ui.Contexts.currentItem().text())
        handler = context.ContextHandler(ctxfile)
        handler.load_context()
        grammar = str(self.ui.Grammars.currentItem().text())
        string = self.env.grammars[grammar].generate(self.ui.Generations.value())
        ctxstring = self.env.grammars[grammar].map(string)
        handler.render(ctxstring)
        filename = str(self.ui.OutputName.text())
        print filename
        handler.save(filename)
        self.ui.MessageView.setPlainText("Output saved in Image file")

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
