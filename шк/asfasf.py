f=open('27.txt','r')
f.readline()
ms=[]
for i in f:
    ms.append(int(i))
def f(n):
    dels=[]
    d=2
    while d**2<=n:
        if n%d==0:
            dels.append(d)
            if n//d>d:
                dels.append(n//d)
        d+=1
    return dels
def check(h):
    for i in f(h):
        if f(i)==[]:
            return True
    return False
s=ms[:4]
count=0
for i in range(5,len(ms)):
    for j in s:
        if check(j*ms[i]):
            count+=1
    s.reverse()
    s.pop()
    s.reverse()
    s.append(ms[i])
print(count)








































#15
a=1
while True:
    for x in range(1000):
        for y in range(1000):
            if not(условие):
                break
        else:
            continue
        break
    else:
        print(a)
    a+=1
