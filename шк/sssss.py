'''
for x in range(2):
    for y in range(2):
        for w in range(2):
            for z in range(2):
                if (((not x)*y)==z)*w:
                    print(x,y,w,z)
'''
for z in range(1000):
    s=z
    n=2
    while s//n>0:
        s-=5
        n+=2
    if n==20:
        print(z)
s='24   23'
print(s.expandtabs(0))
