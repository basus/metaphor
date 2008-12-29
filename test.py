import syntax
import semantics

fl = open('param.gr')
parse = syntax.Parser(fl)
root = parse.parse()
builder = semantics.Builder(root)

genv = semantics.Environment(builder)
genv.populate()
print genv.list_grammars()

tree = genv.grammars['tree']
print tree.assigns

def gen(num):
    for x in range(num):
        print tree.generate(x)
