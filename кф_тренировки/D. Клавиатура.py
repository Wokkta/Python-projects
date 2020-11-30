# https://codeforces.com/group/XWOeQO4RLM/contest/206799/problem/D
sdvig=input()
if sdvig=="R":
	sdvig=-1
else:sdvig=1
text=input()
keyboard='qwertyuiopasdfghjkl;zxcvbnm,./'
final_text=''
for i in text:
	final_text+=keyboard[(keyboard.index(i)+sdvig)]
print(final_text)