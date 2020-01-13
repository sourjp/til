n, m = map(int, input().split())

dp = [0 for _ in range(n+1)]

def ans(dp, n, m) -> list:
    if m == 0:
        return [0, 0]

    ac = 0
    wa = 0
    i = 0
    while i < m:
        q, r = input().split()
        q = int(q)

        if dp[q] == None:
            pass
        elif r == 'WA':
            dp[q] += 1
        elif r == 'AC':
            ac += 1
            wa += dp[q]
            dp[q] = None

        i += 1

    return [ac, wa]

a = ans(dp, n, m)

print(*a)