import itertools

n, a, b = map(int, input().split())
mod = 10 **9 + 7


def ncr(n, r, mod):
    x = 1
    y = 1
    for i in range(1, r+1):
        x = x * (n-i+1) % mod
        y = y * i % mod
    return (x*pow(y, mod-2, mod)) % mod

sumc = pow(2, n, mod)-1
ac = ncr(n, a, mod)
bc = ncr(n, b, mod)

print((sumc - ac - bc)% mod)
