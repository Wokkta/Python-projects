a=1
while True:
    for x in range(1000):
        for y in range(1000):
            if not((x+2*y<a) or (x<a) or (y<a)):
                break
        else:
            continue
        break
    else:
        print(a)
    a+=1
