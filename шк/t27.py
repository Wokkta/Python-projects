#14
'''
f=open('E:/Downloads/28131_B.txt','r')
maxi = 0
i=0
j=0
i1,j1=0,0
n=[]
ans=[]
i=int(f.readline())
for line in f:
    n.append(int(line))
for i in range(len(n)-1):
    for j in range(i+1,len(n)):
        if n[i]>n[j] and (n[i]+n[j])%120==0:
            if (n[i]+n[j])>=maxi:
                maxi = (n[i]+n[j])
                i1,j1=n[i],n[j]
                ans.append(i1)
                ans.append(j1)
print(i1,j1)
for i in range(0,len(ans)-1,2):
    print(ans[i],ans[i+1],ans[i]+ans[i+1])
'''
#18

f=open('C:/Users/Wokkta/Downloads/27-A.txt','r')
f.readline()
n1,n2,n3=0,0,0
for line in f:
    n=list(map(int,line.split()))
    print(n)
    '''
    if min(n)%2==0:
        n1+=n.pop(n.index(min(n)))
    elif  n[1]%2==0 and n[1]<n[:
        n1+=n.pop(n.index(n[1]))
    else:
        n1+=n.pop(n.index(n[-1]))
    print(n)
    if min(n)%2==1:
        n2+=n.pop(n.index(min(n)))
    else:
        n2+=n.pop(n.index(max(n)))
    n3+=n[0]
    print(n)
print(n3)

'''