
'''
def f(start,x):
	if x<start: return 0
	if x==start: return 1
	k=f(start,x-1)
	k+=f(start,x-3)
	return k
 43 print(f(3,12)*f(12,20))
'''
# 63
'''
def f(start,x):
	if x<start: return 0
	if x==start: return 1
	if x==22: return 0
	k=f(start,x-1)
	if x%2==0:
		k+=f(start,x//2)
	return k
print(f(5,8)*f(8,60))
'''
#66
'''
def f(start,x):
	if x<start or x==18: return 0
	if x==start: return 1
	k=f(start,x-1)
	k+=f(start,x-3)
	return k
print(f(3,12)*f(12,21))
'''
#73 
'''
def f(start,x):
	if x<start: return 0
	if x==start: return 1
	k=f(start,x-1)
	k+=f(start,x-2)
	if x%2==0:
		k+=f(start,x//2)
	return k
print(f(2,10)*f(10,12))
'''