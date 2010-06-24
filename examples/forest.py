compile = 'examples/forest.gr'

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

