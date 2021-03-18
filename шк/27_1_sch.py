#1
'''
f = open('27-A_demo.txt', 'r')
mini = 1000
summ = 0
for line in f:
    x, y = map(int, line.split())
    summ += max(map(int, line.split()))
    if 0 < x-y < mini and x-y != 0 and (x-y) % 3 != 0:
        mini = ((x-y)**2)**0.5
    elif 0 < y-x < mini and x-y != 0 and (x-y) % 3 != 0:
        mini = ((x-y)**2)**0.5
summ=int(summ)
if summ % 3 == 0:
    print(summ-mini)
else:
    print(summ)
    '''
''' файл редактирован'''
#2
'''
f = open('27-A_demo.txt', 'r')
mini = 1000
summ = 0
for line in f:
    x, y = map(int, line.split())
    summ += min(map(int, line.split()))
    if 0 < x-y < mini and x-y != 0 and (x-y) % 3 != 0:
        mini = ((x-y)**2)**0.5
    elif 0 < y-x < mini and x-y != 0 and (x-y) % 3 != 0:
        mini = ((x-y)**2)**0.5
summ=int(summ)
if summ % 3 == 0:
    print(summ+mini)
else:
    print(summ)
    '''
    
#3
'''
f = open('27-A_1.txt', 'r')
mini = 1000
summ = 0
for line in f:
    x, y = map(int, line.split())
    summ += max(map(int, line.split()))
    if 0 < x-y < mini and x-y != 0 and (x-y) % 5 != 0:
        mini = ((x-y)**2)**0.5
    elif 0 < y-x < mini and x-y != 0 and (x-y) % 5 != 0:
        mini = ((x-y)**2)**0.5
summ=int(summ)
if summ % 5 == 0:
    print(summ-mini)
else:
    print(summ)
   ''' 
''' файл редактирован'''
''' файл редактирован, если конкретнее, то удалил первую строку, в задании требуется только ответ, а так я сохранил много времени'''
