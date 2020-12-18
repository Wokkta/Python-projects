def convert_base(num, to_base=10, from_base=10):
    # first convert to decimal number
    if isinstance(num, str):
        n = int(num, from_base)
    else:
        n = int(num)
    # now convert decimal to 'to_base' base
    alphabet = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    if n < to_base:
        return alphabet[n]
    else:
        return convert_base(n // to_base, to_base) + alphabet[n % to_base]
base,number,k=map(str,input().split())
base=int(base)
k=int(k)
num_ten_base=int(convert_base(number,10,base))
num_ten_base**=k
number=convert_base(num_ten_base,base,10)
print(number[-1])