n = int(input())
a = list(map(int, input().split()))
b = [0 for _ in range(n)]

ans = []

i = 0
while i < n:
    j = k = n - i
    add = j
    times = n - i
    cnt = 0

    if j == 1:
        cnt = sum(b)
    else:
        while j <= n:
            cnt += b[j-1]
            j += add

    #print(k, a, cnt, b)
    if cnt % 2 != a[k-1]:
        b[k-1] = 1
        ans.append(k)
    else:
        b[k-1] = 0

    i += 1

print(len(ans))
if len(ans) > 0: print(*ans[::-1])
