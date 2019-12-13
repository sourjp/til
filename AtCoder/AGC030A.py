a, b, c = map(int, input().split())

cnt = 0
if a + b + 1>= c:
    ans = b + c
else:
    ans = b + a + b + 1

print(ans)