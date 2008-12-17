import os
class ContextHandler:

    def __init__(self, context, grammars):
        self.context = context
        self.grammars = grammars

    def detect_context(self):
        import self.context as context
        if context.python:
            import context.program as program
            import context.contexts as context_dict
            for pair in self.grammars:
                if pair[0] in context_dict:
                    context_object = program.context_dict[pair[0]]()
                    self.interact_context(self, context_object, pair[1])
        else:
            os.system(context.program)


class PyContextInterface:
    ''' A class that acts as an interface to a Python Context object'''

    def __init__(self, context, genstring):
        ''' Accepts a context object and the translated string to be interpreted'''
        self.context = context
        self.genstring = string

    def create(self):
        '''Steps through the translated string and makes appropriate method calls
        on the context object'''
        for action in genstring:
            call = action.split('[')[0]
            params = action.split('[')[1]
            params = params.rstrip(']').split(',')
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
                raise ContextError(action)
            
    def save(self, filename):
        ''' Saves the result of context representation'''
        self.context.wrapup(filename)
