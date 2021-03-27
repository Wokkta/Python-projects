#16
'''
def f(n):
    if n==1:
        return 1
    if n%2==0:
        return n+f(n-1)
    if n>1 and n%2!=0:
        return 2*f(n-1)+f(n-2)
print(f(20))
'''
#17
'''
counter=0
for i in range(1007,200011):
    if i%10==0 and i%4==0 and i%7==0 and i%11==0 and i%3!=0:
        counter+=1
        mx=i
print(counter,mx)
'''
#23
'''
def f(n,start):
    if n>start:
        return 0
    if n==start:
        return 1
    s=f(n+1,start)
    s+=f(n*3,start)
    s+=f(n*3+1,start)
    s+=f(n*3+2,start)
    return s
print(f(9,33)*f(1,9))
'''
#27
'''
f=open('C:\\Users\\Wokkta\\Desktop\\GitHub\\Python-projects\\шк\\27v02_B.txt')
f.readline()
summ=0
mini=100000
for line in f:
    x, y = map(int, line.split())
    summ += max(map(int, line.split()))
    if abs(x-y)<mini and abs(x-y)%35!=0:
        mini=abs(x-y)
if summ%35==0:
    summ-=mini
print(summ)
'''
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
    if dels==[]:
        return 0
    else:
        return max(dels)-min(dels)
count=0
a=850001
while count!=6:
    if ds(a)!=0 and ds(a)%3==0:
        print(a,ds(a))
        count+=1
    a+=1
'''
#26
'''
f=open('input26_02.txt','r')
q=f.readline
s=99992
values=[]
for line in f:
    values.append(line.strip())
def f(values,s):
    alls=[0]
    while sum(alls)<s:
        alls.append(int(values.pop(values.index(min(values)))))
    if sum(alls)>s:
        alls.pop(-1)
    print(len(alls)-1,max(alls))
    print(s-sum(alls))
    values.remove(values[0])
    values.sort()
    c=0
    a=80
    while c==0:
        if '{}'.format(a) in values:
            c=1
            print(a)
        a-=1

f(values,s)
'''
#2
'''
for x in range(2):
    for y in range(2):
        for w in range(2):
            for z in range(2):
                if ((not x) or y) and z and (not w):
                    print(x,y,w,z)
'''
#24
'''
f=open('24 варианты 1-5.txt','r')
counter=1
sims=['X','Y','Z']
string=''
for line in f:
	string=string+line.strip()
counter1=1
for i in range(1,len(string)):
    if  sims.index(string[i-1])<=sims.index(string[i]) and string[i]!='Z':
        counter1+=1
        if counter1>counter:
            counter=counter1
    else:
        counter1=1

print(counter)
'''
#22
'''
for  i in range(1,1000):
    y=i
    q=2
    l=0
    while i >=5:
        l=l+1
        i=i//q
    m=i
    if m<l:
        m=l
        l=i
    print(l,m,y)
'''
