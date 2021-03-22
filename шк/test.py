i = "1" +"0"*75
while "10" in i or "1" in i:
    if "10" in i:
        i = i[:i.index("10")]+"001"+i[i.index("10")+2:]
        
    else:
        i = i[:i.index("1")]+"00"+i[i.index("1")+1:]
print (i)
print(i.count('0'))
