#37
'''
def f(n):
    dels=[1,n]
    d=2
    while d**2<=n:
        if n%d==0:
            dels.append(d)
            if n//d>d:
                dels.append(n//d)
        d+=1
    return len(dels)
for i in range(248015,251576,2):
    q=f(i)
    if q%2==1:
        print(i-248015+1,i,q,int(i**0.5))

'''
#63
'''
count=0
def f(n):
    dels=[1,n]
    d=2
    while d**2<=n:
        if n%d==0:
            dels.append(d)
            if n//d>d:
                dels.append(n//d)
        d+=1
    return len(dels)
for i in range(2532000,2532161):
    if f(i)==2:
        print(i-2532000+1,i)
        count+=1
    if count==5:
        break
'''
#70
'''
for i in range(2,10001):
    divs=[1]
    d=2
    while d**2<=i:
        if i%d==0:
            divs.append(d)
            if i//d>d:
                divs.append(i//d)
        d+=1
    summ=0
    for q in divs:
        summ+=q
    if summ==i:
        print(i,len(divs))
'''
#73
'''
count=0
for i in range(2,20001):
    divs=[1]
    d=2
    while d**2<=i:
        if i%d==0:
            divs.append(d)
            if i//d>d:
                divs.append(i//d)
        d+=1
    summ=0
    for q in divs:
        summ+=q
    if summ>i:
        count+=1
print(count)
'''
#74 
'''
count=0
for i in range(2,10001):
    divs=[1]
    d=2
    while d**2<=i:
        if i%d==0:
            divs.append(d)
            if i//d>d:
                divs.append(i//d)
        d+=1
    summ=0
    for q in divs:
        summ+=q
    if summ<i:
        count+=1
print(count)
'''
#75
'''
for i in range(1000,20001):
    divs=[1]
    d=2
    while d**2<=i:
        if i%d==0:
            divs.append(d)
            if i//d>d:
                divs.append(i//d)
        d+=1
    summ=0
    for q in divs:
        summ+=q
    if summ+1==i:
        print(i)
'''
#76
'''
for i in range(1000,20001):
    divs=[1]
    d=3
    while d**2<=i:
        if i%d==0:
            divs.append(d)
            if i//d>d:
                divs.append(i//d)
        d+=1
    summ=0
    for q in divs:
        summ+=q
    if 999<summ<20001 :
        print(i,summ)
'''    
	
#81
'''
for i in range(2,263001):
    divs=[1,i]
    d=2
    while d**2<=i:
        if i%d==0:
            divs.append(d)
            if i//d>d:
                divs.append(i//d)
        d+=1
    summ=0
    for q in divs:
        summ+=q
    divs=[1,summ]
    d=2
    while d**2<=summ:
        if summ%d==0:
            divs.append(d)
            if summ//d>d:
                divs.append(summ//d)
    summ=0
    for q in divs:
        summ+=q
        if summ==2*i:
            print(i)
		'''
#84
'''
string=[]
ele=[]
for i in range(87921,88188):
    summ=0
    q=i
    mn=1
    while q>0:
        summ+=q%10
        mn*=q%10
        q//=10
    if summ%14==0 and mn%18==0:
        print(summ, mn)
	'''
#91
'''
summ=0
for i in range(4099,26986):
    divs=[]
    d=2
    while d**2<=i:
        if i%d==0:
            divs.append(d)
            if i//d>d:
                divs.append(i//d)
    if len(divs)==1:
        summ+=divs[0]
print(summ)
'''
#95
'''
summar=0
for i in range(1395,22718):
    q=i
    nums=[]
    summ=0
    while q>0:
        nums.append(q%10)
        q//=10
    num=nums[0]
    for w in range(1,len(nums)):
        if nums[w]<=num:
            summ+=1
        else:
            break
        num=nums[w]
    if summ!=len(nums):
        pass
    else:
        summar+=i
print(summar)
'''
