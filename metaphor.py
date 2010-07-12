import os
import sys
import getopt
from metaphor.ui import script

def main(argv):
    """

    This is the main function controlling interface to the Metaphor system.
    Based on command line parameters it either launches the GUI or feeds a
    script to the script interface.

    @param argv: the command line arguments passed to the program
    
    """
    try:
        opts, args = getopt.getopt(argv, "s:q", ["script="])
    except getopt.GetoptError:
        usage()
        sys.exit(2)

    for opt, arg in opts:
        if opt in ('-s', '--script'):
            path = os.getcwd() + '/' + arg
            interface = script.PyScriptInterface(path)
            interface.run()
        elif opt in ('-q', '--qtinterface'):
            qt_mode()

    if opts == []:
        from metaphor import gui
    
            
        
if __name__ == '__main__':
    sys.path.insert(0, os.getcwd())
    main(sys.argv[1:])
