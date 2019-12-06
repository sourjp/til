datas, goal = map(int, input().split())
val_list = []

for i in range(1, datas + 1):
    k, v = map(int, input().split())
    val_list.append([i * 100, k, v])

c = float('inf')

for val in val_list:
    val_goal = goal
    point, num, bonus_point = val
    cc = 0
    for i in range(1, num + 1):
        val_goal -= i * point
        cc += 1
        if val_goal < 0:
            break
    val_goal -= bonus_point
    print(c, cc)
    if val_goal < 0:
        if min(c, cc) == cc:
            c = cc
            mem_index = i - 1
            print(mem_index)
print(c)