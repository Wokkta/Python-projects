#14
'''
x= 729**7+3**16-18
s=''
while x>0:
    s=s+str(x%9) 
    x//=9
print(s.count('0'))
'''
#16
'''
def f(n):
    if n==0:
        return 0
    elif n>0 and n%3==0:
        return f(n//3)
    else:
        return n%3+ f(n-n%3)
for i in range(1000):
    if f(i)==11:
        print(i)
        break
'''
#23
'''
def f(n,start):
    if n<start:
        return 0
    if n==start:
        return 1
    if n==30:
        return 0
    s=f(n-1,start)
    if n%2==0:
        s+=f(n//2,start)
    if n%3==0:
        s+=f(n//3,start)
    return s
print(f(12,2)*f(36,12))
'''
#24
'''
f=open('24.txt','r')
count=0
lines=[]
maxi=0
for line in f:
    lines.append(line.strip())
    count+=1
    if maxi==0:
        maxi,a=line.count('G'),count
    else:
        if line.count('G')<maxi:
            maxi,a = line.count('G'),count
f.close()
graph={i: set() for i in range(1,count+1)}
for i in graph:
    for j in lines:
        graph[i]=j
print(graph)
'''
#15
'''
def dels(n,z):
    if n%z==0:
        return True
    return False
for x in range(1,1000):
    for a in range(1,1000):
        if dels(a,45)*(not dels(750,x) or dels(a,x) or not dels(120,x)):
            print(a)
            break
'''
#6
'''
for i in range(1000):
    s=i
    s=10*s+5
    n=1
    while s<2021:
        s=s+2*n
        n=n+1
    if n==11:
        print(i)
        break
'''
#17
'''
def dels(n):
    delss=[]
    d=2
    while d**2<=n:
        if n%d==0:
            delss.append(d)
            if n//d>d:
                delss.append(n//d)
        d+=1
    return delss
n=0
for i in range(10001,50001):
    count=0
    for q in dels(i):
        if dels(q)==[]:
           count+=1
        if count>3:
            break
    if count == 3 :
        print(i)
        n+=1
print('n',n)
'''
#22
'''
for i in range(1,1000):
    x=i
    k=x%9
    a,b=0,0
    while x>0:
        d=x%9
        if d==k:
            a+=1
        b+=d
        x//=9
    if a==3 and b==10:
        print(i)
        break
'''
#25
'''
def dels(n):
    delss=[]
    d=2
    nechet=0
    while d**2<=n:
        if nechet>5:
            return False
        if n%d==0:
            if d%2==1:
                nechet+=1
            delss.append(d)
            if n//d>d:
                if (n//d)%2==1:
                    nechet+=1
                delss.append(n//d)
        d+=1
    if nechet==5:
        return  True
    return False
for i in range(35*10**6,40*10**6+1):
    if dels(i):
        print(i)
'''
#27
'''
f=open('27-B.txt','r')
n=int(f.readline())
nums=[]
for line in f:
    nums.append(int(line))
nums.sort()
nums.reverse()
s=0
for i in range(len(nums)):
    if s==0:
        s=nums[i]
        k=nums[i+1]
    
    if (nums[i]+k+s)%3==0:
        print((nums[i]+k+s))
        break
'''
#26
f=open('26.txt','r')
nums=[]
n=int(f.readline())
for line in f:
    nums.append(int(line))
f.close()
maxi=0
count=0
for i in range(len(nums)-1):
    for j in range(1,len(nums)):
        if (nums[i]+nums[j]) in nums:
            count=1
            if maxi==0:
                maxi=(nums[i]+nums[j])
            elif maxi<(nums[i]+nums[j]):
                maxi=(nums[i]+nums[j])
print(count,maxi)
            
