n, m = map(int, input().split())
queue = []
for i in range(m):
    a, b = input().split()
    queue.append([a, b])

sort_list = [[10**10] for i in range(n)]
for data in queue:
    k, v = map(int, data)
    sort_list[k - 1].append(v)

for i in range(n):
    sort_list[i].sort()

for data in queue:
    k, v = map(int, data)   

    num_index = sort_list[k -1].index(v)

    print(str(k).zfill(6) + str(num_index + 1).zfill(6))
