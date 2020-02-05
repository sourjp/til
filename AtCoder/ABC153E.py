h, n = map(int, input().split())
magic = [tuple(map(int, input().split())) for _ in range(n)]
#magic = [list(map(int, input().split())) for _ in range(n)]

dp = [float('inf')] * (h+1)
dp[0] = 0

for i in range(h):
    for d, c in magic:
        next_index = min(i+d, h)
        dp[next_index] = min(dp[next_index], dp[i]+c)
        #print(d, c, dp)

print(dp[-1])

'''
h, n = map(int, input().split())

attack = []
magic = []
for i in range(n):
    a, b = map(int, input().split())
    attack.append(a)
    magic.append(b)

dp = [[float('inf') for _ in range(h+1)] for _ in range(n+1)]
dp[0][0] = 0
#print(attack, magic)
for i in range(n):
    for j in range(h+1):
        #print(max(dp[i][j], dp[i][j-attack[i]] + magic[i]))
        if dp[i+1][j] > dp[i][j]: dp[i+1][j] = dp[i][j]
        if dp[i+1][min(j+attack[i], h)] > dp[i+1][j]+magic[i]: dp[i+1][min(j+attack[i], h)] = dp[i+1][j]+magic[i]

print(dp[-1][-1])
'''
