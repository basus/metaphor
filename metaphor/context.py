import os
import sys
import imp
import error
class ContextHandler:

    def __init__(self, contextpath):
        self.contextpath = contextpath

    def load_context(self):
        try:
            module = imp.load_source('', self.contextpath)
        except Exception, inst:
            print inst
            raise error.InvalidContextError(self.contextpath)
        
        contextname = self.contextpath.split('/')[-1]
        contextname = contextname.rstrip(".py")
        try:
            self.context = getattr(module, contextname)()
        except error.ContextError, inst:
            print inst

    def render(self, genstring):
        '''Steps through the translated string and makes appropriate method calls
        on the context object'''
        for action in genstring:
            call = action.split('[')[0]
            try:
                params = action.split('[')[1]
                params = params.rstrip(']').split(',')
            except:
                params = []
            parsed_params = []
            for param in params:
                if param.isdigit():
                    parsed_params.append(int(param))
                else:
                    parsed_params.append(param)
            try:
                call = getattr(self.context, call)
                call(*parsed_params)
            except:
                raise error.ContextError(action)

    def save(self, filename):
        ''' Saves the result of context representation'''
        self.context.wrapup(filename)


            
