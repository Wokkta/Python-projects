for x in range(101,10001):
    L = x
    M = 65
    if L % 2 == 0:
      M = 52
    while L != M:
      if L > M:
        L = L - M
      else:
        M = M - L
    if M==26:
        print(x)
        break
