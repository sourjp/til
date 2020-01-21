n, k = map(int, input().split())
s = [int(input()) for _ in range(n)]

l = 0
r = 0
cnt = 1
ans = 0
while r < n:
    cnt *= s[r]
    if cnt == 0:
        ans = n
        break
    if cnt > k:
        cnt /= s[l]
        if l == r:
            r += 1
            l += 1
            continue
        l += 1
    else:
        ans = max(ans, r-l+1)
    r += 1

print(ans)
     