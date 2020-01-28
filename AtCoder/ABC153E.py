h, n = map(int, input().split())

attack = []
magic = []
for i in range(n):
    a, b = map(int, input().split())
    attack.append(a)
    magic.append(b)

dp = [[float('inf') for _ in range(h+1)] for _ in range(n+1)]
dp[0][0] = 0
print(attack, magic)
for i in range(n):
    for j in range(h+1):
        #print(max(dp[i][j], dp[i][j-attack[i]] + magic[i]))
        if dp[i+1][j] > dp[i][j]: dp[i+1][j] = dp[i][j]
        if j-attack[i] >= 0 and dp[i+1][j] > dp[i][j-attack[i]] + magic[i]: dp[i+1][j] = dp[i][j-attack[i]] + magic[i]

print(dp)