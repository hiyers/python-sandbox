import random

def nim_random(sticks):
    if sticks==0:
        raise Exception('ERROR : You cannot have 0 sticks!!!')
    if sticks<3:
        return random.randint(1,sticks)
    else:
        return random.randint(1,3)
