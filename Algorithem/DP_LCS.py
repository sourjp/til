
def lcs(s, t):
    sn = len(s)
    tn = len(t)
    dp = [[0 for _ in range(tn+1)] for _ in range(sn+1)]
    
    for i in range(sn):
        for j in range(tn):
            if s[i] == t[j]: dp[i+1][j+1] = max(dp[i+1][j+1], dp[i][j]+1)
            else: dp[i+1][j+1] = max(dp[i+1][j+1], dp[i+1][j], dp[i][j+1])

    return dp

s1 = 'axyb'
t1 = 'aayxb'

s2 = 'abracadabra'
t2 = 'avadakedavra'

[print(val) for val in lcs(s1, t1)]
[print(val) for val in lcs(s2, t2)]