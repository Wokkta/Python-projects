def check_gl(i):
    gl=[ "A", "O", "Y", "E", "U", "I",'i','o','a','y','e','u','[',']',"'"]
    if i in gl:
        return ""
    else:
        return '.'+i.lower()

n = [input()]
word=''
for i in str(n):
    word+=check_gl(i)
print(word)
