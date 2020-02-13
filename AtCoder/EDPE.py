n, W = map(int, input().split())
w = []
v = []
V = 0
for i in range(n):
    tmp1, tmp2 = map(int, input().split())
    w.append(tmp1)
    v.append(tmp2)
    V += tmp2

dp = [[float('inf') for _ in range(V+1)] for _ in range(n+1)]
dp[0][0] = 0

for i in range(n):
    for j in range(V+1):
        if j-v[i] >= 0: dp[i+1][j] = min(dp[i][j], dp[i][j-v[i]]+w[i])
        else: dp[i+1][j] = dp[i][j]

ans = 0
for i in range(V+1):
    if dp[-1][i] <= W: ans = i

print(dp)
print(ans)