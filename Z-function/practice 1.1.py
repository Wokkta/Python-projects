t=int(input())
answers=[]
def is_palindrome(string):
    for k in range(len(string)):
        test_prefix= string[0:k]
        for i in range(len(test_prefix)):
            if test_prefix[i]!=test_prefix[-i]:
                return k-1
    return len(string)
for q in range(t):
    text=input()
    answers.append(is_palindrome(text))

for i in range(len(answers)):
    print(answers[i])