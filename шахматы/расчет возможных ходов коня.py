'''Востановление траектории шахматного коня'''
'''https://youtu.be/S-hjsamsK8U?t=2275'''
letters = 'abcdefgh'
numbers = '12345678'
graph = {l + n: set() for l in letters for n in numbers}


def add_edge(v1, v2):
    graph[v1].add(v2)
    graph[v2].add(v1)


side = 8
moves = [1, -1, 2, -2]
for i in range(side):
    for j in range(side):
        v1 = letters[i]+numbers[j]
        v2 = ''
        for q in moves:
            for w in moves:
                if 0 <= i+q < side and 0 <= j+w < side and w != q and w != -q:
                    v2 = letters[i+q]+numbers[j+w]
                    add_edge(v1, v2)
for i in graph:
    print(i, ' ', graph[i])

k = "g7"
print(k, ' ', graph[k])
