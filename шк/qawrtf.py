'''
a=1
while True :
    for x in range(1000):
        for y in range(1000):
            if not ((x+2*y<a) or (y>x) or (x>20)):
                break
        else:
            continue
        break
    else:
        print(a)
    a+=1
'''
'''
a=1
while True:
    for x in range(1000):
        if not(( x&25!=0)<=((x&19==0)<=(x&a!=0))):
            break
    else:
        print(a)
            
    a+=1
'''
'''
a=1
while True:
    for x in range(1000):
        if not( (x&25!=0)<=((x&17==0)<=(x&a!=0))):
            break
    else:
        print(a)
        break
    a+=1
   '''
'''
a=1
while True:
    for x in range(1000):
        for y in range(1000):
            if not(( (x<=9)<=((x*x<=a))) and (((y*y<=a)<=(y<=9)))):
                break
        else:
            continue
        break
    else:
        print(a)
    a+=1
'''
'''
a=1
while True:
    for x in range(1000):
        for y in range(1000):
            if not(((x<6)<=(x**2<a)) and (((y**2<=a)<=(y<=6)))):
                break
        else:
            continue
        break
    else:
        print(a)
    a+=1
'''
'''
def delit(n):
    dels=[1]
    d=1
    while d**2<=n:
        if n%d==0 :
            dels.append(d)
            if n//d>d:
                dels.append(n//d)
        d+=2
    return dels
for i in range(95632,95651):
    e=0
    for q in delit(i):
        if q%2==1:
            e+=1
        if q%2!=1 or e>6:
            break
    else:
        if e==6:
            print(i,*sorted(delit(i)))
'''

for x in range(95632,95651):
    d=[]
    for i in range(1,x+1,2):
        if x%i==0 :
            d.append(i)
    if len(d)==6:
        print(*d)

'''
def delit(n):
    dels=[]
    d=1
    while d**2<=n:
        if n%d==0:
            dels.append(d)
            if n//d>d :
                dels.append(n//d)
        d+=1
    return dels
print(delit(34),'123')
for x in range(95632,95651):
    e=0
    ans=[]
    for i in delit(x):
        if i%2==1:
            ans.append(i)
            e+=1
        if e>6:
            break
    else:
        if e==6:
            print(*sorted(ans))
'''
