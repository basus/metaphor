import os
import sys
import getopt
from metaphor import script

def main(argv):
    try:
        opts, args = getopt.getopt(argv, "s:", ["script="])
    except getopt.GetoptError:
        usage()
        sys.exit(2)

    for opt, arg in opts:
        if opt in ('-s', '--script'):
            path = os.getcwd() + '/' + arg
            interface = script.PyScriptInterface(path)
            interface.run()

    if opts == []:
        print "You must use the script mode for the time being. Sorry!"
            
        
if __name__ == '__main__':
    sys.path.insert(0, os.getcwd())
    main(sys.argv[1:])
