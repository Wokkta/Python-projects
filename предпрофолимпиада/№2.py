def convert_base(num, to_base=10, from_base=10):
    # first convert to decimal number
    if isinstance(num, str):
        n = int(num, from_base)
    else:
        n = int(num)
    # now convert decimal to 'to_base' base
    alphabet = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    if n < to_base:
        return alphabet[n]
    else:
        return convert_base(n // to_base, to_base) + alphabet[n % to_base]


a=[convert_base(i,3,10) for i in range(218,1300)]
b=[convert_base(i,5,10) for i in range(218,1300)]
a_ans=[]
b_ans=[]
ans=[]
for i in range(1082):
    if a[i][-1]=='2':
        a_ans.append(a[i])
    if b[i][-1]=='3':
        b_ans.append(b[i])
print(a_ans)
print(b_ans)
for i in range(len(a_ans)):
    a_ans[i]=convert_base(a_ans[i],10,3)
for i in range(len(b_ans)):
    b_ans[i]=convert_base(b_ans[i],10,5)
for i in range(len(a_ans)):
    if a_ans[i] in b_ans:
        ans.append(a_ans[i])
ans2=[]
flag = False
for i in range( len(ans)):
    if ans[i]=='218' or ans[i]=='518':
        flag=not flag
    if flag:
        ans2.append(ans[i])
print(ans)
print(ans2)
print(len(ans2))
