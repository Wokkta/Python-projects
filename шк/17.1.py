#48
'''
maxi=0
c=1
for i in range(1985, 8529):
    if i%2!=0 and i%7!=0 and i%47!=0:
        if (i%10+(i%100)//10)%6==0:
            maxi=i
            c*=i
print(maxi,int(str(c)[-3]),int(str(c)[-2]),int(str(c)[-1]))
        
'''
#51
'''
maxi=0
count=0
for i in range(7**6,7**7):
    if i%3==2 and i%8!=3 and i%12!=5:
        maxi=i
        count+=1
print(count,maxi)
'''
#52
'''
count=0
maxi=0
for i in range(4096,15625):
    if i%(16*16)==250:
        maxi=i
        count+=1
print(count,maxi)
'''
#53
'''
summ=0
mini=10**5
for i in range(10,1179,2):
    if i%10!=2 and i%10!=0 and i%10!=6 and i%10!=8 and i%100!=14:
        summ+=i
        if i<mini:
            mini=i
print(summ,mini)
'''
#63
'''
count=0
summ=0
a=1840
while a%7!=0:
    a+=1
for i in range(a,9053,7):
    if i%23!=0:
        count+=1
        summ+=i
print(count,summ)
'''
