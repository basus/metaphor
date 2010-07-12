from PyQt4.QtGui import *
from PyQt4.QtCore import *

import sys
import os


import syntax
import semantics
import context
from error import *
from qtui import Ui_MainWindow
        
class QtInterface(QMainWindow):
    """
    Main graphical interface class. Mostly a text editor with displays for available
    contexts and compiled grammars. Build on PyQt.
    """
    
    def __init__(self):
        """
        Sets up the main interface, loads the list of contexts and sets up environments
        for the grammar
        """
        
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
        """Looks up a folder and lists all available contexts. The default folder is
        the /contexts/ folder in the current directory.
        """
        for ctxfile in os.listdir(self.ctxpath):
            if ctxfile.endswith('.py'):
                self.ui.Contexts.addItem(ctxfile)
        
    def connections(self):
        """
        Connects all required slots and signals to the GUI elements.
        """
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
        """
        Executed when the 'compile' button is clicked. The currently open file is used
        as input to the parser. Correctly compiled grammars are then added to the
        display list.
        """
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
            self.ui.ErrorView.setPlainText("Errors occured: \n")
            self.ui.ErrorView.insertPlainText(str(inst))
            self.ui.UserOut.setCurrentIndex(1)

    def slot_generate(self):
        """
        Executed when the 'generate' button is clicked. Generates the string for
        the selected grammar and specified number of generations.
        """
        grammar = str(self.ui.Grammars.currentItem().text())
        string = self.env.grammars[grammar].generate(self.ui.Generations.value())
        self.ui.StringView.setPlainText(str(string))
        self.ui.UserOut.setCurrentIndex(2)

        

    def slot_render(self):
        """
        Executed when the 'render' button is clicked. A string from the selected
        grammar for the selected number of generations is selected. The selected
        context module is dynamically loaded and the generated string is then
        rendered and saved.
        """
        try:
            ctxfile = self.ctxpath + str(self.ui.Contexts.currentItem().text())
            handler = context.ContextHandler(ctxfile)
            handler.load_context()
            grammar = str(self.ui.Grammars.currentItem().text())
            string = self.env.grammars[grammar].generate(self.ui.Generations.value())
            ctxstring = self.env.grammars[grammar].map(string)
            handler.render(ctxstring)
            filename = str(self.ui.OutputName.text())
            handler.save(filename)
            self.ui.MessageView.insertPlainText("Output saved in file: " + filename)
            self.ui.MessageView.setCurrentIndex(0)
        except Exception, inst:
            self.ui.ErrorView.setPlainText("Errors occured: \n")
            self.ui.ErrorView.insertPlainText(str(inst))
            self.ui.UserOut.setCurrentIndex(1)
            

    def slot_setcontext(self, selected, deselected):
        """
        Sets the currently selected context.
        """
        print selected
        self.current_context = selected
        
    def slot_setgrammar(self, selected, deselected):
        """
        Sets the currently selected compiled Grammar 
        """
        print selected
        self.current_grammar = selected
        
    def slot_open_file(self):
        """
        Launches a file selection dialog and shows the text in the text editor
        """
        self.filename = QFileDialog.getOpenFileName(self, "Open File",os.getcwd(), "*.gr")
        file = open(self.filename)
        data = file.read()
        self.ui.GrammarEdit.setText(data)

    def slot_saveas_file(self):
        """
        Opens a file saving dialog and writes the contents of the text editor.
        """
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