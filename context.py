import os
import sys
import imp
import error
class ContextHandler:

    def __init__(self, context):
        self.context = context

    def get_context(self, path=None):
        try:
            fl, pathname, desc = imp.find_module(self.context, path)
            module = imp.load_module(self.context, fl, pathname, desc)
            ctxclass = getattr(module, self.context)
            handler = PyContextHandler(ctxclass())
            return handler
        except Exception as inst:
            print inst
            raise error.InvalidContextError(self.context)
            

class PyContextHandler:
    ''' A class that acts as an interface to a Python Context object'''

    def __init__(self, context):
        ''' Accepts a context object and the translated string to be interpreted'''
        self.context = context


    def create(self, genstring):
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
