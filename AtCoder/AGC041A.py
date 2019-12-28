def upper_cnt(a, b):
    upper_cnt = n-b + 1
    a += upper_cnt
    upper_cnt += ((n-a) // 2)    
    return upper_cnt

def lower_cnt(a, b):
    lower_cnt = a-1 + 1
    b -= lower_cnt
    lower_cnt += ((b-1) // 2)
    return lower_cnt

n, a, b = map(int, input().split())

if 0 == (b-a) % 2:
    print((b-a) // 2)

else:
    up = upper_cnt(a, b)
    low = lower_cnt(a, b)
    print(min(up, low))
