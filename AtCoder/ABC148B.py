n = int(input())
s, t = map(str, input().split())

ans = ''
for ss, tt in zip(s, t):
    ans += ss+tt

print(ans)