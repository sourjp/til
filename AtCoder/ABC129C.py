n, m = map(int,input().split())
stairs = set([int(input()) for i in range(m)])
dp = [0] * (n+1)
dp[0] = 1

for i in range(1, n+1):
    if i in stairs: 
        dp[i] = 0
        continue

    dp[i] = (dp[i-1] + dp[i-2]) % (10**9+7)

print(dp[n])