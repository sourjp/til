AN = int(input())
A = [tuple(map(int, input().split())) for _ in range(AN)]
BN = int(input())
B = [tuple(map(int, input().split())) for _ in range(BN)]

def checkstart(x, y):
    cnt = 0
    for a in A:
        ax, ay = a
        if (ax+x, ay+y) in B: cnt += 1
    return cnt


ax, ay = A[0]
for b in B:
    bx, by = b
    dx, dy = bx-ax, by-ay
    if AN == checkstart(dx, dy): break

print(dx, dy)