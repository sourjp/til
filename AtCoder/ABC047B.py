W, H, N = map(int, input().split())

xl, xr = 0, W
yl, yh = 0, H

for i in range(N):
    xi, yi, ai = map(int, input().split())

    if ai == 1:
        xl = max(xi, xl)
    elif ai == 2:
        xr = min(xi, xr)
    elif ai == 3:
        yl = max(yi, yl)
    else:
        yh = min(yi, yh)

if xr - xl > 0 and yh - yl > 0:
    ans = (xr - xl) * (yh - yl)
else:
    ans = 0

print(ans)
