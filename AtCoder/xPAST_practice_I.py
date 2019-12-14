
def counter(arr, i, j):
    l = j - 1
    r = j + 1
    u = i - 1
    d = i + 1
    count = 0

    while l >= 0:
        if arr[i][l] == '#':
            break
        count += 1
        l -= 1

    while r < w:
        if arr[i][r] == '#':
            break
        count += 1
        r += 1

    while u >= 0:
        if arr[u][j] == '#':
            break
        count += 1
        u -= 1        

    while d < h:
        if arr[d][j] == '#':
            break
        count += 1
        d += 1  

    return count + 1

h, w = map(int, input().split())

arr = []
for _ in range(h):
    l = []
    for a in input():
        l.append(a)
    arr.append(l)

ans = 0
i = 0
while i < h:
    j = 0
    while j < w:
        if arr[i][j] == '.':
            val = counter(arr, i, j)
            ans = max(ans, val)
        j += 1
    i += 1
print(ans)
