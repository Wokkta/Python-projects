#57
'''summ=[]
def f(n):
	summ.append(n)
	if n<7:
		summ.append(n)
		f(n+2)
		f(n*2)
		f(n*3)
	return 0

f(1)
summe=0
for i in  summ:
	summe+=i
print(summe)
'''
# P-01
'''
def f(n):
	if n ==1:
		return 1
	elif n%2==0:
		return n+2+f(n-1)
	else:
		return 2*f(n-2)
print(f(24))
'''
# P-03
'''
summ=[]
def f(n):
	summ.append(2*n)
	if n>1:
		summ.append(n-5)
		f(n-1)
		f(n-2)
	return 0
test_values=[i for i in range(1,51)]
summe1=0
for i in summ:
	summe1+=i
for i in test_values:
	summ=[]
	f(i)
	summe2=0
	for k in summ:
		summe2+=k
	if summe2>500000:
		print (i,' ',summe2)
		break
'''
#P-02
'''
string =[]
def f(n,string=string):
	string.append('*')
	if n>1:
		string.append('*')
		f(n-1,string=string)
		f(n-2,string=string)
		f(n-3,string=string)
	return string
f(22)
print(len(string))

'''
# 16
'''
def f(n):
	if n==1:
		return 1
	elif n%2==0:
		return n+f(n-1)
	else:
		return 2*f(n-2)
print(f(26))
'''
#18 
'''
def f(n):
	if n==1 :
		return 1
	return 2*f(n-1)+g(n-1)-2
def g(n):
	if n==1:
		return 1
	return f(n-1)+2*g(n-1)
print(f(14)+g(14))
'''
#30
'''
summ=[]
def f(n):
	summ.append(n*n)
	if n>1:
		summ.append(2*n+1)
		f(n-2)
		f(n//3)
	return 0
test_values=[i for i in range(1,51)]
summe1=0
for i in summ:
	summe1+=i
for i in test_values:
	summ=[]
	f(i)
	summe2=0
	for k in summ:
		summe2+=k
	if summe2>500000:
		print (i,' ',summe2)
		break
''