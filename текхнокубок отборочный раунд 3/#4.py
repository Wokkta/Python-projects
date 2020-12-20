rap=input()
x,y=map(int,input().split())
if rap.count('1')>rap.count('0'):
    rap=rap.replace('?','1')
elif rap.count('1')<rap.count('0'):
    rap=rap.replace('?','0')
else:
    if x<y:
        rap=rap.replace('?',"0")
    else:
        rap = rap.replace('?', "1")
count=0
if '10' in rap:
    count+=y*len(rap)
if '01'in rap:
    count+=x*len(rap)
print(count)