#2
'''
for x in range(2):
    for y in range(2):
        for w in range(2):
            for z in range(2):
                if not( not((x==y) or x==z) or w or not(not y or z)):
                    print(x,y,w,z)
'''
#16
'''
def f(n):
    if n==1:
        return 1
    if n==2:
        return 2
    if n>2 and n%2==0:
        return 2+f(n-1)
    if n>2 and n%2==1:
        return 3*n+f(n-2)
print(f(43))
'''
#14
'''
x=4**100-4**65+16**15-64
s=''
while x>0:
    s+=str(x%4)
    x//=4
print(s.count('3'))
'''
#17
'''
c=0
for i in range(2077,8393):
    if i%10==4 or (i%15==0 or i%16==0 or i%21==0 or i%25==0):
        c+=1
        print(i)
print(c)
'''
#22
'''
for i in range(10*5):
    x=i
    p=0
    s=5*(x-x%21)
    a=1
    while p<s:
        s=s-3*a
        p+=a
        a+=1
    if s==42 and p==91:
        print(i)
'''
#23
'''
def f(n,start):
    if n<start:
        return 0
    if n==start:
        return 1
    s=f(n-3,start)
    s+=f(n-4,start)
    if n%3==0:
        s+=f(n//3,start)
    return s
print(f(7,1)*f(30,7))
'''
#24
'''
f=open('24_varianty_6-14.txt','r')
n=f.readline()
count=0
ans=[]
for i in range(len(n)-1):
    for j in range(1,len(n)):
        if i!=j:
            count+=1
        else:
            ans.append(count)
            count=1
print(max(ans))
'''
#6
'''
maxi=0
for i in range(1000):
    s=127
    n=i
    while n-s>0:
        s+=20
        n+=15
    if s== 627:
        maxi=i
print(maxi)
'''
#15
'''
for a in range(1000):
    for x in range(1000):
        for y in range(1000):
            if  (x<a)and (y<a) and (x*y<601):
                maxi=a
print(maxi)
'''
#22
'''
for q in range(1000):
    x=q
    p=0
    s=5*(x-x%21)
    i=1
    while p<s:
        s-=3*i
        p+=i
        i+=1
    if s==42 and p==91:
        maxi=q
print(maxi)
'''
'''
w=1
n=143
#19
q=144
def win(x,y,turn):
    if x+y>=q and turn==3:
        return True
    else:
        if x+y<q and turn==3:
            return False
        if x+y>=q and turn <3:
            return False
    return win(x+1,y,turn+1) or win(x,y+1,turn+1) or win(x*2,y,turn+1) or win(x,y*2,turn+1)

for i in range(1,n):
    if win(w,i,1):
        print(i,'19')
        break


#20
q=101
def win(x,y,turn):
    if x+y>=q and turn==4:
        return True
    else:
        if x+y<q and turn==4:
            return False
        if x+y>=q and turn <4:
            return False
    if turn%2==1:
        return win(x+1,y,turn+1) or win(x,y+1,turn+1) or win(x*2,y,turn+1) or win(x,y*2,turn+1)
    else:
        return win(x+1,y,turn+1) and win(x,y+1,turn+1) and win(x*2,y,turn+1) and win(x,y*2,turn+1)
for i in range(1,n):
    if win(w,i,1):
        print(i,'20')


#21
def win(x,y,turn):
    if x+y>=q and (turn==5 or turn==3):
        return True
    else:
        if x+y<q and turn==5:
            return False
        if x+y>=q and turn <5:
            return False
    if turn%2==0:
        return win(x+1,y,turn+1) or win(x,y+1,turn+1) or win(x*2,y,turn+1) or win(x,y*2,turn+1)
    else:
        return win(x+1,y,turn+1) and win(x,y+1,turn+1) and win(x*2,y,turn+1) and win(x,y*2,turn+1)
for i in range(1,n):
    if win(w,i,1):
        print(i,'21')
        break
'''
#25
'''
def ds(n):
    dels=[1]
    d=2
    while d**2<=n:
        if n%d==0:
            dels.append(d)
            if n//d>d:
                dels.append(n//d)
        d+=1
    return dels
i=450000
c=0
while c!=6:
    if len(ds(max(ds(i))))!=1:
        print(i)
        c+=1
    i+=1
'''
#26
'''
f=open('input26_07(1).txt','r')
f.readline()
s,q=99989, 9997
nums=[]
for line in f:
    nums.append(int(line))
f.close()
summ=0
nums.sort()
i=0
while summ<s:
   summ+=nums[i]
   i+=1
if summ==s:
    print(i,nums[i-1])
else:
    print(i-1,nums[i-2])
'''
#27
f = open('27v07_B.txt', 'r')
f.readline()
mini = 1000000
summ = 0
for line in f:
    x, y = map(int, line.split())
    summ += max(map(int, line.split()))
    if 0 < x-y < mini and x-y != 0 and (x-y) % 43 != 0:
        mini = abs(x-y)
    elif 0 < y-x < mini and x-y != 0 and (x-y) % 43 != 0:
        mini = abs(x-y)
summ=int(summ)
if summ % 43 == 0:
    print(summ-mini)
else:
    print(summ)























    
