import random

def nim_human(sticks):
    if sticks==0:
        taken=0
        raise Exception('ERROR : You cannot have 0 sticks!!!')
    taken = int(input("Enter number of sticks between 1-3:"))
    type(taken)
    return taken
