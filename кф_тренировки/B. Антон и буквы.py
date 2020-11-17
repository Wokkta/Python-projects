'''https://codeforces.com/group/XWOeQO4RLM/contest/206799/problem/B'''
symvols=input()
symvols=symvols.replace('{','')
symvols=symvols.replace('}','')
symvols=symvols.replace(',','')
symvols=list(symvols.split())
count=0
lenth=len(symvols)
for i in range(lenth) :
	value=symvols.pop()
	if value  not in symvols:
		count+=1

print(count)
