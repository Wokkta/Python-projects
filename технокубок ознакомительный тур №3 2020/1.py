n=int(input())
marks=list(map(int,input().split()))
count=0
gifts=0
for i in range(n):
    if marks[i]>3:
        count+=1
    else:
        count=0
    if count==3:
        gifts+=1
        count=0
print(gifts)