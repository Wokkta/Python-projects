from math import sqrt
def f(n,start):
    if n<start:
        return 0
    if n==start:
        return 1
    s=f(n-1,start)
    s+=f(n-3,start)
    if sqrt(n)==n**0.5:
        s+=f(sqrt(n),start)
    return s
print(f(19,2))
