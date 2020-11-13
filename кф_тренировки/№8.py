x=0
n=int(input())
iteration=[]
for i in range(n):
    iteration.append((input()))
for i  in iteration:
    if i=='--X' or i=='X--':
        x-=1
    if i=='++X' or i=='X++':
        x+=1

print(x)