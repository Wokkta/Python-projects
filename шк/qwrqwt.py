#2
'''
for x in range(2):
    for y in range(2):
        for w in range(2):
            for z in range(2):
                if not( (not(z and (not w))) or (((z<=w)==(x<=y)))):
                    print(x,y,w,z)
'''
#6
'''
for x in range(10000):
    s=x
    n=1
    while s<94:
        s+=8
        n*=2
    if n==32:
        print(x)
'''
#12
'''
x='9992'*33+'9'+'2'*15+'1'*14
while '999' in x or '22' in x:
    if '999' in x:
        x=x[:x.index('999')]+'12'+x[x.index('999')+3:]
    else:
        x=x[:x.index('22')]+'1'+x[x.index('22')+2:]
print(x)
print(x.count('1'))
'''
#14
'''
x=4**625-2**311+2**571-48
s=''
while x:
    s+=str(x%4)
    x//=4
print(s.count('1'))
'''
'''
print(36*48*60)
'''
#16
'''
def f(n):
    if n==1 or n==2:
        return n
    if n>2 and n%2==0:
        return (n+f(n-2))//5
    else:
        return (2*n+f(n-1)+f(n-2))//4
print(f(50))
'''
#17
'''
c=0
flag=0
def delits(i,n):
    for q in n:
        if i%q!=0:
            return False
    return True
for i in range(1206,14993):
    if i%10==3 or i%10==6:
        if  not delits(i,[3,4,5]):
            c+=1
            if flag==0:
                mini=i
                flag=1
print(c,mini)
'''
#20
'''
def f(x,y,turn):
    if x*y>=63 and turn ==4:
        return True
    if x*y<63 and turn ==4:
        return False
    if x*y>63 and turn <4:
        return False
    if turn%2==1:
        return f(x+1,y,turn+1) or f(x*2,y,turn+1) or f(x,y+1,turn+1) or f(x,y*2,turn+1)
    return f(x+1,y,turn+1) and f(x*2,y,turn+1) and f(x,y+1,turn+1) and f(x,y*2,turn+1)

for i in range(1,32):
    if f(i,2,1):
        print(i)
'''
#21
'''
def f(x,y,turn):
    if x*y>=63 and turn ==5:
        return True
    else:
        if x*y<63 and turn ==5:
            return False
        if x*y>63 and turn <5:
            return False
    if turn%2==1:
        return f(x+1,y,turn+1) or f(x*2,y,turn+1) or f(x,y+1,turn+1) or f(x,y*2,turn+1)
    else:
        return f(x+1,y,turn+1) and f(x*2,y,turn+1) and f(x,y+1,turn+1) and f(x,y*2,turn+1)

for i in range(1,32):
    if f(i,2,1):
        print(i)
'''
#22
'''
c=0
for i in range(100000):
    x=i
    a=0
    b=0
    while x>0:
        a+=1
        if x%2!=0:
            b+=1
        x//=2
    if a==16 and b==14:
        c+=1
print(c)
'''
#23
'''
def f(x,start):
    if x<start:
        return 0
    if x==start:
        return 1
    if x==60:
        return 0
    s=f(x-5,start)
    if x%5==0:
        s+=f(x//5,start)
    return s
print(f(30,5)*f(280,30))
'''
#24
'''
f=open('24 (2).txt','r')
s=f.readline()
f.close()
lenth=0
ans=[]
for i in range(len(s)-1):
    j=i+1
    if not(s[i]=='X' and s[j]=='Y' or (s[i]=='X' and s[j]=='Z')):
        lenth+=1
    else:
        lenth+=1
        ans.append(lenth)
        lenth=0

print(max(ans))
'''
#25
'''
def delit(n):
    dels=[]
    d=2
    while d**2<=n:
        if n%d==0:
            dels.append(d)
            if n//d>d:
                dels.append(n//d)
        d+=1
    return dels
def check(ms):
    s=0
    count=0
    for i in ms:
        if delit(i)==[]:
            s+=i
            count+=1
    if s!=0:
        s//=count
    return s
a=310001
c=0
while c!=6:
    if check(delit(a))%6==0 and check(delit(a))%10!=4 and check(delit(a))!=0:
        print(a,check(delit(a)))
        c+=1
    a+=1
'''
#26
'''
f=open('26 (1).txt','r')
s,n=list(map(int,f.readline().split()))
ms=[]
for i in f:
    ms.append(int(i))
ms=sorted(ms)
ss=[]
i=0
while s>0:
    s-=ms[i]
    ss.append(ms[i])
    i+=1
if s<0:
    ss.pop()
print(len(ms)-len(ss))
q=0
for i in range(len(ss),len(ms)):
    q+=ms[i]
print(q)
'''
#27

f=open('27-A (1).txt','r')
f.readline()
s=0
mini=[100000]
for line in f:
    m=list(map(int,line.split()))
    m.sort()
    if m[1]-m[0]<mini[-1] and ( m[1]-m[0])%123!=0:
        mini.append(m[1]-m[0])
    s+=m[0]
def med(n,q):
    for i in range(-1,-len(n),-1):
        if q==1:
            if n[i]%2==1:
                return n[i]
        else:
            if n[i]%2==0:
                return n[i]
if s%123==0:
    if s%2==0:
        s+=med(mini,0)
    else:
        s+=med(mini,1)

print(s)






































