import heapq

n, m = map(int, input().split())
points = [tuple(map(int, input().split())) for _ in range(n)]
points.sort()

ans = 0
i = 0
days = 0
heap = []
while days <= m:
    while i < len(points) and points[i][0] <= days:
        d, p = points[i]
        heapq.heappush(heap, -p)
        i += 1

    days += 1
    if heap: ans += heapq.heappop(heap)

print(-ans)