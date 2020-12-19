distanse,parts=map(int,input().split())
parts_lenfs=[]
for i in range(parts):
    lenth=int(input())
    parts_lenfs.append(lenth-1)
count=0
for i in parts_lenfs:
    count+=i//distanse
print(count)