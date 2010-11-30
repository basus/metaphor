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
from metaphor.core import context
from metaphor.core import system

class CLInterface:
    """
    Implements the basic command line interface. Takes the parsed options
    provided by the starter script and runs the backend appropriately.
    """
    
    def __init__(self,src,sys,gen,cont,ren):
        """
        Takes the required commandline parameters and creates an Environment
        for the grammars

        @param src: The filepath fo the Lsystem declaration code
        @param sys: The Lsystem to be used
        @param gen: The number of generations to iterate for
        @param cont: The context used to render
        @param ren: The output filepath
        """
        self.src = src
        self.system = sys
        self.generations = gen
        self.context = cont
        self.render = ren
        self.env = system.Environment()

    def run(self):
        """
        Runs the Metaphor engine and creates the output file
        """
        src = os.path.abspath(self.src)
        context = os.path.abspath(self.context)
        self.env.add_from_file(src)
        self.env.add_context_from_file(context)
        self.env.generate(self.system,self.generations)
        self.env.render(save=self.render)
