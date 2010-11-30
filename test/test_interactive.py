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

from metaphor.core import system
from metaphor.core import parser as p

fl = open("examples/parametric.lsys")
st = ""

for line in fl:
    st += line

p.lex.input(st)
root = p.parser.parse(st)
builder = system.Builder(root)
s = builder.build_system()
f = s.transform(system.Symbol('F',[0]))
f1 = s.transform(f[0])
print "For F(1)"
for i in f1:
    print i.symbol, i.params

def prob():
    x = s.transform(system.Symbol('F', [2]))
    for i in x:
        print i.symbol, i.params
