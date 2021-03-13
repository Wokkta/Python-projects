import time
start_time=time.time()
def f(n):
    if n<=5:
        return n+15
    elif n%2==0:
        return f(n//2)+n**3-1
    else:
        return f(n-1)+2*n*n+1
count=0
for i in range(1,1001):
    if str(f(i)).count('8')>=2:
        count+=1
print(count)
print(time.time-start_time)
