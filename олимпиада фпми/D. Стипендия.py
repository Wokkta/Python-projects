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
	costs=quicksort(costs)
	if num<costs[0]:
			return num
	maximums=[]
	current_max=0
	i=0
	while num - costs[i]>=0 and i<=num_of_obj:
		print(num,costs[i])
		current_max=num-costs[i]
		num-=costs[i]
		maximums.append(current_max)
		i+=1
	maximums=quicksort(maximums)
	print(maximums)
	return maximums[-1]

print(check_till(max_income,objs),' answer')
'''
test input
3 10
5 4 1
'''