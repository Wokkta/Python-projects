f= open('','r')
flag=0
for line in f:
	if flag==0:
		Size,rand=map(int,input().split())
		flag=1
	