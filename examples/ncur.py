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

compile = 'examples/ncur.gr'

context = 'contexts/turtle.py'

generate = [('Sierpinski2', 2),
            ('Sierpinski4', 4),
            ('Sierpinski6', 6),
            ('Sierpinski9', 9)]

for x in range(1, 7):
    tup = ('Simple', x*5)
    generate.append(tup)


render = []

for x in range(1,5):
    fname = "tri"+str(x)+".png"
    render.append(fname)

for x in range(1,7):
    fname = "simp"+str(x)+".png"
    render.append(fname)

