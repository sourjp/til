s = input()

mod = 10**9 + 7
dp = [[0]*13 for _ in range(len(s))]


if s[-1] == '?':
    i = 0
    while i < 10:
        dp[0][i] = 1
        i += 1

    else:
        dp[0][s[-1]] = 1

k = -1
while k > -len(s):
    if s[k-1] == '?':
        for i in range(13):
            for j in range(10):
                dp[-k][(i*10%13+j)%13] += dp[k][i]
                dp[-k][(i*10%13+j)%13] %= mod
    else:
        for i in range(13):
                dp[-k][(i*10%13+s[-k+1])%13] += dp[k][i]
                dp[-k][(i*10%13+s[-k+1])%13] %= mod
    k -= 1

print(dp)