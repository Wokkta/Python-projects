N, C = map(int, input().split())
files = {}
positions = {}
ans = {}
lens = []
flag = True
for i in range(N):
    file_name, place = map(str, input().split())
    files[place] = file_name
for i in range(C):
    positions[str(i+1)] = int(input())
for i in range(1, C+1):
    k = 0
    if str(i) in files:
        r = positions[str(i)]
        while r != -1:
            r = positions[str(r)]
            k+=1
            if r == positions[str(i)]:
                print(files[str(i)], 'CYCLE')
                flag=not flag
                break
            if r == 0:
                print(files[str(i)], 'BAD')
                flag=not flag
                break
        lens.append(k)
        ans[str(k)] = files[str(i)]
for i in range(len(lens)):
    for g in range(i+1, len(lens)):
        if lens[i] > lens[g]:
            lens[i], lens[g] = lens[g], lens[i]
if flag:
    print(ans[str(lens[-1])])