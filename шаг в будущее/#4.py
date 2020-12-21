from collections import deque
n,m =map(int,input().split())
data=[]
points=[]
mainlandS=0
islandS=0
for i in range(n):
    value=list(map(int,input().split()))
    data.append(value)
for i in data:
    print(i)
'''for i in range(n):
    for j in range(m):
        if 0<i<n-1 and 0<j<m-1:
        data['{},{}'.format(i,j)].add(data[i][j])
        data['{},{}'.format(i,j)].add('{},{}'.format(i+1,j))
        data['{},{}'.format(i, j)].add('{},{}'.format(i + 1, j+1))
        data['{},{}'.format(i, j)].add('{},{}'.format(i + 1, j-1))
        data['{},{}'.format(i, j)].add('{},{}'.format(i - 1, j))
        data['{},{}'.format(i, j)].add('{},{}'.format(i - 1, j + 1))
        data['{},{}'.format(i, j)].add('{},{}'.format(i - 1, j - 1))
        data['{},{}'.format(i, j)].add('{},{}'.format(i , j+1))
        data['{},{}'.format(i, j)].add('{},{}'.format(i, j - 1))
        elif 0<i<n-1 and j==m-1:
        data['{},{}'.format(i, j)].add(data[i][j])
        data['{},{}'.format(i, j)].add('{},{}'.format(i + 1, j))
        data['{},{}'.format(i, j)].add('{},{}'.format(i + 1, j - 1))
        data['{},{}'.format(i, j)].add('{},{}'.format(i - 1, j))
        data['{},{}'.format(i, j)].add('{},{}'.format(i - 1, j - 1))
        data['{},{}'.format(i, j)].add('{},{}'.format(i, j - 1))
        elif 0<j<m-1 and i==n-1:
        data['{},{}'.format(i, j)].add(data[i][j])
        data['{},{}'.format(i, j)].add('{},{}'.format(i - 1, j))
        data['{},{}'.format(i, j)].add('{},{}'.format(i - 1, j + 1))
        data['{},{}'.format(i, j)].add('{},{}'.format(i - 1, j - 1))
        data['{},{}'.format(i, j)].add('{},{}'.format(i, j + 1))
        data['{},{}'.format(i, j)].add('{},{}'.format(i, j - 1))
        elif 0<i<n-1 and j==0:
        data['{},{}'.format(i, j)].add(data[i][j])
        data['{},{}'.format(i, j)].add('{},{}'.format(i + 1, j))
        data['{},{}'.format(i, j)].add('{},{}'.format(i + 1, j + 1))
        data['{},{}'.format(i, j)].add('{},{}'.format(i - 1, j))
        data['{},{}'.format(i, j)].add('{},{}'.format(i - 1, j + 1))
        data['{},{}'.format(i, j)].add('{},{}'.format(i, j + 1))
        elif 0<j<m-1 and i==0:
        data['{},{}'.format(i, j)].add(data[i][j])
        data['{},{}'.format(i, j)].add('{},{}'.format(i + 1, j))
        data['{},{}'.format(i, j)].add('{},{}'.format(i + 1, j + 1))
        data['{},{}'.format(i, j)].add('{},{}'.format(i + 1, j - 1))
        data['{},{}'.format(i, j)].add('{},{}'.format(i, j + 1))
        data['{},{}'.format(i, j)].add('{},{}'.format(i, j - 1))
for i in data:
    print(i,data[i])
#use dfs or bfs
'''
'''test input
5 4
3 2 0 0
2 4 5 0
0 0 0 0
0 1 3 0
0 0 0 0
'''