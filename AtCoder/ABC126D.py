import sys
sys.setrecursionlimit(10**7)

n = int(input())
tree = [[] for _ in range(n)]
for _ in range(n-1):
    u, v, w = map(int, input().split())
    u -= 1
    v -= 1
    tree[u].append((v, w))
    tree[v].append((u, w))

ans = [0 for _ in range(n)]

def journey(u, p, bit):
    ans[u] = bit
    for v, w in tree[u]:
        if v == p: continue
        if w % 2 == 0: journey(v, u, bit)
        else: journey(v, u, 1-bit)
    
journey(0, -1, 0)
[print(x) for x in ans]

'''

n = int(input())
tree = [[] for _ in range(n)]
for _ in range(n-1):
    u, v, w = map(int, input().split())
    tree[u-1].append((v-1, w))
    tree[v-1].append((u-1, w))

visited = [False for _ in range(n)]
visited[0] = True
ans = [0 for _ in range(n)]

def journey(next, bit):
    for pos in next:
        v, w = pos
        if visited[v]: continue
        visited[v] = True
        #print(pos, bit, bit+w)
        if (bit+w) % 2 == 0: ans[v] = 0
        else: ans[v] = 1
            
        journey(tree[v], bit+w)
    
journey(tree[0], 0)
[print(x) for x in ans]
'''