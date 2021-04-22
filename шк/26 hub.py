#21
'''
f=open('26-1k.txt','r')
q=f.readline()
m,n=1000,100
costs=[]
for line in f:
    costs.append(int(line.strip()))
costs.sort()
f.close()
s=0
for i in range(1,n+1):
    s+=costs[-i]*0.2
print(costs[-(n+1)],int(s))
'''
#22
'''
m,n=1000,50
f=open('26-2k.txt','r')
f.readline()
costs=[]
for line in f:
    costs.append(int(line.strip()))
f.close()
costs.sort()
costs=costs[n:-n]
s=sum(costs)//len(costs)
print(costs[-1],s)
'''
#23
'''
f=open('26-3k.txt','r')
m,n,b =600,60,240
f.readline()
points=[]
for line in f:
    points.append(int(line))
points.sort()
winner=points[-n]
prizer=points[-n-b]
print(prizer,winner)
'''
#24
'''
f=open('26-4k.txt','r')
f.readline()
m,n=700, 70
ns=[]
for line in f:
    ns.append(int(line))
ns.sort()
best=ns[-n:]
best1=ns[-2*n:-n]
print(sum(best1)//len(best1),sum(best)//len(best))
'''
#25

f=open('26-5k.txt','r')
f.readline()
m,n,b=100,30,10
costs=[]
for line in f:
    costs.append(int(line))
costs.sort()
print(costs[-b],int(sum(costs[:n])/len(costs[:n])))

#26
'''
f=open('26-J1.txt','r')
f.readline()
n=8321
costs=[]
for line in f:
    costs.append(int(line))
deleted=[]
count=0
for i in costs:
    for j in costs:
        if i!=j and j+i==100 and j not in deleted and i not in deleted:
            count+=1
            deleted.append(i)
            deleted.append(j)
for i in costs:
    if costs.count(i)>1 and i*2==100:
        count+=1
print(count)
'''
