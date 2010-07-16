import os
import sys
from optparse import OptionParser
from metaphor.ui import cli
from metaphor.ui import script
from metaphor.core import util

def main(argv):
    """

    This is the main function controlling interface to the Metaphor system.
    Based on command line parameters it launches one of the supported interfaces.
    Currently supports the script and command line interfaces

    @param argv: the command line arguments passed to the program
    
    """
    parser = OptionParser()

    # Update Lsystem declaration file
    parser.add_option("-u", "--update", dest="update",
                      help="Update the given declaration file to the current syntax")

    # Python Script Interface
    parser.add_option("-s", "--script",dest="script",
                      help="Use the supplied Python script to run Metaphor")

    # Command line interface
    parser.add_option("-c", "--cli", dest="cli", action="store_true",
                      help="Use Metaphor as a command-line tool")
    parser.add_option("--source",dest="source")
    parser.add_option("--system",dest="system")
    parser.add_option("--generations",dest="gen", type="int")
    parser.add_option("--context",dest="context")
    parser.add_option("--render",dest="render")

    (options, args) = parser.parse_args()
    
    if options.script: 
        interface = script.PyScriptInterface(options.script)
        interface.run()
    elif options.cli:
        interface = cli.CLInterface(options.source,options.system,options.generations,
                                    options.context,options.render)
        interface.run()
    elif options.update:
        util.to2(update,update+'.lsys')
    else:
        print "Options required"
        
if __name__ == '__main__':
    sys.path.insert(0, os.getcwd())
    main(sys.argv[1:])
