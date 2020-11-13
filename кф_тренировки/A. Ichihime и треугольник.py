t=int(input())
massa=[]
def test(a,b,c):
    if c<a+b:
        return str(a)+' '+str(b)+' '+str(c)
    else:
        return str(b)+' '+str(c)+' '+str(c)
for k in range(t):
    q=((input().split()))
    a=int(q[0])
    b=int(q[1])
    c=int(q[2])
    d=int(q[3])
    massa.append(test(a, b, c))
for i in range(len(massa)):
    print(massa[i])
