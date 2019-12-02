import copy

def DepthFirstSearch(graph, i):
    global linking
    result[i] = 1
    memo.append(i)    
    if memo == [1] * N:
        linking = True
        print('yes')
        return
    for j in range(N):
        # print(i, j)
        if graph[i][j] == 1:
            if j in memo:
                continue
            DepthFirstSearch(graph, j)
            memo.pop()
    if linking:
        return 0
    else:
        return 1

N, M = map(int, input().split())
AB = []
for _ in range(N):
    a, b = input().split()
    AB.append([int(a), int(b)])
 
graph = [[0] * N for _ in range(N)]

for data in AB:
    i, j = data
    graph[i - 1][j - 1] = 1
    graph[j - 1][i - 1] = 1


count = M
for data in AB:
    linking = False
    i = 0
    memo = []
    result = [0 for _ in range(N)]
    tmp = copy.deepcopy(graph)

    x, y = data
    tmp[x - 1][y - 1] = 0
    tmp[y - 1][x - 1] = 0
    print(count)
    count -= DepthFirstSearch(tmp, i)
'''
    print('tmp')
    for _ in range(len(graph)):
        print(tmp[_])
    print('graph')
    for _ in range(len(graph)):
        print(graph[_])
'''

print(count)
