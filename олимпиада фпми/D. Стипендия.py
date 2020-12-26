'''https://contest.yandex.ru/contest/22235/problems/D/'''
import random
num_of_obj,max_income=map(int,input().split())
objs=(list(map(int,input().split())))
def quicksort(nums):
   if len(nums) <= 1:
       return nums
   else:
       q = random.choice(nums)
   l_nums = [n for n in nums if n < q]
   e_nums = [q] * nums.count(q)
   b_nums = [n for n in nums if n > q]
   return quicksort(l_nums) + e_nums + quicksort(b_nums)
def summ(massive):
	summ=0
	for i in range(len(massive)):
		summ+=massive[i]
	return summ
def check_till(num,costs):
	maximum=-1
	costs=quicksort(costs)
	if num>costs[-1]*len(costs):
		return num-summ(costs)
	else:
		for i in costs:
			if num<i and maximum==-1:
				print('1 one')
				return num
			elif num>i:
				if num-1>maximum:
					print('2 one',num-i)
					maximum=num-i
			elif num<i:
				print('3 one')
				return maximum

print(check_till(max_income,objs),' answer')
'''
test input
3 10
5 4 1
'''