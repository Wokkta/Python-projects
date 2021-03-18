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