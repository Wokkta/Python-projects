from collections import deque
N,M=map(int,input().split())
graph={i: set() for i in range(N)}
for i in range(M):
    v1,v2=map(int,input().split())
    graph[v1].add(v2)
    graph[v2].add(v1)
for i in graph:
    print(i,' ',graph[i])
distances=[None]*N
parents=[None]*N # все взаимодействия для востановления кратчайшего пути
start_vertex=0
distances[start_vertex]=0
queue=deque([start_vertex])
counter=0
while queue:
    cur_v=queue.popleft()
    for neigh_v in graph[cur_v]:
        counter+=1
        if distances[neigh_v] is  None:
            distances[neigh_v]=distances[cur_v]+1
            parents[neigh_v]=cur_v
            queue.append(neigh_v)
        if distances[neigh_v] is  not None:
            counter+=1
            break
print(distances, ' distances ')
print(counter,' counter ')
end_vertex=9
path=[end_vertex]
parent=parents[end_vertex]
while parent is not None:
    path.append(parent)
    parent=parents(parent)
print()