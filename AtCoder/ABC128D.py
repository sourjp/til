n, k = map(int, input().split())
v = list(map(int, input().split()))

i = 0
ans = 0

for number in range(min(n+1, k+1)):
    for i in range(number+1):
        right = n - number - i
        vv = v[:i] + v[right:]

        vv.sort()
    
        tmp_ans = sum(vv)
        qb = min(k - number, len(vv))
        for j in range(qb):
            if vv[j] < 0:
                tmp_ans -= vv[j]
            else:
                break

        ans = max(ans, tmp_ans)

print(ans)

