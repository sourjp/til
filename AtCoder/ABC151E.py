n, k = map(int, input().split())
alist = sorted(map(int, input().split()))
mod = 10**9 + 7

def comb(n, r, p=mod):
    if (r < 0) or (n < r):
        return 0
    r = min(r, n - r)
    return fact[n] * factinv[r] * factinv[n-r] % p

fact = [1, 1]
factinv = [1, 1]
inv = [0, 1]
p = mod
N = n
for i in range(2, N + 1):
    fact.append((fact[-1] * i) % p)
    inv.append((-inv[p % i] * (p // i)) % p)
    factinv.append((factinv[-1] * inv[-1]) % p)

amax = 0
amin = 0
i = 0
while i <= n-k:
    cnt = comb(n-i-1, k-1)
    amax += (alist[n-i-1] * cnt)%mod
    amin += (alist[i] * cnt)%mod
    i += 1

print((amax - amin) % mod)

'''
import itertools

n, k = map(int, input().split())
alist = sorted(list(map(int, input().split())))
paterns = list(itertools.combinations(alist, k))
divide = 10**9 + 7

ans = 0
for patern in paterns:
    gmax = patern[-1]%divide
    gmin = patern[0]%divide
    ans += (gmax - gmin)%divide


print(ans%divide)

def comb(n, k):
    n1 = n+1
    r = min(k, n-k)
    numer = denom = 1
    i = 1
    while i < r+1:
        numer = numer * (n1-i) % mod
        denom = denom * i % mod
        i += 1
    
    #memo[n][k] = numer * pow(denom, mod - 2, mod) % mod
    #return numer // denom
    return numer * pow(denom, mod - 2, mod) % mod

'''