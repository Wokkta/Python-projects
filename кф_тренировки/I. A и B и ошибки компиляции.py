# https://codeforces.com/group/XWOeQO4RLM/contest/206799/problem/I
mistakes_kolvo=int(input())
mistakes=list(map(int,input().split()))
mistakes_mines_one=list(map(int,input().split()))
mistakes_mines_two=list(map(int,input().split()))
debugged=[]
def find_deb(mistakes_kolvo_q,mistakes_q,array,count=-1):
	for i in range(mistakes_kolvo_q):
		if mistakes_q[i] not in array or mistakes_q[i] in array and mistakes_q.count(mistakes_q[i])!=array.count(mistakes_q[i]) and mistakes_q.count(mistakes_q[i])!=count :
			debugged.append(mistakes_q[i])
			count=mistakes_q.count(mistakes_q[i])+1
			
find_deb(mistakes_kolvo,mistakes,mistakes_mines_one)

find_deb(mistakes_kolvo - 1, mistakes_mines_one, mistakes_mines_two)
answers=[]
for i in range(len(debugged)):

	if debugged[i] not in answers:
		answers.append(debugged[i])

print(answers[0])
print(answers[1])
