#27890
'''
f= open('27-B_1.txt','r')
n=f.readline()
mini=10000
s=0
for line in f:
    x,y=map(int,line.split())
    x,y=int(x),int(y)
    s+=max(x,y)
    if mini> max(x,y)-min(x,y) and (max(x,y)-min(x,y))%5!=0:
        mini=max(x,y)-min(x,y)
if s%5!=0:
    print(s)
else:
    print(s-mini)
'''
#27985
'''
f= open('27985_B.txt','r')
n=f.readline()
n1,n2=0,0
flag=0
for line in f:
    if flag==1:
        n2=int(line)
    if int(line)%14==0:
        n1=int(line)
        flag=1
    elif int(line)%2==0:
        n1=int(line)
    elif int(line)%7==0:
        n2=int(line)
    if n1!=0 and n2!=0:
        flag=0
        break
print(n1*n2)
'''
#27988
'''
f=open('27988_B.txt','r')
n=f.readline()
n1,n2=0,0
flag=0
for line in f:
    if flag==1:
        n2=int(line)
    if int(line)%26==0:
        n1=int(line)
        flag=1
    elif int(line)%2==0:
        n1=int(line)
    elif int(line)%13==0:
        n2=int(line)
    if n1!=0 and n2!=0:
        flag=0
        break
print(n1*n2)
'''
#27989
'''
f=open('27989_B.txt','r')
n=f.readline()
nar=[]
count=0
count26,count2,count13=0,0,0
for line in f:
    count+=1
    if int(line)%26==0:
        count26+=1
    elif int(line)%13==0:
        count13+=1
    elif int(line)%2==0:
        count2+=1
ans=count26*(count-count26)+count2*count13

print(ans)
'''
#28129
from time import time
timer=time()
f=open('28129_B.txt','r')
n=f.readline()
nar=[]
for i in f:
    nar.append(int(i))
nar.sort()
nar.reverse()
ans1,ans2=0,0
maxi=0
for i in range(len(nar)-1):
    for j in range(1,len(nar)):
        if (nar[i]*nar[j])%7==0 and nar[i]%160!=nar[j]%160:
            if maxi==0:
                ans1=nar[i]
                ans2=nar[j]
                maxi=nar[i]+nar[j]
            elif maxi<nar[i]+nar[j]:
                maxi=nar[i]+nar[j]
                ans1=nar[i]
                ans2=nar[j]
print(ans1,ans2)
print('%s'%(time()-timer))
