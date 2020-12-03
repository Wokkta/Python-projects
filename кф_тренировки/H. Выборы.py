# https://codeforces.com/group/XWOeQO4RLM/contest/206799/problem/H

def vote(array,vinner,counter=0):
	maximum=-1
	for i in range(len(array)):
		if array[i]>maximum:
			maximum=array[i]
			counter=i+1
	vinner.append(counter)


n,m=list(map(int,input().split()))

votes_all=[]

vinners_by_sities=[]

for i in range(m):
	vote_city=list(map(int,input().split()))
	votes_all.append(vote_city)

for k in range(m):
	vote(votes_all[k],vinners_by_sities)

count=[]

maximum=vinners_by_sities.count(vinners_by_sities[0])



index=vinners_by_sities[0]


if maximum==len(vinners_by_sities):
	pass

else:
 	for i in range(1,len(vinners_by_sities)):

 		if vinners_by_sities.count(vinners_by_sities[i]) >maximum or vinners_by_sities.count(vinners_by_sities[i])==maximum and vinners_by_sities[i]<index:

 			maximum=vinners_by_sities.count(vinners_by_sities[i])

 			index=vinners_by_sities[i]

print(index)