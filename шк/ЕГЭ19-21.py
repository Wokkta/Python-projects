'''
19
def win(x,y,turn):
    if x+y>=77 and turn==3:
        return True
    else:
        if x+y<77 and turn==3:
            return False
        if x+y>=77 and turn <3:
            return False
    return win(x+1,y,turn+1) or win(x,y+1,turn+1) or win(x*2,y,turn+1) or win(x,y*2,turn+1)

for i in range(1,70):
    if win(7,i,1):
        print(i)
        break
'''
'''
20
def win(x,y,turn):
    if x+y>=77 and turn==4:
        return True
    else:
        if x+y<77 and turn==4:
            return False
        if x+y>=77 and turn <4:
            return False
    if turn%2==1:
        return win(x+1,y,turn+1) or win(x,y+1,turn+1) or win(x*2,y,turn+1) or win(x,y*2,turn+1)
    else:
        return win(x+1,y,turn+1) and win(x,y+1,turn+1) and win(x*2,y,turn+1) and win(x,y*2,turn+1)
for i in range(1,70):
    if win(7,i,1):
        print(i)
'''
'''
21
def win(x,y,turn):
    if x+y>=77 and (turn==5 or turn==3):
        return True
    else:
        if x+y<77 and turn==5:
            return False
        if x+y>=77 and turn <5:
            return False
    if turn%2==0:
        return win(x+1,y,turn+1) or win(x,y+1,turn+1) or win(x*2,y,turn+1) or win(x,y*2,turn+1)
    else:
        return win(x+1,y,turn+1) and win(x,y+1,turn+1) and win(x*2,y,turn+1) and win(x,y*2,turn+1)
for i in range(1,70):
    if win(7,i,1):
        print(i)
        break
'''
