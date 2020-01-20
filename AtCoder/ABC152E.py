import fractions

n = int(input())
a = list(map(int, input().split()))
mod = 10 ** 9 + 7

aset = set(a)

def lcm(x, y):
    return (x * y) // fractions.gcd(x, y)

if n == 1:
    print(1)

elif 1 < n:
    g = lcm(a[0], a[1])

    if n != 2:
        for val in aset:
            g = lcm(g, val)

    ans = 0
    for val in a:
        ans += g//val

    print(ans % mod)