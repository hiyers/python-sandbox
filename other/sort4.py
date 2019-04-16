def sort(x,y):
    return min(x,y),max(x,y)


def sort4(x,y,a,b):
    #print('running sort4',x,y,a,b)
    if x<y and y<a and a<b:
        return x,y,a,b
    else:
        if x>y:
            x,y=sort(x,y)
            return sort4(x,y,a,b)
        elif y>a:
            y,a=sort(y,a)
            return sort4(x,y,a,b)
        elif a>b:
            a,b=sort(a,b)
            return sort4(x,y,a,b)
        else:
            return x,y,a,b
