'''n=int(input())
print(n//2)'''
n,q=list(map(int,input().split()))
people=[]
for i in range(n-1):
	people.append(input().format(' ',''))
asks=input().format(' ','')
ans=[1]*len(asks)
for a in range(len(asks)):
	
	for i in range(len(people)):
		counter=a
		for p in range(a):
			if people[i][a]!=counter:
				ans[a]+=1
print(ans)