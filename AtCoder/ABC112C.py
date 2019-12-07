n = int(input())
map_list = []
for _ in range(n):
    map_list.append(input().split())

def function():
    for i in range(101):
        if int(map_list[i][2]) > 0:
            x = int(map_list[i][0])
            y = int(map_list[i][1])
            h = int(map_list[i][2])
            break
        else:
            continue

    for i in range(101):
        for j in range(101):
            cont_check = True
            H = abs(x - i) + abs(y - j) + h
            
            for data in map_list:
                xx, yy, hh = map(int, data)
                if hh != max(H - abs(xx - i) - abs(yy - j), 0):
                    cont_check = False
                    break
            if cont_check:
                return i, j, H

i, j, H = function()
print(i, j, H)