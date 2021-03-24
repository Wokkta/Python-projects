letters = 'abcdefgh'
numbers = '12345678'
graph = {l + n: set() for l in letters for n in numbers}


def add_edge(v1, v2):
    graph[v1].add(v2)
    graph[v2].add(v1)


for i in range(8):
    for j in range(8):
        v1 = letters[i]+numbers[j]
        v2 = ''
    # действие, опред цвет пешки, пока не доделал
    # белые сверху
        if j < 4:
            if j+1 < 8:
                v2 = letters[i]+numbers[j+1]
                add_edge(v1, v2)
            if i+1 < 8 and j+1 < 8:
                 v2 = letters[i+1]+numbers[j+1]
                 add_edge(v1, v2)
            if 0 <= i-1 < 8 and j+1 < 8:
                v2 = letters[i-1]+numbers[j+1]
                add_edge(v1, v2)
        else:
            if j-1>=0:
                v2 = letters[i]+numbers[j-1]
                add_edge(v1, v2)
            if j-1>=0 and 0<=i+1<8:
                v2 = letters[i+1]+numbers[j-1]
                add_edge(v1, v2)
            if j-1>=0 and 0<=i-1<8:
                v2 = letters[i-1]+numbers[j-1]
                add_edge(v1, v2)

for i in graph:
    print(i, ' ', graph[i])
