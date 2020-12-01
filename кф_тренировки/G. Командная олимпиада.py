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
	count=len(abilities)
	diff=0
	for q in range(1,len(abilities)+1):
		for k in range(1,4):

			if str(k) ==abilities[q-diff]:
				print(q,' q ' ,q-diff,'q - diff',len(abilities),' len ',comands, 'comands')
				abilities.remove(str(k))
				count2=len(abilities)
				count-=count2
				diff=count
				comands.append(q+count)
				count+=count2






print(len(comands)//3)
print(abilities,'abilities after')
print("comands",comands)
while comands:
	print(comands[0],' ',comands[1],' ',comands[2])
	comands.remove(comands[0])
	comands.remove(comands[0])
	comands.remove(comands[0])