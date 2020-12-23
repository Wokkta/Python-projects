'''https://contest.yandex.ru/contest/22235/download/A/'''
import random
n=int(input())
string=list(input())
def quicksort(nums):
   if len(nums) <= 1:
       return nums
   else:
       q = random.choice(nums)
   l_nums = [n for n in nums if n < q]
 
   e_nums = [q] * nums.count(q)
   b_nums = [n for n in nums if n > q]
   return quicksort(l_nums) + e_nums + quicksort(b_nums)   
string=quicksort(string)
ans=''
for i in range(1,n):
	ans+=string[-i]

print(ans)

