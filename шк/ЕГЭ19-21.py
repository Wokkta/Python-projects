w=5
n=53
#19
q=59
def win(x,y,turn):
    if x+y>=q and turn==2:
        return True
    else:
        if x+y<q and turn==2:
            return False
        if x+y>=q and turn <2:
            return False
    return win(x+1,y,turn+1) or win(x,y+1,turn+1) or win(x*2,y,turn+1) or win(x,y*2,turn+1)

for i in range(1,n):
    if win(w,i,1):
        print(i,'19')
        break


#20
def win(x,y,turn):
    if x+y>=q and turn==4:
        return True
    else:
        if x+y<q and turn==4:
            return False
        if x+y>=q and turn <4:
            return False
    if turn%2==1:
        return win(x+1,y,turn+1) or win(x,y+1,turn+1) or win(x*2,y,turn+1) or win(x,y*2,turn+1)
    else:
        return win(x+1,y,turn+1) and win(x,y+1,turn+1) and win(x*2,y,turn+1) and win(x,y*2,turn+1)
for i in range(1,n):
    if win(w,i,1):
        print(i,'20')


#21
def win(x,y,turn):
    if x+y>=q and (turn==5 or turn==3):
        return True
    else:
        if x+y<q and turn==5:
            return False
        if x+y>=q and turn <5:
            return False
    if turn%2==0:
        return win(x+1,y,turn+1) or win(x,y+1,turn+1) or win(x*2,y,turn+1) or win(x,y*2,turn+1)
    else:
        return win(x+1,y,turn+1) and win(x,y+1,turn+1) and win(x*2,y,turn+1) and win(x,y*2,turn+1)
for i in range(1,n):
    if win(w,i,1):
        print(i,'21')
        break

#24
'''
f=open('24_varianty_6-14.txt','r')
n=f.readline()
count=0
ans=[]
for i in range(len(n)-1):
    for j in range(1,len(n)):
        if i!=j:
            count+=1
        else:
            ans.append(count)
            count=1
print(max(ans))
'''