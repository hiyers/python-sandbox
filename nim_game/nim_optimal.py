import random

def nim_optimal(sticks):
    if sticks==0:
        raise Exception('ERROR : You cannot have 0 sticks!!!')

    taken=sticks%4
    if taken==0: 
        taken=random.randint(1,min(sticks,3))
        
    return taken
