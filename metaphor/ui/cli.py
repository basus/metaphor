import os
from metaphor.core import context
from metaphor.core import system

class CLInterface:
    def __init__(self,src,sys,gen,cont,ren):
        self.src = src
        self.system = sys
        self.generations = gen
        self.context = cont
        self.render = ren
        self.env = system.Environment()

    def run(self):
        src = os.path.abspath(self.src)
        context = os.path.abspath(self.context)
        self.env.add_from_file(src)
        self.env.add_context_from_file(context)
        self.env.generate(self.system,self.generations)
        self.env.render(save=self.render)
