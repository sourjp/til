W = 9
n = 6
wv = [(2,3),(1,2),(3,6),(2,1),(1,3),(5,85)]

dp = [[0 for _ in range(W+1)] for _ in range(n+1)]

for i in range(n):
    print(dp[i])
    for w in range(W+1):
        if w >= wv[i][0]:
            print('w:', w, 'pick:', dp[i][w-wv[i][0]] + wv[i][1], 'unpick:', dp[i][w])
            dp[i+1][w] = max(dp[i][w-wv[i][0]] + wv[i][1], dp[i][w])
        else:
            dp[i+1][w] = dp[i][w]
    print(dp[i+1])

print(dp[n][W], dp)