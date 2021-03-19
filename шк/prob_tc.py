#8
'''
counter=0
def four(n):
	string=''
	while n>0:
		string=str(n%4)+string
		n//=4
	return string
def low(n):
	for i in range(1,len(n)):
		if int(n[i-1])<int(n[i]):
			return False
	return True
for x in range(100,1000):
	if low(four(x)):
		counter+=1
print(counter)
'''
#22
'''
for x in range(1,100000):
	i=x
	q=15
	l=0
	while x>=q:
		l+=1
		x-=q
	m=x
	if m<l:
		m=l
		l=x
	if l==3 and m==7:
		print(i)
'''
#23
'''
def f(n,start):
	if n>start:
		return 0
	elif n==start:
		return 1
	s=f(n+1,start)
	s+=f(n*2,start)
	return s
print(f(10,30)*f(1,10))
'''
#16
'''
def f(n):
	if n==1:
		return 1
	elif n%2==0:
		return n+2*f(n-1)
	elif n>1 and n%2!=0:
		return 1+3*f(n-2)
print(f(17))
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
x=850000
counter=0
while counter!=6:
	if ds(x)!=0 and ds(x)%7==0:
		counter+=1
		print(x,ds(x))
	x+=1
'''
#26
# не дооптимизировал, тк времени не хватило, понимаю, что надо 
# сделать, чтобы сумма была максимально близкая
'''
f=open('input26_01.txt','r')
flag=0
values=[]
S,N=0,0
for line in f:
	if flag==0:
		S,N=map(int,line.split())
		flag=1
	else:
		values.append(line.strip())
def bag(values,maxweight):
	alls=[0]
	#maxweight=maxweight.sort()
	while sum(alls)<maxweight:
		alls.append(int(values.pop(values.index(min(values)))))
	if sum(alls)> maxweight:
		alls.pop(-1)
	#alls_copy=alls
	#alls_copy.remove(max(alls_copy))
	#if maxweight- sum(alls)>=max(alls)-max(alls_copy):

	print(len(alls)-1,max(alls))
bag(values,S)
'''
#27

''' из файла вырезаю первую строку'''
'''
f = open('27v01_A.txt', 'r')
mini = 1000000
summ = 0
for line in f:
    x, y = map(int, line.split())
    summ += max(map(int, line.split()))
    if 0 < x-y < mini and x-y != 0 and (x-y) % 31 != 0:
        mini = ((x-y)**2)**0.5
    elif 0 < y-x < mini and x-y != 0 and (x-y) % 31 != 0:
        mini = ((x-y)**2)**0.5
summ=int(summ)
if summ % 31 == 0:
    print(summ-mini)
else:
    print(summ)
'''
#24
'''
f=open('24 варианты 1-5.txt','r')
counter=0
sims=['X','Y','Z']
string=''
for line in f:
	string=string+line.strip()
counter1=0
for i in range(1,len(string)):
	if sims.index(string[i-1])<=sims.index(string[i]):
		counter1+=1
	else:
		if counter1>counter:
			counter=counter1
			counter1=0
print(counter)
'''
#17
'''
counter=0
simvol=0
def ds(n):
	dels=[]
	d=2
	while d**2<=n:
		if n%d==0:
			dels.append(d)
			if n//d>d:
				dels.append(n//d)
		d+=1
	if 6 in dels :
		sim=[4,5,9,13]
		for i in sim :
			if i in dels:
				return False
		return True
	else:
		return False
for x in range(1007,8011):
	if ds(x):
		counter+=1
		simvol=x
print(counter,simvol)
'''
#18 друг как-т через excel решает, я не додумался как