import sys
sys.setrecursionlimit(10**9)

n, m = map(int, input().split())
graph = [[] for _ in range(n)]
dp = [-1 for _ in range(n)]

for _ in range(m):
    x, y = map(int, input().split())
    graph[x-1].append(y-1)


def dfs(s):
    # スタートした一から最下層までの最大値は一意に決定するためメモ化して読み込む
    if dp[s] != -1:
        return dp[s]
    
    rep = 0
    for g in graph[s]:
        # graph[s]がlistだった時、どの階層が一番最大なのかを調べるためにmaxを使う
        rep = max(rep, dfs(g)+1)
    dp[s] = rep
    return rep

def dfs2(s):
    rep = 0
    for g in graph[s]:
        rep = max(rep, dfs2(g)+1)
    return rep

ans = 0
for i in range(n):
    ans = max(ans, dfs(i))

print(ans)