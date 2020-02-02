import bisect

A, B, Q = map(int, input().split())
s = [-float('inf')] + [int(input()) for _ in range(A)] + [float('inf')]
t = [-float('inf')] + [int(input()) for _ in range(B)] + [float('inf')]
X = [int(input()) for _ in range(Q)]

for x in X:
    sp = bisect.bisect_left(s, x)
    tp = bisect.bisect_left(t, x) 
    res = float('inf')
    for S in [s[sp-1], s[sp]]:
        for T in [t[tp-1], t[tp]]:
            d1, d2 = abs(S-x) + abs(T-S), abs(T-x)+abs(S-T)
            res = min(res, d1, d2)
    print(res)
