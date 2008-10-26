src = open('patlang')
txt = src.read().split()
index = 0
symbtable = ['tree:', 'is', 'Flowering', 'Oak']

def get_token():
    token = txt[index]
    index += 1
    return token

def program():
    
    while True:
        token = get_token()
        if token == 'pattern':
            pattern()
            print 'pattern ended'
            print 


def pattern():
    token = get_token()
    if token in symbtable:
        print 'in pattern'
        print token
    if token == 'end':
        return
