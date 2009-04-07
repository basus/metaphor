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

    
#render = ['dragon.png', ('curve.png', 'contexts/turtle.py')]
