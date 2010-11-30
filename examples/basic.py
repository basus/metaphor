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
