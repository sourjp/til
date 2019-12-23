d, g = map(int, input().split())
point_list = []
expection_list = []
for i in range(1, d+1):
    p, c = map(int, input().split())
    expection_list.append((p*i*100 + c) / p)
    point_list.append([p, c, p*i*100+c])

print(expection_list)
print(point_list)

best_q = float('inf')
for i in range(d):
    if g < point_list[i][2]:
        tmp = point_list[i][2]
        if tmp < best_q:
            index = i
            best_q = tmp
