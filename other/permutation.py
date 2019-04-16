from sort4 import *
def insertion(e,s):
    for i in range(len(s)+1):
        yield s[:i]+[e]+s[i:]


def perm(s):
    if s == []:
        yield []
    else:
        e,s1 = s[0],s[1:]
        for s1p in perm(s1):
            for p in insertion(e,s1p):
                yield p

for p in perm([1,3,66,0]):
    print((p[0],p[1],p[2],p[3]),'->',sort4(p[0],p[1],p[2],p[3]))
