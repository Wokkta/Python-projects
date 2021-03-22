#73
'''
count=0
a=[]
for i in range(1005,147871):
    if str(i).count('1')==0:
        if int(max(list(str(i))))-int(min(list(str(i))))<4:
            count+=1
            a.append(i)
print(count,a[-25])
   '''
#74
'''
count=0
closest=0
a=[]
for i in range(5903,174204):
    flag=0
    check=0
    for q in range(1,10):
        if q>4:
            check+=str(i).count('{}'.format(q))
        if str(i).count('{}'.format(q))>1:
            flag=0
            break
        else:
            flag=1
    if flag==1 and check==3:
        count+=1
        
        #if i>28000 and i<32000:
         #   a.append(i)
           
# через массив нашел близжайшие
print(count,29874)
'''    
#75
'''
def g(n):
    summ=0
    while n:
        summ+=n%10
        n//10
    return summ
def f(n):
    for q in range(1,10):
        if str(n).count('{}'.format(q))>1:
            return True
    return False
count=0
check=[]
for i in range(138,603885,3):
    if f(i):
        count+=1
        if check==[]:
            check.append(g(i))
        else:
            if g(i)>check[-1]:
                check.append(g(i))
print(count,check[-1])
'''
#76
'''
count=0
a=0
def f(n):
    q=str(n)
    for w in range(1,len(q)):
        if q[w]>q[0]:
             return False
    return True
for i in range(1007,746001):
    if f(i):
        if str(i).count('5')%2==0:
                count+=1
                if str(i)[:2]=='50':
                    a=i
print(count,a)
'''
#77
'''
count=0
srednee=0
aver=[]
def q(aver,n):
    summ=0
    for i in aver:
        summ+=int(i)
    return int(summ//n)
def g(n):
    summ=0
    while n:
        summ+=n%10
        n//10
    return summ
for i in range(2020,647039):
    if g(i)<10:
        a=min(list(str(i)))
        if str(a)!=str(i)[0] and str(a)!=str(i)[1] and str(a)!=str(i)[2]:
            count+=1
            aver.append(i)
averenge=q(aver,count)
print(count,averenge)
'''
#78
'''
count=0
num=0
def dels(n):
    divs=[1,n]
    d=2
    while d**2<=n:
        if n%d==0:
            divs.append(d)
            if n//d>d:
                divs.append(n//d)
        d+=1
    return len(divs)
def g(n):
    q=str(n)
    check=int(q[0])
    for i in range(1,len(q)):
        if int(q[i])>check:
            return False
        check=int(q[i])
    return True
for i in range(1082,129933):
    if g(i):
        if dels(i)%3==0:
            count+=1
            if str(i)[0]=='7':
                num=i
print(count,num)
'''
#79
'''
count=0
num=0
def dels(n):
    divs=[1,n]
    d=2
    while d**2<=n:
        if n%d==0:
            divs.append(d)
            if n//d>d:
                divs.append(n//d)
        d+=1
    return len(divs)
for i in range(2095,19403):
    if dels(i)==2:
        if int(str(i)[0])>int(str(i)[-1]):
            count+=1
            if str(i)[-2:]=='21':
                num=i
print(count,num)
'''
