'''https://codeforces.com/edu/course/2/lesson/6/1/practice/contest/283911/problem/A'''
n,k= list(map(int, input().split()))
array=list(map(int, input().split()))
asked=list(map(int, input().split()))
array=array[:n]
def bin_search(list1, n):
    #return true or false
    low = 0
    high = len(list1) - 1
    mid = 0

    while low <= high:
        # for get integer result
        mid = (high + low) // 2

        # Check if n is present at mid
        if list1[mid] < n:
            low = mid + 1

            # If n is greater, compare to the right of mid
        elif list1[mid] > n:
            high = mid - 1

            # If n is smaller, compared to the left of mid
        else:
            return True

            # element was not present in the list, return -1
    return False


for i in range(len(asked)):
    if bin_search(array,asked[i]):
        print("YES")
    else:print("NO")

