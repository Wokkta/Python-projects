'''import time
qw=time.time()
num_of_t=int(input())
lenths=[]
strs=[]
def counter(string):
    count=0
    if string.count(')')==len(string):
        return len(string)
    while string[-1]==')':
        count+=1
        string=string[:-1]
    return count
for i in range(num_of_t):
    lenth_of_string=int(input())
    lenths.append(lenth_of_string//2)
    string=input()
    strs.append(string)
for i in range(num_of_t):
    if lenths[i]-counter(strs[i])<0:
        print('Yes')
    else:
        print('No')
print(time.time()-qw)'''
num_of_t=int(input())
def counter(string):
    count=0
    if string.count(')')==len(string):
        return len(string)+1
    while string[-1]==')':
        count+=1
        string=string[:-1]
    return count
for i in range(num_of_t):
    lenth_of_string=int(input())
    lenth_of_string//=2
    string=input()
    if lenth_of_string-counter(string)<0:
        print('Yes')
    else:
        print('No')


