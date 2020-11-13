t=int(input())
massa=[]
def test(x,n,m):
    test_value=0
    while n>0 and m>0 or x>0:
        '''test_value+=1
        if test_value>30000:
            return "PROBLEMS test_value=={}".format(test_value)'''
        if x >= 40 and n > 0:
            x=x//2+10
            n-=1
            print(" \-1\ n ={} m = {} x = {}  place 1".format(n,m,x))
        elif m>0:
            if n==0 and x-(10*m)<=0:
                print(" n ={} \-1\ m = {} x = {}  place 2".format(n, m, x))
                return "YES"
            elif n>0:
                x = x // 2 + 10
                n -= 1
                print(" \-1\ n ={} m = {} x = {} place 3".format(n, m, x))
        if x<=0:
            return "YES"
        elif x>0 or n<=0 and m<=0:
            return "NO"


for k in range(t):
    q=((input().split()))
    x = int(q[0])
    n = int(q[1])
    m = int(q[2])
    massa.append(test(x, n, m))

for i in range(len(massa)):
    print(massa[i])
'''check your previos var at codeforses'''