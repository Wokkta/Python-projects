#23
def f(n,start):
	if n<start:
		return 0
	if n==start:
		return 1
	s+=f(n,start)
	#change s
	return s
print(f(n,start))