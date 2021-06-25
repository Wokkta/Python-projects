#2
'''
for x in range(2):
    for y in range(2):
        for w in range(2):
            for z in range(2):
                if ((x!=y) or (x!=z) ) and w and (not y or z):
                    print(x,y,w,z)
'''
#23
'''
def f (n,start):
    if n<start:
        return 0
    if n==start:
        return 1
    s=f(n-2,start)
    if n%2==0:
        s+=f(n//2,start)
    if n%3==0:
        s+=f(n//3,start)
    return s
print(f(6,1)*f(24,6))
'''
#24

f=open('24_varianty_1-5.txt','r')
n=f.readline()
count=0
ans=[]
ans2=[]
s=0
while 'Z' in n:
    s=len(n[:n.index('Z')])
    ans.append(s)
    n=n[n.index('Z')+1:]
    if len(ans)>2:
        ans2.append(ans[-1]+ans[-2]+ans[-3])
    #print(s)
print(max(ans2))

#25
'''
def ds(n):
    dels=[]
    d=2
    while d**2<=n:
        if n%d==0:
            dels.append(d)
            if n//d>d:
                dels.append(n//d)
        d+=1
    dels.sort()
    if len(dels)>1:
        return dels[-1]-dels[0]
    return 0
count=0
i=850000
while count!=6:
    s=ds(i)
    if s!=0 and s%13==0:
        print(i,s)
        count+=1
    i+=1
'''
#26
'''
f=open('input26_05.txt','r')
n,s=map(int,f.readline().split())
nums=[]
for line in f:
    nums.append(line)
nums.sort()
count=0

i=0
while count <=n:
    count+=int(nums[i])
    i+=1
count-=int(nums[i-1])
print(i,nums[i-2])
print(bin(90))
'''
#27
'''
f= open('27v05_B.txt','r')
n=f.readline()
mini=10000000
s=0
for line in f:
    x,y=map(int,line.split())
    x,y=int(x),int(y)
    s+=max(x,y)
    if mini> max(x,y)-min(x,y) and (max(x,y)-min(x,y))%39!=0:
        mini=max(x,y)-min(x,y)
if s%39!=0:
    print(s)
else:
    print(s-mini)
'''
#17
'''
def ds(n):
    dels=[]
    d=2
    while d**2<=n:
        if n%d==0:
            dels.append(d)
            if n//d>d:
                dels.append(n//d)
        d+=1
    return dels
c=0
for i in range(1007,8012,2):
    s=ds(i)
    if 31 not in s and 33 not in s and 7 in s and 15 in s:
        c+=1
        print(i)
print(c)
'''
#6
'''
for i in range(1000):
    s=522
    n=i
    while s-n>0:
        s-=20
        n-=15
    if s==22:
        print(i)
        break
'''
#16
'''
def f(n):
    if n==1:
        return 1
    if n%2==0:
        return 2*f(n-1)
    return 3*f(n-2)-1
print(f(18))
'''
#14
'''
x=7**80-7**65+49**15-49
s=''
while x>0:
    s+=str(x%7)
    x//=7
s=list(s)
s.reverse()
n=''
for i in s:
    n+=str(i)
print(n.count('6'))
'''
#22
'''
for i in range(10000):
    x=i
    p=0
    s=6*(x-x%22)
    q=1
    while p<s:
        s-=2*q
        p+=q
        q+=1
    if s==82 and p==91:
        print(i)
'''
