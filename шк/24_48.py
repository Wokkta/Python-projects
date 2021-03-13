stroka='ABCFFFDCABCCBAACCCCDEEADBCADFECAEEEAAEEFEAABCCCBAACCDDCCDEEADBCADFECAEEEAAEEFEAABCCFFFBAACCCCDEEADBCADFECAEEEAAEEFEADDDABCCBAACCCCDEEADBCADFECAEEEAAEEFEA'
alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
counter=0
for i in range(len(stroka)-3):

    if alphabet.index(stroka[i])<=alphabet.index(stroka[i+1]) :
        if alphabet.index(stroka[i+1])<=alphabet.index(stroka[i+2]) :
            counter+=1
    else:
        print(counter,alphabet.index(stroka[i-2]))
