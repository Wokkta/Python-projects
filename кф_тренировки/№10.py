string_one=input()
string_two=input()
alth=['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'V', 'X', 'Y', 'Z']
string_one=string_one.upper()
string_two=string_two.upper()
first_count=0
second_cout=0
first_position=0
second_position=0
def test(string_one,string_two,first_position,second_position):
    for i in range(len(string_one)):
        for j in range(len(alth)):
            if string_one[i] != string_two[i]:

                if string_one[i]==alth[j]:
                    first_position+=j
                if string_two[i]==alth[j]:
                    second_position+=j
                if second_position>first_position:
                    print(-1)
                    break
                if first_position>second_position:
                    print(1)
                    break

    if second_position==first_position:
        print(0)

test(string_one,string_two,first_position,second_position)