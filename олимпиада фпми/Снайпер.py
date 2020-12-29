''' https://contest.yandex.ru/contest/22235/download/E/'''
''' not ready at all'''
n,m,kolvo_bombs=map(int,input().split())
bombs=[]
for i in range(kolvo_bombs):
	bomb = list(map(int,input().split()))
	bombs.append(bomb)
for i in range(kolvo_bombs):
	for q in range(2):
		bombs[i][q]-=1
print(bombs)
print('')
pole=[[0 for q in range(n)] for i in range(m) ]
for i in range(kolvo_bombs):
	pole[bombs[i][0]][bombs[i][1]]=1
for i in pole:
	print(i)
count=0
ans=[]
count_of_shots=kolvo_bombs
for i in range(kolvo_bombs):
	y=bombs[i][0]
	x=bombs[i][1]
	if y==0:
		if x==0:
			if pole[y][x]==pole[y+1][x]==1 or pole[y][x]==pole[y][x+1]==1:
				count_of_shots-=1
		elif x<n:
			if pole[y][x]==pole[y+1][x]==1 or pole[y][x]==pole[y][x+1]==1 or pole[y][x]==pole[y][x-1]==1:
				count_of_shots-=1
		elif x==n:
			if pole[y][x]==pole[y+1][x]==1 or pole[y][x]==pole[y][x-1]==1:
				count_of_shots-=1
	if y<m:
		if x==0:
			if pole[y][x]==pole[y+1][x]==1 or pole[y][x]==pole[y][x+1]==1  or  pole[y][x]==pole[y-1][x]==1:
				count_of_shots-=1
		elif x<n:
			if pole[y][x]==pole[y+1][x]==1 or pole[y][x]==pole[y][x+1]==1 or pole[y][x]==pole[y][x-1]==1  or pole[y][x]==pole[y-1][x]==1:
				count_of_shots-=1
		elif x==n:
			if pole[y][x]==pole[y+1][x]==1 or pole[y][x]==pole[y][x-1]==1 or  pole[y][x]==pole[y-1][x]==1:
				count_of_shots-=1
	if y==m:
		if x==0:
			if pole[y][x]==pole[y-1][x]==1 or pole[y][x]==pole[y][x+1]==1:
				count_of_shots-=1
		elif x<n:
			if pole[y][x]==pole[y-1][x]==1 or pole[y][x]==pole[y][x+1]==1 or pole[y][x]==pole[y][x-1]==1:
				count_of_shots-=1
		elif x==n:
			if pole[y][x]==pole[y-1][x]==1 or pole[y][x]==pole[y][x-1]==1:
				count_of_shots-=1
print(count_of_shots)
'''
test input 1
2 2 2
1 2
2 1
test input 2
3 3 4
1 1
1 3
3 3
3 1
'''