n, l = map(int, input().split())

cost = 1001
for i in range(n):
    c, t = map(int, input().split())
    if t <= l:
        cost = min(cost, c)

print(cost if cost != 1001 else 'TLE')