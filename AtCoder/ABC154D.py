N, K = map(int, input().split())
P = list(map(int, input().split()))
e = []

def expect(x):
    return ((x*(x+1))//2) / x

for p in P:
    e.append(expect(p))

ans = sum(e[:K])
tmp = ans
#print(e, e[:K])
for i in range(K, N):
    tmp = tmp - e[i-K] + e[i]
    ans = max(ans, tmp)
    #print(tmp, ans, e[i-K], e[i])

print(ans)