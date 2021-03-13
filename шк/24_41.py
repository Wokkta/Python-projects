stroka='AAAAAABBBBBBBBCCCCCCCCAAAAAABBBBBBBBCCCCCCCAAAAAABBBBBBBAAAAAABBBBBBBBCCCCAAAAAABBBBBBBBCCCAAAAAABBBBBBBBCCCCCCCCBCCCCCAABBBCBBBBBCCCCCCAAAAAABBBBBBBBCCCCCCCCBCC'
stroka=stroka.lower()
counter=0
for i in range(1,len(stroka)-2):
    if stroka[i-1]=='C':
        q=1
        while stroka[i-2+q]=='C':
            counter+=1
            q+=1
        if counter>4:
            counter=0
            stroka=stroka[:stroka[i-1]]+stroka[stroka[i-2+q]:]
        else:
            print(i,counter,stroka[stroka[i-1]:stroka[i-2+q]].capitalize())
