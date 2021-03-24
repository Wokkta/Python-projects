'''Востановление траектории шахматного коня'''
'''https://youtu.be/S-hjsamsK8U?t=2275'''
letters='abcdefgh'
numbers='12345678'
graph={}
for l in letters:
    for n in numbers:
        graph[l+n]=set()
def add_edge(v1,v2):
    graph[v1].add(v2)
    graph[v2].add(v1)
for i in range(8):
    for j in range(8):
        v1=letters[i]+numbers[j]
        v2=''
        if 0<=i+2<8 and 0<=j+1<8:
            v2=letters[i+2]+numbers[j+1]
            add_edge(v1,v2)
        if 0<=i+2<8 and 0<=j-1<8:
            v2=letters[i+2]+numbers[j-1]
            add_edge(v1,v2)
        if 0<=i-2<8 and 0<=j+1<8:
            v2=letters[i-2]+numbers[j+1]
            add_edge(v1,v2)
        if 0<=i-2<8 and 0<=j-1<8:
            v2=letters[i-2]+numbers[j-1]
            add_edge(v1,v2)
        if 0<=i+1<8 and 0<=j+2<8:
            v2=letters[i+1]+numbers[j+2]
            add_edge(v1,v2)
        if 0<=i+1<8 and 0<=j-2<8:
            v2=letters[i+1]+numbers[j-2]
            add_edge(v1,v2)
        if 0<=i-1<8 and 0<=j+2<8:
            v2=letters[i-1]+numbers[j+1]
            add_edge(v1,v2)
        if 0<=i-1<8 and 0<=j-2<8:
            v2=letters[i-1]+numbers[j-2]
            add_edge(v1,v2)
for i in graph:
    print(i,' ',graph[i])