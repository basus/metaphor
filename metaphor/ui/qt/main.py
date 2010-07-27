
from PyQt4.QtGui import *
from PyQt4.QtCore import *

import sys

from metaphorGUI import metaphorGUI

def run():
    app = QApplication(sys.argv)
    window = metaphorGUI()
    window.show()
    sys.exit(app.exec_())
    
if __name__ == '__main__':
    run()
