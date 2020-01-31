
n = 5
a = (7, 5, 3, 1, 8)
A = 12
'''
n = 4
a = (4, 1, 1, 1)
A = 5
'''

dp = [[0 for _ in range(A+1)] for _ in range(n+1)]
dp[0][0] = 1

for i in range(n):
    for j in range(A+1):
        if j >= a[i]: dp[i+1][j] = dp[i][j] + dp[i][j-a[i]]
        else: dp[i+1][j] = dp[i][j]
print(dp)
print(dp[n][A])