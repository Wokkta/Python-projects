#37 
'''
count=0
squad=0
for i in range(248015,251576,2):
	divs=[1,i]
	d=3
	count+=1
	while d**2<=i:
		if d**2==i:
			squad=d
		if i%d==0:
			divs.append(d)
			if i//d>d:
				divs.append(i//d)
			d+=1
	print(count,i,len(divs),squad)
	'''
#63
'''
rg=[]
count=0
for i in range(2532000,2532161):
	divs=[1,i]
	d=2
	count+=1
	while d**2<=i:
		if i%d==0:
			divs.append(d)
			if i//d>d:
				divs.append(i//d)
			d+=1

	if len(divs)==2:
		rg.append(i,count)
	if len(rg)==10:
		break
for i in range(0,10,2):
	print(rg[i],rg[i+1])
	'''
#70
'''
for i in range(2,10001):
	divs=[1]
	d=2
	while d**2<=i:
		if i%d==0:
			divs.append(d)
			if i//d>d:
				divs.append(i//d)
			d+=1
	summ=0
	for q in divs:
		summ+=q
	if summ==i:
		print(i,len(divs))
'''
#73
'''
count=0
for i in range(2,20001):
	divs=[1]
	d=2
	while d**2<=i:
		if i%d==0:
			divs.append(d)
			if i//d>d:
				divs.append(i//d)
			d+=1
	summ=0
	for q in divs:
		summ+=q
	if summ>i:
		count+=1
print(count)
'''
#74 
'''
count=0
for i in range(2,10001):
	divs=[1]
	d=2
	while d**2<=i:
		if i%d==0:
			divs.append(d)
			if i//d>d:
				divs.append(i//d)
			d+=1
	summ=0
	for q in divs:
		summ+=q
	if summ<i:
		count+=1
print(count)
'''
#75
'''
for i in range(1000,20001):
	divs=[1]
	d=2
	while d**2<=i:
		if i%d==0:
			divs.append(d)
			if i//d>d:
				divs.append(i//d)
			d+=1
	summ=0
	for q in divs:
		summ+=q
	if summ+1==i:
		print(i)
'''
#76
'''for i in range(1000,20001):
	divs=[1]
	d=3
	while d**2<=i:
		if i%d==0:
			divs.append(d)
			if i//d>d:
				divs.append(i//d)
			d+=1
	summ=0
	for q in divs:
		summ+=q
	'''
#81
'''
for i in range(2,263001):
	divs=[1,i]
	d=2
	while d**2<=i:
		if i%d==0:
			divs.append(d)
			if i//d>d:
				divs.append(i//d)
			d+=1
	summ=0
	for q in divs:
		summ+=q
	divs=[1,summ]
	d=2
	while d**2<=summ:
		if summ%d==0:
			divs.append(d)
			if summ//d>d:
				divs.append(summ//d)
	summ=0
	for q in divs:
		summ+=q
	if summ==2*i:
		print(i)
		'''
#84
'''
string=[]
ele=[]
for i in range(87921,88188):
	summ=0
	q=i
	mn=1
	while q>0:
		summ+=q%10
		mn*=q%10
		q//=10
	if summ%14==0 and mn%18==0:
		print(summ, mn)
	'''
#91
'''
summ=0
for i in range(4099,26986):
	divs=[]
	d=2
	while d**2<=i:
		if i%d==0:
			divs.append(d)
			if i//d>d:
				divs.append(i//d)
	if len(divs)==1:
		summ+=divs[0]
print(summ)
'''
#95
'''
summar=0
for i in range(1395,22718):
	q=i
	nums=[]
	summ=0
	while q>0:
		nums.append(q%10)
		q//=10
	num=nums[0]
	for w in range(1,len(nums)):
		if nums[w]<=num:
			summ+=1
		else:
			break
		num=nums[w]
	if summ!=len(nums):
		pass
	else:
		summar+=i
print(summar)
'''
