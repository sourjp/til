n, k = map(int, input().split())
h = list(map(int, input().split()))

h.sort()
if k == 0: print(sum(h))
else: print(sum(h[:-k]))