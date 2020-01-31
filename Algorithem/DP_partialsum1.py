n = 3
a = (7, 5, 3)
A = 10

dp = [[0 for _ in range(A+1)] for _ in range(n+1)]
dp[0][0] = True
for i in range(n):
    for j in range(A+1):
        if j >= a[i]: dp[i+1][j] = dp[i][j-a[i]] or dp[i][j]
        else: dp[i+1][j] = dp[i][j]

print(dp[n][A])