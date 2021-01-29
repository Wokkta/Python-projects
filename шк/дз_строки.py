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