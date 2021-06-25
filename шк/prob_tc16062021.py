#2
'''
for x in range(2):
    for y in range(2):
        for w in range(2):
            for z in range(2):
                if not( not(z and not w)or ((not z or w)==(not x or y))):
                    print(x,y,w,z)
'''
#14
'''
x=4**525-2**311+2**571-48
s=''
while x>0:
    s+=str(x%4)
    x//=4
print(s.count('1'))
'''
#16
'''
def f(n):
    if n==1 or n==2:
        return n
    if n>2 and n%2==0:
        return (n+f(n-2))//5
    elif n>2:
        return (2*n+f(n-1)+f(n-2))//4
    
print(f(50))
'''
#17
'''
mini=0
count=0
for i in range(1206,14994):
    if i%3!=0 and i%4!=0 and i%5!=0 and str(i)[-1]=='3' or str(i)[-1]=='6':
        if mini==0:
            mini= i
        count+=1
print(count,mini)
'''
#6
'''
i=0
flag=1
while flag:
    s=i
    n=1
    while s<94:
        s+=8
        n*=2
    if n==32:
        print(i)
    i+=1
'''
#12
'''
s='9'*100+'1'*14+'2'*48
while '999' in s or '22' in s:
    if '999' in s:
        s=s[:s.index('999')]+'12'+s[s.index('999')+3:]
    else:
        s=s[:s.index('22')]+'1'+s[s.index('22')+2:]
print(s.count('1'))
'''
#22
'''
count=0
for i in range(100000000):
    x=i
    a=0
    b=0
    while x>0:
        a+=1
        if x%2!=0:
            b+=1
        x//=2
    if a==16 and b==14:
        count+=1
        print(count)
'''
#23
'''
def f(n,start):
    if n==start:
        return 1
    if n<start:
        return 0
    if n==60:
        return 0
    s=f(n-5,start)
    if n%5==0:
        s+=f(n//5,start)
    return s
print(f(30,5)*f(280,30))
'''
#24
'''
f=open('24.txt','r')
s=f.readline()
count=0
ans=[]
for i in range(len(s)-1):
    if s[i]+s[i+1]=='XY' or s[i]+s[i+1]=='XZ':
        ans.append(count+1)
        count=0
    else:
        count+=1
print(max(ans))
'''
#25
'''
def f(n):
    dels=[1]
    d=2
    while d**2<=n:
        if n%d==0:
            dels.append(d)
            if n//d>d:
                dels.append(n//d)
        d+=1
    return dels
def a(n):
    s=0
    k=f(n)
    if k==1:
        return 0
    for i in k:
        s+=i
    s//=len(k)
    return s
q=310001
count=0
while count!=6:
    if a(q)!=0 and a(q)%6==0 and str(a(q))[-1]!='4':
        print(q,a(q))
        count+=1
    q+=1
'''
#26
'''
import collections
f=open('26.txt','r')
f.readline()
s,n=99987, 9864
d=[]
for i in f:
    d.append(int(i))
d.sort()
i=0
d=collections.deque(d)
while s>0:
    k =d.popleft()
    s-=k
if s<0:
    s+=k
    d.append(k)
print(len(d),sum(d))
'''
#27
'''
f=open('27-A.txt','r')
f.readline()
s=0
mini=10000
for line in f:
    q,w,e=map(int,line.split())
    x=[q,w,e]
    x.sort()
    q=x[1]-x[0]
    if (x[0]+s)%123!=0 and (x[0]+s)%2==0:
        s+=x[0]
    elif (x[1]+s)%123!=0 and (x[1]+s)%2==0:
        s+=x[1]
    elif (x[2]+s)%123!=0 and (x[2]+s)%2==0:
        s+=x[2]
    if q<mini and q%2==0 and  q%123!=0:
        mini=q
if s%123==0:
    s+=mini
print(s)
       
'''
#14
'''
x='1'*91
while '1111' in x or '88888' in x:
    if '1111' in x:
        x=x[:x.index('1111')]+'888'+x[x.index('1111')+4:]
    if '88888' in x:
        x=x[:x.index('88888')]+'888'+x[x.index('88888')+5:]
print(len(x))
'''
#16
'''
x=9*9**23+3**129-18
s=''
while x>0:
    s+=str(x%3)
    x//=3
print(s.count('1')+s.count('0'))
'''
'''
count=0
for q in range(100000):
    i=1
    k=q
    while i**3<k:
        i+=1
    if (i**3-k<=k-(i-1)**3):
        n=i
    else:
        n=i-1
    if n==3:
        count+=1
    n=0
print(count)
'''
#22
def f(n,start):
    if n>start:
        return 0
    if n==start:
        return 1
    s=f(n+5,start)
    s+=f(n+2,start)
    s+=f(n**2,start)
    return s
print(f(5,26)*f(3,5))
















































