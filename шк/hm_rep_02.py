#37
'''
for i in range(248015,251576):
	divs=[1,i]
	d=2
	while d**2<=i:
		if i%d==0:
			divs.append(d)
			if i//d>d:
				divs.append(i//d)
		d+=1
	if len(divs)%2==1:
		print(i-248014,i,len(divs),int((i**0.5)//1))
'''
#63
count=0
for i in range(2532000,2532161):
	divs=[1,i]
	d=2
	while d**2<=i:
		if i%d==0:
			divs.append(d)
			if i//d>d:
				divs.append(i//d)
		d+=1
	if len(divs)==2:
		count+=1
		print(i-2532000+1,i)
		if count==5:
			break
