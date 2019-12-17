n, m, c = map(int, input().split())

base_list = list(map(int, input().split()))

ans = 0
for i in range(n):
    cal = 0
    source_list = list(map(int, input().split()))

    for j in range(m):
        cal += base_list[j] * source_list[j]

    if cal + c > 0:
        ans += 1

print(ans)