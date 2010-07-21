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
