'''https://codeforces.com/edu/course/2/lesson/8/1/practice/contest/290939/problem/A'''
t=int(input())
for i in range(t):
	N,M=map(int,input().split())
	graph={i: set() for i in range(N)}
	for i in range(M):
		v1,v2=map(int,input().split())
    	graph[v1].add(v2)
    	graph[v2].add(v1)
	for i in graph:
    	print(i,' ',graph[i])