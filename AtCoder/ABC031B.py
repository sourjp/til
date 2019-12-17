l, h = map(int, input().split())
n = int(input())
for i in range(n):
    p = int(input())
    if p >= l and p <= h:
        print(0)
    elif p < l:
        print(l-p)
    else:
        print(-1)