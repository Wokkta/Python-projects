n,m = map(float,input().split())
values=[]
summ=0
ans=[]
for i in range(int(m)):
    value=float(input())
    values.append(value)
    summ+=value
if float(summ)<n:
    print("NO")
else:
    maximum=-1
    indexs=[]
    while n>0:
        maximum = -1
        for i in range(len(values)):
            if values[i] > maximum:
                maximum = values[i]
                count=i
        '''print(maximum,' maximum ',values, ' values ',count+1,' index+1')'''
        indexs.append(count+1)
        n -= maximum
        values.remove(maximum)
    while indexs:
        min=2 *summ
        for i in range(len(indexs)):
            if indexs[i]<min:
                min=indexs[i]
        ans.append(min)
        indexs.remove(min)
    for i in range(len(ans)):
        print(ans[i])