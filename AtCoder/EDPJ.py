N = int(input())
A = list(map(int, input().split()))
dp = [[[-1 for _ in range(N+1)] for _ in range(N+1)] for _ in range(N+1)]

def func(i, j, k):
    if dp[i][j][k] >= 0: return dp[i][j][k]
    if i == 0 and j == 0 and k == 0: return 0.0

    res = 0.0
    if i > 0: res += func(i-1, j, k) * i
    if j > 0: res += func(i+1, j-1, k) * j
    if k > 0: res += func(i, j+1, k-1) * k
    res += N
    res *= 1.0 / (i + j + k)

    dp[i][j][k] = res
    print(dp)
    return dp[i][j][k]

one = 0
two = 0
three = 0
for a in A:
    if a == 1: one += 1
    if a == 2: two += 1
    if a == 3: three += 1

print(func(one, two, three))

