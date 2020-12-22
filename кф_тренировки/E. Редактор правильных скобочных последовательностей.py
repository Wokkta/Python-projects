'''https://codeforces.com/problemset/problem/670/E?locale=ru'''
num_of_slice,num_of_operations,position=map(int,input().split())
position-=1
psp=input()
comands=input()
#print(psp[:1]+psp[-1:])
def do_operation(string,position,comands):
    if len(comands)==0:
        print(string)
        return 0
    print(comands,' comands ',string,' string ',position,' position')
    if comands[0]=='R':
        position+=1
    elif comands[0]=='L':
        position-=1
    elif comands[0]=='D':
        if string[position]=='(':
            opened=1
            closed=0
            i=1
            while opened!=closed:
                print('something 1')
                if string[position+i]==')':
                    closed+=1
                else:
                    opened+=1
                i+=1
            end_position=position+i
            string=string[:position]+string[end_position:]
        else:
            opened=0
            closed=1
            i=-1
            while opened!=closed:
                print('something 2')
                if string[position+i]==')':
                    closed+=1
                else:
                    opened+=1
                i-=1
            end_position=position+i
            string=string[:end_position]+string[position:]
    do_operation(string,position,comands[1:])
do_operation(psp,position,comands)
