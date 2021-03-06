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

compile = 'examples/forest.lsys'

context = 'contexts/turtle.py'

# grammars = ['WeedFern', 'WeedTree', 'TreeWeedFern']

grammars = ['WeedFernProb']

generate = []
render = []

for x in range(1,8):
    for g in grammars:
        generate.append((g,x))

for x in range(1,8):
    for g in grammars:
        render.append(g+str(x)+".png")

