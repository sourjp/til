n, m = map(int, input().split())
queue = []
for i in range(m):
    c, y= map(int, input().split())
    queue.append([c, y, i])

queue = sorted(queue)

index = 0
keep = queue[0][0]
for i in range(m):
    if keep != queue[i][0]:
        index = 0
        keep = queue[i][0]
    index += 1
    queue[i][0] = str(queue[i][0]).zfill(6)
    queue[i][1] = str(index).zfill(6)

queue.sort(key=lambda x: x[2])

for data in queue:
    cn, yn, i = data
    print(cn + yn)

'''
n, m = map(int, input().split())
queue = []
sort_list = [[10**10] for i in range(n)]
for i in range(m):
    c, y = map(int, input().split())
    queue.append([c, y])
    sort_list[c - 1].append(y)

for i in range(n):
    sort_list[i].sort()

print(queue)
print(sort_list)

for data in queue:
    c, y = map(int, data)   
    cy_index = sort_list[c - 1].index(y)
    print(str(c).zfill(6) + str(cy_index + 1).zfill(6))

'''