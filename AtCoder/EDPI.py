n = int(input())
p = list(map(float, input().split()))

dp = [[.0 for _ in range(n+1)] for _ in range(n+1)]
dp[0][0] = 1.0

for i in range(n):
    for j in range(i+1):
        dp[i+1][j+1] += dp[i][j] * p[i]
        dp[i+1][j] += dp[i][j] * (1-p[i])

ans = sum(dp[-1][n//2+1:])

#print(dp)
print(ans)