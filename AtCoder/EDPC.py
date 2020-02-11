n = int(input())

dp = [[0, 0, 0] for _ in range(n)]
a, b , c = map(int, input().split())
dp[0] = [a, b, c]
for i in range(n-1):
    a, b ,c = map(int, input().split())
    dp[i+1][0] = a + max(dp[i][1], dp[i][2])
    dp[i+1][1] = b + max(dp[i][0], dp[i][2])
    dp[i+1][2] = c + max(dp[i][0], dp[i][1])

print(max(dp[-1]))