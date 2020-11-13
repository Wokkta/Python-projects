'''n,k=map(int, input().split(" "))
def test(n,k):
    users=[]
    q=0
    users.append((input().split(" ")))
    global winners
    winners=users
    print(winners[0])
    i=0
    while i<n:

        print(14)
        if i==len(winners[0]) or q==len(winners[0]):

            print(4,len(winners[0]))
        if int(winners[0][i])<int(winners[0][k-1]) and i+q!=n-1:
            q+=1
            winners[0].remove(winners[0][i])
            print(2)
        i+=1
    for i in range(len(winners)):
        if winners[0][i]!=0:
            print(1)

        else:
            winners[0].remove(winners[0][i])
            print(3)
    return (len(winners[0]))
print(test(n,k))
print(winners[0])'''
'решение Артема(оно работает '
n, k = map(int, input().split(' '))
points = list(map(int, input().split(' ')))

def count(array, num):
    count_nums = 0
    for i in range(len(array)):
        if array[i] >= num and array[i] > 0:
            count_nums += 1
    return count_nums

print(count(points, points[k-1]))