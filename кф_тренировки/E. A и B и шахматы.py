'''https://codeforces.com/group/XWOeQO4RLM/contest/206799/problem/E'''
white_figures=('Q',9,'R',5,'B',3,'N',3,'P',1,'K',0)
black_figures=('q',9, 'r',5, 'b',3, 'n',3, 'p',1, 'k',0)
white_massa=0
black_massa=0
board=[]
string_board=''
for i in range(8):
	board.append(input())
for i in range(8):
	string_board+=board[i]
for i in range(len(string_board)):
	if string_board[i] in white_figures:
		for q in range(len(white_figures)):
			if white_figures[q]==string_board[i]:
				white_massa+=white_figures[q+1]
	elif string_board[i] in black_figures:
		for q in range(len(black_figures)):
			if black_figures[q]==string_board[i]:
				black_massa+=black_figures[q+1]
if white_massa>black_massa:
	print('White')
elif white_massa<black_massa:
	print('Black')
elif white_massa==black_massa:
	print('Draw')
else: 
	print(white_massa)
	print(black_massa)