letters = 'abcdefgh'
numbers = '12345678'
graph = {l + n: set() for l in letters for n in numbers}
rotation = 1
#bl,wh=map(input.split())
bl,wh='up','down'
if bl=='up' and'down':
    rotation*=1
else:
    rotation!=-1
def add_edge(v1, v2):
    graph[v1].add(v2)
    graph[v2].add(v1)

# выводит возможные ходы в обе стороны
for i in range(8):
    for j in range(8):
        v1 = letters[i]+numbers[j]
        v2 = ''
        if 0 <= rotation*(j+1) < 8:
            v2 = letters[i]+numbers[rotation*(j+1)]
            add_edge(v1, v2)
        if 0 <= rotation*(i+1) < 8 and rotation*(j+1) < 8:
            v2 = letters[rotation*(i+1)]+numbers[rotation*(j+1)]
            add_edge(v1, v2)
        if 0 <= rotation*(i-1) < 8 and rotation*(j+1) < 8:
            v2 = letters[rotation*(i-1)]+numbers[rotation*(j+1)]
            add_edge(v1, v2)
for i in graph:
    print(i, ' ', graph[i])
