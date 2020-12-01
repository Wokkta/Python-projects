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





print(q,' q ' ,q-diff,'q - diff',len(abilities),' len ',comands, 'comands')
print(len(comands)//3)
print(abilities,'abilities after')
print("comands",comands)
while comands:
	print(comands[0],' ',comands[1],' ',comands[2])
	comands.remove(comands[0])
	comands.remove(comands[0])
	comands.remove(comands[0])