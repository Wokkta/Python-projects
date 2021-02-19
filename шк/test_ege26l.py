n, m = map(int, input().split())
a = []
costa = []
costb = []
colva = []
colvb = []
end = 0
summ=0
for i in range(n):
    ins = list(map(str, input().split()))
    a.append(ins)
for i in range(len(a)):
    if a[i][-1] == "A":
        costa.append(int(a[i][0]))
        colva.append(int(a[i][1]))
    else:
        costb.append(int(a[i][0]))
        colvb.append(int(a[i][1]))

    summ += int(a[i][1])*int(a[i][0])
while m > 0:
    mini = m*2
    if costa:
        for i in range(len(costa)):
            if int(costa[i]) < mini:
                mini = int(costa[i])
        m -= mini*int(colva[costa.index(mini)])
        costa.remove(mini)
    elif costb:
        for i in range(len(costb)):
            if int(costb[i]) < mini:
                mini = int(costb[i])
        if m >= mini*colvb[costb.index(mini)]:
            m -= mini*colvb[costb.index(mini)]
            end += colvb[costb.index(mini)]
        elif m > mini:
            end += m//mini
            m -= mini*m//mini
        costb.remove(mini)
    else:
        break
print(end, m)
