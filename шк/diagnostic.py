#24

with open('text.txt') as text:
	lines=text.readlines()
counter=0
alf='ABCDEFGHIJKLMNOPQRSTUVWXYZ'
counter_array=[0]*26
marker= None # what you need to find
for i in range(len(lines)):
	for l in range(len(lines[i])):
		if lines[i][l]=='E':
			counter_array[alf.index(lines[i][l+1])]+=1
maximum=-1
for i in range(26):
	print(counter_array[i],' {}'.format(alf[i]))
	if counter_array[i]>maximum:
		maximum=i
print(alf[maximum])

#16
'''def f(n):
	if n==0:
		return 0
	elif n>0 and n%3==0:
		return n+f(n-3)
	else:
		return n+f(n-(n%3))
print(f(26))'''
#17
'''dels=[11,13,17,19]
flag =True
count=0
for i in range(22000,33000):
	q=0
	for p in dels:
		if i%p==0:
			q+=1
	if q==2:
		if flag:
			minimum=i
			flag = not flag
		count+=1
print(count,' count ',minimum,' min ')'''
#22
'''
for i in range(1000):
	a = 1
	x=i
	while x > 0:
		a *= x % 11
		x = x // 11
	if a==140:
		print(i)
		break'''
#25
'''for i in range(2000000,3000000):
	for q in range(1,116):
		if i'''