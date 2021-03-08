#### 17
#64
'''
step = 1
count = 0
for i in range(4563, 7912, step):
    if i % 7 == 0:
        step == 7
    if i % 10+i//1000 > 10:
    	count+=1
    	maxi=i
print(maxi,count)
'''
#66
'''
count=0
step=1
flag=0
for i in range(333666,666999+1,step):
	if flag!=1 and i%17==0:
		step=17
		flag=1
	if str(i).count('2')==2 and step==17:
		count+=1
		maxi=i
print(maxi,count)
'''
#67
'''
count=0
for i in range(100001,900010):
	if i&7+i%10==10 and i%11==0 and i%5!=0:
		count+=1
		maxi=i
print(maxi,count)'''
#68
'''
count=0
mini=10**5
for i in range(2079,43168):
	a =str(i)
	if i%7==0 and a.count('0')>0 and a.count('2')>0 and a.count('5')>0:
		count+=1
		if i<mini:
			mini=i
print(count,mini)'''
#69 
'''
count=0
for i in range(1388,63253):
	if i%7!=0 and (str(i).count('7')>0 or str(i).count("4")>0):
		count+=1
		maxi=i
print(count,maxi)
'''
#71
'''
count=0
mini=10**9
for i in range(1031,125889):
	if i%10==5 and i==((i**0.5)//1)**2:
		count+=1
		if i%100==36 and i<mini:
			mini=i
print(count,mini)
'''
#70
'''
count=0
for i in range(2894,174883):
	if i%10==8:
		cost=list(str(i))
		costel=0
		for q in cost:
			costel+=int(q)
		if costel>22:
			count+=1
			if count==13:
				mas=i
print(count,mas)
'''
#72
'''
count=0
maxi=0
for i in range(2848,109500):
	qw=str(i)
	if qw.count('9')>0:
		cost=list(str(i))
		costel=0
		for q in cost:
			if int(q)>5:
				costel+=int(q)
		if costel%3==0:
			count+=1
			if qw[0]==8 and i>maxi:
				maxi=i
print(count,maxi)
'''
#27
'''
mini=10000
count=0
for i in range(3712,8433):
	if i%13==0 or i%14==0 or i%15==0:
		if (i%10)%2==(i%10)%4:
			if i<mini:
				mini=i
			count+=1
print(count,mini)
'''
#30
'''
mini=10000
summ=0
for i in range(1529,9483):
	if bin(i)[-2:]=='01':
		if i%5==3:
			if i<mini:
				mini=i
			summ+=i
print(mini,summ)
'''
#33
'''
mini=1111111111111111
maxi=0
for i in range(1000,10000):
	if i%5!=0 and i%7!=0 and i%11!=0:
		if i<3**9 and i>=3**8:
			if i>maxi:
				maxi=i
			if i<mini:
				mini=i
print(mini,maxi)
'''
#38
'''
count=0
maxi=0
for i in range(2461,9720):
	if 3<(i%100)//10<7:
		if (i%1000)//100!=1 and (i%1000)//100!=9:
			count+=1
			maxi=i
print(count,maxi)
'''
#40
'''
count=0
mini=1010101001
for i in range(1871,9198):
	if i%9==2 or i%9==4:
		cc=1
		q=i
		while q>0 :
			q//=16
			cc+=1
		if len(str(i))!=cc:
			if i<mini:
				mini=i
			count+=1
print(count,mini)
'''
#42
'''
count=0
mini=100000
for i in range(2495,7084):
	if i%5!=0 and i%9!=0:
		if bin(i)[-5:]=='11010' or bin(i)[-5:]=='11111':
			count+=1
			if i<mini:
				mini=i
print(count,mini)
'''
#43
'''
count=0
mini=1111111111
for i in range(3721,7753):
	summ=0
	q=i
	while q>0:
		summ+=q%10
		q//10
	if summ%3==0:
		if bin(i)[-3]!='000':
			count+=1
			if i<mini:
				mini=i
print(count,mini)
'''