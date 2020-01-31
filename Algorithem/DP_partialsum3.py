'''
n = 5
a = (7, 5, 3, 1, 8)
A = 12
'''
n = 2
a = (7, 5)
A = 6

dp = [[float('inf') for _ in range(A+1)] for _ in range(n+1)]
dp[0][0] = 0

for i in range(n):
    for j in range(A+1):
        if j >= a[i]: dp[i+1][j] = min(dp[i][j], dp[i][j-a[i]]+1)
        else: dp[i+1][j] = dp[i][j]
print(dp)
print(dp[n][A] if dp[n][A] != float('i
nf') else -1)