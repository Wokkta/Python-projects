from math import factorial
n=int(input())
count=n
k=int(input())
ans=[]
if n< factorial(k) :
    print(-1)
else:
    for i in range(1,k+1):
        ans.append(i)
        n-=i
    for i in range(n):
        ans.append(1)
    if ans.count(1)==len(ans):
        print(1)
        print(count)
    else:
        print(len(ans))
        print(*ans)