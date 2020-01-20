n = int(input())
p = list(map(int, input().split()))

cnt = 0
m = float('inf')
for i in range(n):
    if m > p[i]:
        cnt += 1
        m = p[i]

print(cnt)
