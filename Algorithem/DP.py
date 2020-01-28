a = [10, -5, 6, 9, -2, 3]

dp = [0 for _ in range(len(a)+1)]

dp[0] = 0
for i in range(len(a)):
    dp[i+1] = max(dp[i], dp[i] + a[i])

print(dp[-1], dp)