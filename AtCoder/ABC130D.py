n, k = map(int, input().split())
a = list(map(int, input().split()))

li = 0
ri = 0
cnt = 0
ans = 0

while ri < n:
    #print(li, ri, ans)
    cnt += a[ri]
    while li <= ri and cnt >= k:
        #print(li, ri, ans)

        ans += n-ri
        cnt -= a[li]
        li += 1

    ri += 1

print(ans)
