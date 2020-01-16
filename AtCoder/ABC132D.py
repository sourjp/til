n, k = map(int, input().split())
mod = 10**9 + 7

def comb(n, k):
    return fact[n] // (fact[k] * fact[n-k])

i = 1
fact = [1]
while i < n+1:
    fact.append(i * fact[-1])
    i += 1

j = 1
while j < k+1:
    print((comb(n-k+1, j) * comb(k-1, j-1)) % mod)
    j += 1
