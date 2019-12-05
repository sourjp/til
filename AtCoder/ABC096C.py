h, w = map(int, input().split())

grid = []
grid.append(['.'] * (w + 2))
for _ in range(h):
    word = '.' + input() + '.'
    grid.append([i for i in word])
grid.append(['.'] * (w + 2))

for i in range(1, h):
    for j in range(1, w):
        if grid[i][j] == '#':
            if grid[i][j-1] == '#' or grid[i-1][j] == '#' or grid[i][j+1] == '#' or grid[i+1][j] == '#':
                pass
            else:
                print('No')
                exit()

print('Yes')