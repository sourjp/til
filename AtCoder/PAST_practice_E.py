pre_num, city_num = map(int, input().split())

pre_list = [[ ] for _ in range(pre_num)]
for index, i in enumerate(range(city_num)):
    pre, year = map(int, input().split())
    pre_list[pre - 1].append([pre, year, index])

ll = [int(0) for _ in range(city_num)]
for pre in pre_list:
    pre.sort()
    j = 1
    for data in pre:
        c, y, i = data
        cc = str(c).zfill(6)
        jj = str(j).zfill(6)
        j += 1
        ll[i] = (cc + jj)

for ans in ll:
    print(ans)
