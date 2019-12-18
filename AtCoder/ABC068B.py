n = int(input())
for i in range(7):
    if 2 ** i <= n:
        ans = 2 ** i
print(ans)