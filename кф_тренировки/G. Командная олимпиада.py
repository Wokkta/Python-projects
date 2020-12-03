# https://codeforces.com/group/XWOeQO4RLM/contest/206799/problem/G
studens=int(input())
abilities=input()
abilities=abilities[::2]
abilities=list(abilities)
for i in range(len(abilities)):
	abilities[i]=int(abilities[i])
comands=[]
diff = 1
while abilities!=[]:
	for i in abilities:
		print(111)
		if len(comands)<4:
			comands.append(i)
			comands.append('index = '+str(abilities.index(i)+diff)+' , ')
			abilities.remove(i)
			diff+=1
			print(222)
		elif i!=comands[-2] and i!=comands[-4]:
			comands.append(i)
			comands.append('index = '+str(abilities.index(i)+diff)+' , ')
			abilities.remove(i)
			diff+=1
			print(333)
print(' comands ')
print(*comands)