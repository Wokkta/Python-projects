# https://codeforces.com/group/XWOeQO4RLM/contest/206799/problem/H
n,m=list(map(int,input().split()))
votes_all=[]
vinners_by_sities=[]
for i in range(m):
	vote_city=list(map(int,input().split()))
	votes_all.append(vote_city)
def vote(array,vinner,counter=0):
	maximum=-1
	for i in range(len(array)):
		if array[i]>maximum:
			maximum=array[i]
			counter=i+1
	vinner.append(counter)
for k in range(m):
	vote(votes_all[k],vinners_by_sities)
count=[]
maximum=vinners_by_sities.count(vinners_by_sities[0])
index=vinners_by_sities[0]

print(maximum)
if maximum==len(vinners_by_sities):
	print(index)
else:
 	for i in range(1,len(vinners_by_sities)):
 		print(maximum)
		if vinners_by_sities.count(vinners_by_sities[i]) > maximum:
			maximum=vinners_by_sities.count(vinners_by_sities[i])
			index=vinners_by_sities[i]
print(index)