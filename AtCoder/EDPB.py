n, k = map(int, input().split())
h = list(map(int, input().split()))

dp = [float('inf')] * n
dp[0] = 0

for i in range(n):
    for j in range(k+1):
        num = i+j
        if num >= n: break
        else: 
            dp[num] = min(dp[num], dp[i]+abs(h[num]-h[i]))

print(dp[-1])
