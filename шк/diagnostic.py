with open(text.txt) as text:
	lines=text.readlines()
counter=0
marker= # what you need to find
for i in range(len(lines)):
	if lines[i].count(marker)>0:
		counter+=lines[i].count((marker))