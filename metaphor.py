# This file is part of Metaphor.

# Metaphor is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.

# Metaphor is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.

# You should have received a copy of the GNU General Public License
# along with Metaphor.  If not, see <http://www.gnu.org/licenses/>.

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

    # Run unit tests
    parser.add_option("-t", "--test", dest="test", action="store_true",
                      help="Run all unit tests using the nose framework")
    
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

    # QT interface
    parser.add_option("-q", "--qt", dest="qt", action="store_true",
                      help="Launch the Qt interface")

    (options, args) = parser.parse_args()
    
    if options.script: 
        interface = script.PyScriptInterface(options.script)
        interface.run()
    elif options.cli:
        interface = cli.CLInterface(options.source,options.system,options.generations,
                                    options.context,options.render)
        interface.run()
    elif options.qt:
        from metaphor.ui.qt.main import run
        run()
    elif options.test:
        import nose
        nose.main()
    elif options.update:
        util.to2(options.update,options.update+'.lsys')
    else:
        print "Options required"
        
if __name__ == '__main__':
    sys.path.insert(0, os.getcwd())
    main(sys.argv[1:])
