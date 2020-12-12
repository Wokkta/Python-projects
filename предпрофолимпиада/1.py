n,k=list(map(int,input().split()))
import math
'''fs=((n/math.e)**n) * ((2 * math.pi * n)**0.5)
fs=fs//1
sd=((k/math.e)**k) * ((2 * math.pi * k)**0.5)
sd=sd//1
print(int((fs-sd))%10)'''
n=math.factorial(n)
k=math.factorial(k)
print((n-k)%10)