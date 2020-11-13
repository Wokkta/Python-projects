n = int(input())
words=[]
for i in range(n):
    words.append(input())
for i in range(len(words)):
    if len(words[i])>10:
        words[i]=str(words[i][0])+str(len(words[i][1:-1]))+str(words[i][-1])
for i in range(n):
    print(words[i])