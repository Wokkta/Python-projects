def delit(n):
	dels=[]
	d=2
	while d**2<=n:
		if n%d==0:
			dels.append(d)
			
			if n//d>d:
				dels.append(n//d)

		d+=1
	return dels
def delits(n):
	dels=[]
	d=2
	while d**2<=n:
		if len(dels)>2:
			return False
		if n%d==0:
			dels.append(d)
			
			if n//d>d:
				dels.append(n//d)

		d+=1
	return True
for i in range(10**6,10**6):
	for q in delit(i):
		if not delits(q):
			break
	else:
		print(i)