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

class typewriter(object):

    def __init__(self):
        self.current_name = ''
        self.stack = []
        
    def __getattr__(self, name):
        self.current_name = name
        return self.to_text

    def to_text(self, *args):
        arg = ' '.join([`x` for x in args])
        action = self.current_name + '(' + arg + ')'
        print action
        self.stack.append(action)

    def wrapup(self, fname):
        fl = open(fname, 'w')
        commands = ' '.join([x for x in self.stack]) 
        fl.write(commands)
        fl.write('\n')
        fl.close()
