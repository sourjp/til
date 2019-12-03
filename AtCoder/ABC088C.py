grid = []
for i in range(3):
    grid.append([int(i) for i in input().split()])

for _ in range(100):
    a1 = i
    b1 = grid[0][0] - a1
    b2 = grid[0][1] - a1
    b3 = grid[0][2] - a1
    if  grid[1][0] - b1 == grid[1][1] - b2 == grid[1][2] - b3 and grid[2][0] - b1 == grid[2][1] - b2 == grid[2][2] - b3:
        print('Yes')
        exit()
print('No')
