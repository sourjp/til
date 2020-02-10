'''
桁DP

dp[i][j][k]
i桁目まで決めて、j個の非ゼロを使って、
k -> 0: そこまでの桁はNと一致
k -> 1: そこまでの桁でですにN以下であることが確定

i = 0-n
j = 1-K

'''

s = input()
n = len(s)
K = int(input())

dp = [[[0 for _ in range(2)] for _ in range(K+1)] for _ in range(n+1)]
dp[0][0][0] = 1

for i in range(n):
    for j in range(K):
        for k in range(2):
            nd = int(s[i])
            print('nd:', nd)
            for d in range(10):
                ni = i+1
                nj = j
                nk = k
                if d != 0: nj += 1
                if nj > K: continue
                if k == 0:
                    if d > nd: continue
                    if d < nd: nk = 1
                dp[ni][nj][nk] += dp[i][j][k]
                print(dp)
                print(ni, nk, nk, i, j, k, d)

ans = dp[n][K][0] + dp[n][K][1]
print(ans)                
