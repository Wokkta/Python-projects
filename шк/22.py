#4
'''for x in range(1,10000):
    L = 0; M = 0;z = x
    while x > 0:
        L = L + 1
        if x % 2 == 1:
            M = M + (x % 10)
        x = x // 10
    if L==3 and M==8:
        print(z)
'''
#9
'''
for x in range(1,10000):
    L = 0; M = 0
    z=x
    while x > 0:
        L = L + 1
        if (M < x) and (x % 2 == 1):
            M = (x % 10) * 2
        x = x // 10
    if L==3 and M==10:
        print(z)
'''
#11
'''
for x in range(1,10000):
    a = 0; b = 1
    z=x
    while x > 0:
        a = a + 1
        b = b * (x % 10)
        x = x // 10
    if a==2 and b==72:
        print(z)
'''
#19
'''
for x in range(1,10000):
    L = 0; M = 0
    z=x
    while x > 0:
        L = L + 1
        if x % 2 == 0:
            M = M + (x % 10) // 2
        x = x // 10
    if L==3 and M==7:
        print(z)
        break
'''
#30
'''
for x in range(1,10000):
    z=x
    a = 0; b = 1
    while x > 0:
        a = a + 1
        b = b * (x % 8)
        x = x // 8
    if a==3 and b==10:
        print(z)
        break
'''
#31
'''
for x in range(1,10000):
    z=x
    a = 0; b = 1
    while x > 0:
        a = a + 1
        b = b * (x % 6)
        x = x // 6
    if a==3 and b==6:
        print(z)
        break
'''
#32
'''
for x in range(1,10000):
    z=x
    a = 0; b = 1
    while x > 0:
        a = a + 1
        b = b * (x % 5)
        x = x // 5
    if a==3 and b==9:
        print(z)
'''
#40
'''
for i in range(1,10000):
    for q in range(1,10000):
        x=i
        y=q
        if (y > x):
            z = x
            x = y
            y = z
        a = x; b = y
        while b > 0:
            r = a % b
            a = b
            b = r
        if a==13 and x==65:
            print(a,x,y)
'''
#53
'''
for x in range(1,10000):
    z=x
    K = 0; R = 9
    y = x % 10
    while x > 0:
        K = K + 1
        if R > (x % 10):
            R = x % 10
        x = x // 10
    R = y - R
    if K==4 and R==3:
        print(z)
        break
'''
#68
'''
for x in range(1,10000):
    z=x
    L = 0; M = 0
    while x > 0:
        M = M + 1
        if x % 2 != 0:
            L = L + 1
        x = x // 2
    if L==3 and M==6:
        print(z)
        break
'''
#74
'''
for x in range(101,10000):
    z=x
    L = x - 30
    M = x + 30
    while L != M:
        if L > M:
            L = L - M
        else:
            M = M - L 
    if M==30:
        print(z)
        break
'''
#82
'''
for x in range(101,10000):
    z=x
    L = x - 16
    M = x + 32
    while L != M:
        if L > M:
            L = L - M
        else:
            M = M - L
    if M==4:
        print(z)
        break
'''
