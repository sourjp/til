n, a, b = map(int, input().split())

ans = 0
cnt = 0
for i in range(a, n+1):
    res = 0
    num = i
    while num > 0:
        res += num % 10
        num //= 10

    if res >= a and res <= b:
        ans += i

print(ans)