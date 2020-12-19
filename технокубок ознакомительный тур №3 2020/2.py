n, d = map(int, input().split())
cities = list(map(int, input().split()))

count = 0
counter=0
for i in range(n-counter):
    if cities[i-counter]+d in cities:
        count+=1
    if cities[i-counter]-d in cities:
        count+=1
    cities.remove(cities[i-counter])
    counter+=1
print(count)