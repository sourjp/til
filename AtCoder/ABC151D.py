import collections

h, w = map(int, input().split())

m = []
for _ in range(h):
    m.append(list(input()))


ans = 0
for i in range(h):
    for j in range(w):
        if m[i][j] == '#':
            continue

        checked = [[False]*w for _ in range(h)]
        q = collections.deque()
        q.append((i, j, 0))
        checked[i][j] = True
        while True:
            x, y, s = q.popleft()
            #print(q)

            if x > 0 and m[x-1][y] != '#' and checked[x-1][y] == False:
                q.append((x-1, y, s+1))
                checked[x-1][y] = True

            if x+1 < h and m[x+1][y] != '#' and checked[x+1][y] == False:
                q.append((x+1, y, s+1))
                checked[x+1][y] = True

            if y > 0 and m[x][y-1] != '#' and checked[x][y-1] == False:
                q.append((x, y-1, s+1))
                checked[x][y-1] = True

            if y+1 < w and m[x][y+1] != '#' and checked[x][y+1] == False:
                q.append((x, y+1, s+1))
                checked[x][y+1] = True

            ans = max(ans, s)

            if len(q) == 0:
                break

print(ans)
