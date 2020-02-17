N, K = map(int, input().split())
A = list(map(int, input().split()))

minl = []
zl = []
maxl = []

for val in range(A):
    if val == 0: zl.append(val)
    if val < 0: minl.append(val)
    if val > 0: maxl.append(val)


minn
zn
maxn

a = []
if K <= minn:
    cnt = K
    for v1 in minl:
        for v2 in maxl:
            a.append(v1*v2)    
    ans = a[cnt]

elif minn+1 < K <= zn+minn:
    pass



else:
    pass

print(ans)