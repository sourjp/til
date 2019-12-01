import math

N = int(input())

for i in range(1, int(math.sqrt(N) + 1)):
    if N % i == 0:
        val = N // i
        ans = len(str(val))
        print(val, ans, math.sqrt(N))

print(ans)