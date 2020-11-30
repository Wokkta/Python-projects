def F(n):
	if n==0:
		return 1
	return 2*F(n-1) + (3*F(n-1)**2+3)**0.5
print(F(800))