string=input()
if string.upper()==string or string==string[0].lower()+string[1:].upper():
    string=string[0].upper()+string[1:].lower()
print(string)
