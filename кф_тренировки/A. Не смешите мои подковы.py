'''https://codeforces.com/group/XWOeQO4RLM/contest/206799/problem/A'''
have_already=list(map(int, input().split()))
count=0
lenth=len(have_already)
for i in range(4) :
	value=have_already.pop()
	if value in have_already:
		count+=1

print(count)
