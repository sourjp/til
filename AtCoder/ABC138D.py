n, q = map(int, input().split())
tree = [[] for _ in range(n)]
for _ in range(n-1):
    a, b = map(int, input().split())
    tree[a-1].append(b-1)
    tree[b-1].append(a-1)

cost = [0 for _ in range(n)]
for _ in range(q):
    pos, point = map(int, input().split())
    cost[pos-1] += point

memo = set([0])
stack = [0]

while len(stack) > 0:
    cur_node = stack.pop()
    cur_cost = cost[cur_node]

    for node in tree[cur_node]:
        if node not in memo:
            memo.add(node)
            cost[node] += cur_cost
            stack.append(node)

print(*cost)

'''
n, q = map(int, input().split())

tree = [0 for _ in range(n)]
for _ in range(n-1):
    a, b = map(int, input().split())
    tree[b-1] = a-1

cost = [0 for _ in range(n)]
for _ in range(q):
    pos, point = map(int, input().split())
    cost[pos-1] += point

for i in range(1, n):
    cost[i] += cost[tree[i]]    

print(*cost)
'''
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