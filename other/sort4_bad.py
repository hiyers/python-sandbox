

def sort(x,y):
    return min(x,y),max(x,y)


def sort4(x,y,a,b):
    a,b = sort(x,y),sort(a,b)
    p,q = sort(a,b)
    x,y= p
    a,b= q
    return x,y,a,b
