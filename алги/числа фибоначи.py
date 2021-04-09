# recursion
n=4001
cashe=[0]*n
import time
def fib(n):
	if n<=1:
		return n
	if cashe[n]==0:
		cashe[n]=fib(n-1)+fib(n-2)
	return cashe[n]
'''
for i in range(n):
	timer=time.time()
	print(fib(i),'%s'%(time.time()-timer), i)
'''
# dinamic version
Fib=[0]*(n+1)
def fib_din(n):
	Fib[0]=0
	Fib[1]=1
	for i in range(2,n+1):
		Fib[i]= Fib[i-1]+Fib[i-2]
	return Fib[n]
i=n-1
print(fib_din(i), i)