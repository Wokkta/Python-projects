n,m = map(float,input().split())
values=[]
values_copy=[]
summ=0
ans=[]
for i in range(int(m)):
    value=float(input())
    values.append(value)
    values_copy.append(value)
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
                count=values_copy.index(values[i])
        #print(maximum,' maximum ',values, ' values ',count+1,' index+1')
        #print(count, ' values_copy.index(values[i])  ',values_copy)
        indexs.append(count+1)
        n -= maximum
        values.remove(maximum)
# everething down is clear
    while indexs:
        min=2 *summ
        for i in range(len(indexs)):
            if indexs[i]<min:
                min=indexs[i]
        ans.append(min)
        indexs.remove(min)
    for i in range(len(ans)):
        print(ans[i])
'''test input
5 4
1
3.5
2
4'''
'''
3 5
1
0.8
1.2
2
1.5'''