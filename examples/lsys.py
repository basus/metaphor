compile = 'examples/lsys.gr'

context = 'contexts/turtle.py'

generate = []

for x in range(1, 10):
    tup = ('Sierpinski', x)
    generate.append(tup)
    
#generate = [('Dragon', 10), ('KochCurve',3)]

render = []

for x in range(1,10):
    fname = "tri"+str(x)+".png"
    render.append(fname)
    
#render = ['dragon.png', ('curve.png', 'contexts/turtle.py')]
