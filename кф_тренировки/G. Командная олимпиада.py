# https://codeforces.com/group/XWOeQO4RLM/contest/206799/problem/G
studens=int(input())
abilities=list(map(int,input().split()))
comands=[]
abilities=str(abilities)
abilities=abilities[1:len(abilities)-1]
abilities=list(abilities)
count = 1
while ',' in abilities:
	abilities.remove(',')
	abilities.remove(abilities[count])
	count+=1
print(abilities, 'abilities')
for i in range(studens//3):
	count=0
	for k in range(1,4):
		print(str(k),' str ',abilities,' abilities')
		if abilities:
			if str(k) in abilities: 
				comands.append(abilities.index(str(k))+count)
				abilities=abilities.remove(str(k))
				count+=1
print(len(comands)//3)
print(abilities,'abilities after')
print("comands",comands)
while comands:
	print(comands[0],' ',comands[1],' ',comands[2])
	comands.remove(comands[0])
	comands.remove(comands[0])
	comands.remove(comands[0])