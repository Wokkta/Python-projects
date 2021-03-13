f=open('24.txt','r')
count=0
for line in f:
    for i in range(1,len(line)-1):
        if line[i-1]=='A' and line[i+1]=='R':
            count+=1
            break
print(count)
