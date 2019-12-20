import math

n = int(input())

ans = float('inf')
for i in range(1, math.ceil(n**(1/2))):
    if n%i == 0:
        a = i
        b = n // i
        d = a-1 + b-1
        ans = min(ans, d)

print(ans)