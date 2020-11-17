'''https://codeforces.com/group/XWOeQO4RLM/contest/206799/problem/C'''
s,n=list(map(int,input().split()))
count=s
dragons={}
def test(s,n):
	for i in range(n):
		power,bonus=list(map(int,input().split()))
		dragons["power {}".format(i)]=power
		dragons["bonus {}".format(i)]=bonus
	while dragons!={}:
		for i in range(n):
			try: #without try and except
				if s>int(dragons["power {}".format(i)]):
					del dragons["power {}".format(i)]
					s+=dragons["bonus {}".format(i)]
					del dragons["bonus {}".format(i)]
			except KeyError: 'power {}'.format(i):
				return "NO"
		if s==count:
			return "NO"
	return "YES"
print(test(s,n))