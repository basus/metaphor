class typewriter(object):

    def __init__(self):
        self.current_name = ''
        self.stack = []
        
    def __getattr__(self, name):
        self.current_name = name
        return self.to_text

    def to_text(self, *args):
        arg = ' '.join([`x` for x in args])
        action = self.current_name + '(' + arg + ')'
        print action
        self.stack.append(action)

    def wrapup(self, fname):
        fl = open(fname, 'w')
        commands = ' '.join([x for x in self.stack]) 
        fl.write(commands)
        fl.write('\n')
        fl.close()
