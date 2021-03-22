import time
from math import sqrt
start_time = time.time()

def check(n):
    for i in range(2, int(sqrt(n)) + 1):
        if(n % i == 0):
            return False
    return True
    
for n in range(106000000, 107000001):
    if(n % 2 == 0):
        if(int(sqrt(n // 2))**2 == n//2):
            if(check(int(sqrt(n // 2)))):
                print(n)
print( % (time.time() - start_time))
