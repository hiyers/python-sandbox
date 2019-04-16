import sys
print('Sys Version',sys.version)
print(sys.getrecursionlimit())
def ackermann(m,n):
    if m==0 :
        return n+1
    if m>0 and n==0 :
        return ackermann(m-1,1)
    if m>0 and n>0 :
        return ackermann(m-1,ackermann(m,n-1))
