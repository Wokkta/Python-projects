n,m = input().split()
values=[]
for i in range(int(m)):
    value=float(input())
    values.append(value)
indexes=[]
n = int(n)
global array_summ
array_summ=[0]
maximum=-1
def find_max(array):
    maximum=-1
    for i in range(len(array) ):
        array_summ[0]+=array[i]
        if array[i]>maximum:
            maximum=array[i]
    indexes.append(i)
    return maximum
find_max(values)
if array_summ[0]<n:
    print('No')
else:
    while n>0:
        n-=maximum
        values.remove(values[values.index(maximum)])
        find_max(values)
    for i in range(len(indexes)):
        print(indexes[i])
