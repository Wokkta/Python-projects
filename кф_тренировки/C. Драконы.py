'''https://codeforces.com/group/XWOeQO4RLM/contest/206799/problem/C'''
s,n=list(map(int,input().split()))
counter=s
dragons_power=[]
dragons_bonus=[]
def test(s,n):
	for i in range(n):
		power,bonus=list(map(int,input().split()))
		dragons_power.append(power)
		dragons_bonus.append(bonus)
	while dragons_bonus!=[] and dragons_power!=[]:
		for k in range(n-1):
			for i in range(n-1):
				if s>int(dragons_power[i]):
					dragons_power.remove(dragons_power[i])
					s+=dragons_bonus[i]
					dragons_bonus.remove(dragons_bonus[i])
				
		if s==counter:
			return "NO"
	return "YES"
print(test(s,n))