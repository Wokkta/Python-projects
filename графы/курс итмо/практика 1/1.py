'''https://codeforces.com/edu/course/2/lesson/8/1/practice/contest/290939/problem/A'''
t=int(input())
mass=[]
for i in range(t):
	free_lan=input()
	n,m=map(int,input().split())
	graph=[]
	for q in range(m):
		path=list(map(int,input().split()))
		graph.append(path)
print(mass,' end ')
print(graph)