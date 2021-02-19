#33
'''
n=input()
while '222' in n or '555' in n:
	if '222' in n:
		n=n[:n.index('222')-1]+[5]+n[n.index('222')+2:]
	else:
		n=n[:n.index('555')-1]+[2]+n[n.index('555')+2:]
print(n)
'''
#4
'''
file=open('filename','r')
f=file
fives=0
flag=0
srednee=0
words_count
mm=0
word=''
for line in f:
	words=[]
	line.rstrip()
	line_copy=line
	if word in line:
		flag=1
	i=-1
	while line_copy:
		i+=1
		if i==' ':
			words.append(line_copy[:i])
			line_copy=line_copy[i:]
			i=-1
	mini=words[0]
	for i in words:
		srednee+=len(i)
		if len(i)>5:
			fives+=1
		if len(i)<mini:
			mini=i
		if i[0]=='м':
			mm+=1
	words_count+=len(words)
	srednee//=words_count
	sim_short=len(mini)
print(fives,mm,sim_short,srednee)
if flag==1:
	print("YES")

'''
#6
'''
file=open('filename','r')
f=file
dots=0
maxi=0
alle=0
for line in f:
	words=[]
	line.rstrip()
	line_copy=line
	i=-1
	while line_copy:
		i+=1
		if i==' ':
			words.append(line_copy[:i])
			line_copy=line_copy[i:]
			i=-1
	if line[-1]=='.':
		dots+=1
		alle+=len(words)
	if len(words)>maxi:
		maxi=len(words)
print(dots,maxi,alle)
'''
#5
'''
file=open('filename','r')
f=file
summ=0
summ_2=0
count=0
srednee=0
flag=0
chet=0
word=''
maxi=0
wordtest='No'
for line in f:
	if word in line:
		wordtest='YES'
	words=[]
	line.rstrip()
	line_copy=line
	i=-1
	while line_copy:
		i+=1
		if i==' ':
			words.append(line_copy[:i])
			line_copy=line_copy[i:]
			i=-1
	for i in words:
		summ+=int(i)
		count+=1
		if flag==1:
			summ_2+=int(i)
		flag=!flag
		if int(i)%2==0:
			chet+=1
		if int(i)<0:
			srednee_otric+=0
			count_otric+=1
		if int(i)>maxi:
			maxi=int(i)
srednee_otric=srednee_otric//count_otric
srednee=summ//count
print(summ,srednee,summ_2,chet,srednee_otric,maxi,wordtest)

'''