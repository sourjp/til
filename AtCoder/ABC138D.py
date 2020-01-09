import collections

def dfs(queue, ans):
    foot_print = [False for _ in range(n)]
    for val in tree[0]:
        queue.append(val)
    ans[0] = counter[0]
    foot_print[0] = True

    while queue:
        node = queue.popleft()
        if foot_print[node] == True:
            continue

        else:
            for val in tree[node]:
                queue.append(val)
            ans[node] = counter[node] + ans[node-1]
            foot_print[node] == True


n, q = map(int, input().split())

tree = [[] for _ in range(n)]
ans = [0 for _ in range(n)]

for _ in range(n-1):
    a, b = map(int, input().split())
    tree[a-1].append(b-1)

counter = [0 for _ in range(n)]
for _ in range(q):
    p, x = map(int, input().split())
    counter[p-1] += x
    queue = collections.deque()

    dfs(queue, ans)

print(*ans)

'''
import collections

def add(queue, ans, start_node, value):
    ans[start_node] += value
    for val in tree[start_node]:
        queue.append(val)
    while queue:
        node = queue.popleft()
        ans[node] += value
        if not node:
            continue

        if tree[node] != []:
            for val in tree[node]:
                queue.append(val)


n, q = map(int, input().split())

tree = [[] for _ in range(n)]
ans = [0 for _ in range(n)]

for _ in range(n-1):
    a, b = map(int, input().split())
    tree[a-1].append(b-1)

for _ in range(q):
    p, x = map(int, input().split())
    queue = collections.deque()

    add(queue, ans, p-1, x)

print(*ans)

'''