compile = 'examples/ncur.gr'

context = 'contexts/turtle.py'

generate = [('Sierpinski2', 2),
            ('Sierpinski4', 4),
            ('Sierpinski6', 6),
            ('Sierpinski9', 9)]


render = []

for x in range(1,5):
    fname = "tri"+str(x)+".png"
    render.append(fname)
    
#render = ['dragon.png', ('curve.png', 'contexts/turtle.py')]
