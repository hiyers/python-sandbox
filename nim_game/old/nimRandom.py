import random

def nimRandom(sticks):
    
    taken=random.randint(1,3)     
    if sticks==0:
        taken=0
        print('ERROR : You cannot have 0 sticks!!!')
        return taken
    if taken<=sticks:
        sticks=sticks-taken
    else:
        taken=1
        sticks=sticks-taken
    return taken
