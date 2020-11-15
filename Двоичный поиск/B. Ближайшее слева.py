'''https://codeforces.com/edu/course/2/lesson/6/1/practice/contest/283911/problem/B'''
n,k= list(map(int, input().split()))
array=list(map(int, input().split()))
asked=list(map(int, input().split()))
array=array[:n]
def bin_search(list1, searching_value):
    #return true or false
    low = -1 #<x
    high = len(list1) #>x
    mid = 0
    while low +1 < high:
        # if array[low]==array[high-1]
        # for get integer result
        mid = (high + low) // 2

        # Check if n is present at mid
        if list1[mid] < searching_value:
            low = mid

            # If n is greater, compare to the right of mid
        elif list1[mid] > searching_value:
            high = mid
        else:
            return 0
    return low

for i in range(len(asked)):
    print(bin_search(array,asked[i])+1)