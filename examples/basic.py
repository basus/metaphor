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

compile = 'examples/basic.lsys'

context = 'contexts/turtle.py'

generate = []

render = []

# For Fractal plants
for x in range(1, 7):
    tup = ('FractalPlant', x)
    generate.append(tup)
    fname = 'plant' + str(x) + '.png'
    render.append(fname)


# For Cantor dust
for x in range(1,10):
    tup = ('CantorDust', x)
    generate.append(tup)
    fname = 'cantor' + str(x) + '.png'
    render.append(fname)

# For Koch Curve
for x in range(1,7):
    tup = ('KochCurve', x)
    generate.append(tup)
    fname = 'koch' + str(x) + '.png'
    render.append(fname)

# For Sierpinski Triangle
for x in range(1,10):
    tup = ('Sierpinski', x)
    generate.append(tup)
    fname = 'sierpinski' + str(x) + '.png'
    render.append(fname)

# For dragon curve
for x in range(1,10):
    tup = ('Dragon', x)
    generate.append(tup)
    fname = 'dragon' + str(x) + '.png'
    render.append(fname)
