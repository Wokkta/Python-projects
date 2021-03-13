count=0
maxi=0
a=1016
while a%3!=0:
	a+=1
for i in range(a,7938,3):
	if i%7!=0 and i%17!=0 and i%19!=0 and i%27!=0:
		count+=1
		maxi=i
print(count,maxi)