n, k = map(int, input().split())
s = input()

ans = 0
cnt = 0
l = 0
r = 0

if s[r] == '0':
    cnt = 1
    while r < n:
        if s[r] == '0' and cnt == 1:
            save = r

        if s[r] == '0' and cnt == k:
            ans = max(ans, r-l+1)
            cnt = 1
            l = save

        if s[r] == '1' and s[r-1] == '0':
            cnt += 1

        r += 1

else:
    while r < n:
        print(ans, r, l)
        if s[r] == '1' and cnt == 1:
            save = r

        if s[r] == '1' and cnt == k:
            ans = max(ans, r-l+1)
            print(ans, r, l)

            cnt = 0
            l = save

        if s[r] == '0' and s[r-1] == '1':
            cnt += 1

        r += 1

print(ans)