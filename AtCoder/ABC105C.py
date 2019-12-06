number = int(input())

def to_bin(n):
    if n == 0:
        return [0]
    
    digits = []
    i = 0
    base = 1
    while n != 0:
        if n % (base * 2) == 0:
            digits.append('0')
        else:
            digits.append('1')
            n -= base
        i+= 1
        base *= -2
    return digits[::-1]

ans_list = to_bin(number)

for ans in ans_list:
    print(ans, end='')
