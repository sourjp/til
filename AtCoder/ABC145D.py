
def comb(n, r, mod=10 ** 9 + 7):
    n1 = n + 1
    r = min(n, n - r)
    numer = denom = 1
    for i in range(1, r + 1):
        numer = numer * (n1 - i) % mod
        denom = denom * i % mod
    return numer * pow(denom, mod - 2, mod) % mod

x, y = map(int, input().split())

if (x+y) % 3 != 0:
    print(0)
    exit()

n = (2*y-x) // 3
m = (2*x-y) // 3

if n*m < 0:
    print(0)
    exit()

print(comb(n+m, m))