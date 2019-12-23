def dfs(graph, visited, edge):
    visited[edge] = True

    for i in range(n):
        if graph[edge][i] == 1 and visited[i] == False:
            dfs(graph, visited, i)

    if sum(visited) == n: return True
    else: return False


n, m = map(int, input().split())
input_list = []
for i in range(m):
    input_list.append(list(map(int, input().split())))
    
cnt = 0
for skip in range(m):
    graph = [[0]*n for _ in range(n)]

    for stage in range(m):
        if stage == skip:
            continue

        i, j = input_list[stage]
        graph[i-1][j-1] = 1
        graph[j-1][i-1] = 1

    visited = [False for _ in range(n)]

    cnt += dfs(graph, visited, 0)        

print(m - cnt)