import heapq

n, d, a = map(int, input().split())
bom = []

for _ in range(n):
    x, h = map(int, input().split())
    bom.append([x, h])

bom.sort(key=lambda x:x[0])

ans = 0
tot = 0
q = []
for x, h in bom:
    while q:
        if q[0][0] >= x: break
        else:
            _, t = heapq.heappop(q)
            tot -= t
    
    r = max((h-tot-1)//a + 1, 0)
    ans += r
    tot += r * a
    heapq.heappush(q, (x+2*d, r*a))

print(ans)

