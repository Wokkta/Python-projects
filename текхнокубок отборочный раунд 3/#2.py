num_of_tests=int(input())
n_array=[]
ans=[]
for i in range(num_of_tests):
    n=int(input())
    n_array.append(n)
def dig(n):
    count=n
    while n>0:
        if n%10!=0:
            if count%(n%10)!=0:
                return False
        n//=10
    return True
def check(n):
    if n<=12:
        return n
    for i in range(n,2*n):
        if dig(i):
            return i
    return -1
for q in n_array:
    if check(q)==-1 :
        if q>12:
            print(12)
        else:
            print(q)
    else:
        print(check(q))

