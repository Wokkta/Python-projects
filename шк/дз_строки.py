#14
'''
strn=input()
pattern='12'
value='11'
strn=strn.replace(pattern,value)
print(strn)
'''
#15
'''
strn=input()
flag=0
elements="',.~`|]}[{';:.?<>!@#$%^&*()_  "
for i in elements:
	strn=strn.replace(i,'')
if len(strn)%2==1:
	strn=strn[:len(strn)//2]+strn[len(strn)//2+1:]
for i in range(1,len(strn)-1):
	if strn[i]!=strn[-i]:
		print("NO")
		flag=1
		break
if flag==0:
	print("YES")
	'''
#1
'''
strn=input()
if strn.count("о")>strn.count("а"):
	print('o')
else: print('a')
'''
#2
'''
strn=input()
if ',' in strn:
	print('YES')
else: print("NO")
'''
#3
'''
strn=input()
if strn.index('н')< strn.index("к"):
	print('H')
else:
	print('K')
'''
#4
'''
strn=input()
nums=[1,2,3,4,5,6,7,8,9,0]
index=strn.index(' ')
if int(strn[index+1]) in nums:
	print('num')
else: print('nit a num')'''
#5
'''
strn=input()
nums=[1,2,3,4,5,6,7,8,9,0]
summ=0
for i in nums:
	summ+=strn.count(i)
if  summ>strn.count(' '):
	print('nums')
else: print(' tabulation')'''
#6
'''
strn=input()
print(strn.count("или"))
'''
#7
'''
strn=input()
m,n=6,6
if strn[strn.index(m)]+strn[strn.index(m)+1]+strn[strn.index(m)+2] =='666':
	print('yes')
else: print('no')
'''
#8
'''
strn=input()
print(strn[:strn.index('  ')])
'''
#9
'''
strn=input()
streng=[]
for i in range(1,len(strn)-1):
	if strn[-i]!=' ':
		streng.append(strn[-i])
	else:
		break
ans=[]
for i in range(1,len(streng)-1):
	ans.append(streng[-i])
print(ans)
'''
#10
'''
strn=input()
f=strn[:strn.index('  ')]
strn=strn[strn.index('  ')+2:]
s=strn[:strn.index('  ')]
strn=strn[strn.index('  ')+2:]
l=strn
print(f,s,l)'''
#12
'''
strn=input()
count=0
strn=strn.split(' ')

for i in range(6):
	print(strn[i])
	'''
#2
'''
strn=input()
strn=strn.split(',')
print(len(strn[0]),len(strn[1])
'''
#3
'''
strn=input()
count=0
strn=strn.split('+')
for i in strn:
	count+=int(i)
print(count)
'''
#13
'''
strn=input()
strn=strn.split('')
for i in strn:
	print(i)
	'''
#14
'''
maxi=0
strn=input()
strn=strn.split(' ')
for i in strn:
	if len(i)>maxi:
		maxi=len(i)
print(maxi)'''
#16
'''
strn=input()
strn=strn.replace(' ','')
print(strn)
'''