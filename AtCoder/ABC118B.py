n, m = map(int, input().split())
table = [0] * (m+1)

for i in range(n):
    k, *args = map(int, input().split())
    for j in args:
        table[j] += 1

cnt = 0
for t in table:
    if t == n:
        cnt += 1

print(cnt)