import syntax
import semantics
import script

psi = script.PyScriptInterface('./examples/lsys.py')
psi.compile()
psi.setcontext()
psi.generate()
psi.render()
