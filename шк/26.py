f = open('26_demo.txt', 'r')
f.readline()
mini = 100000
n = 8200
nums = []
numscop = []
for line in f:
    nums.append(int(line.strip()))
f.close()
nums = sorted(nums)
numscop = nums
ans = []
while sum(ans) <= n:
    ans.append(min(numscop))
    numscop.remove(min(numscop))
ans.pop()
if (n-sum(ans)) in numscop:
    q = n-sum(ans)
    print(q, ans[-1], sum(ans))
    ans.append(q)
if ans[-1]+21 in numscop:
	q=ans[-1]+24
	#print(q)
	ans.remove(ans[-1])
	#print(q)
	ans.append(q)
print(len(ans), ans[-1],)


