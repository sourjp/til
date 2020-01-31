def add(a, b):
    a += b
    if a >= mod: a -= mod
    return a

mod = 10**9 + 7
N = int(input())

dp = [[[[0 for _ in range(5)] for _ in range(5)] for _ in range(5)] for _ in range(101)]
dp[0][0][0][0] = 1

for n in range(N):
    for i in range(5):
        for j in range(5):
            for k in range(5):
                for l in range(5):
                    if i == 1 and j == 2 and l == 3: continue
                    if i == 1 and k == 2 and l == 3: continue
                    if j == 1 and k == 2 and l == 3: continue
                    if j == 2 and k == 1 and l == 3: continue
                    if j == 1 and k == 3 and l == 2: continue
                    add(dp[n+1][j][k][l], dp[n][i][j][k])
    print(dp)
    res = 0
    for i in range(5):
        for j in range(5):
            for k in range(5):
                add(res, dp[N][i][j][k])

print(res)

