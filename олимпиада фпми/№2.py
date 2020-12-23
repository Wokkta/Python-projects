'''https://contest.yandex.ru/contest/22235/download/B/'''
n,k=map(int,input().split())
n_massive=[]
for i in range(1,n+1):
	n_massive.append(i%k)
maximum=-1
print(n_massive,' kk')
for i in range(k):
	counter=n_massive.count(i)
	if counter>maximum:
		maximum=counter
print(maximum)
'''working wrong'''