n=int(input())
from collections import Counter
surely=[]
check=0
count=[]
for i in range(n):
    surely.append((input().split(" ")))
    count.append(Counter(surely[i]))
for i in range(len(surely)):
    if count[i]['1']>=2:

        check+=1
print(check)
