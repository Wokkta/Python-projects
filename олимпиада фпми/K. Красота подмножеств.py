'''https://contest.yandex.ru/contest/22235/download/K/'''
n,q=map(int,input().split())
asks=list(map(int,input().split()))
ans=[]
for i in asks:
	for q in range(1,i+1):
		if i%q==0:
			counter=q
	ans.append(counter)
print(ans)
#not right vers  of ask