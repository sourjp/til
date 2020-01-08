n, k = map(int, input().split())
s = list(input())

cnt = 0

i = 1
while i < len(s):
    if cnt == k:
        break

    if s[i] != s[i-1]:
        cnt += 1
        start = i
        target = s[i]

        while  i < len(s) and target == s[i]:
            if s[i] == 'R': s[i] = 'L'
            else: s[i] = 'R'

            i += 1   

        continue    

    i += 1

ans = 0
for i in range(1, len(s)):
    if s[i] == s[i-1]:
        ans += 1

print(ans)

