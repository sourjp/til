h, w = map(int, input().split())
rule = []
for _ in range(h):
    rule.append(list(input()))
mod = 10**9 + 7

graph = [[0 for _ in range(w)] for _ in range(h)]
graph[0][0] = 1

for i in range(h):
    for j in range(w):
        if j+1 < w and rule[i][j+1] == '.':
            graph[i][j+1] = (graph[i][j+1] + graph[i][j]) % mod
        if i+1 < h and rule[i+1][j] == '.':
            graph[i+1][j] = (graph[i+1][j] + graph[i][j]) % mod

#print(graph)
print(graph[-1][-1])