clear=[]
for i in range(174457,174506):
    dels=[1,i]
    d=2
    while d**2<=i:
        if i%d==0:
            dels.append(d)
            if i//d>d:
                dels.append(i//d)
        if len(dels)>4:
            break
    if len(dels)==4:
        clear.append(dels)
print(clear)
