from collections import deque
import sys

sys.setrecursionlimit(10**9)

N, M, K = map(int, input().split())
white = [[] for _ in range(N)]
for _ in range(M):
    A, B = map(lambda s: int(s)-1, input().split())
    white[A].append(B)
    white[B].append(A)

black = [[] for _ in range(N)]
for _ in range(K):
    C, D = map(lambda s: int(s)-1, input().split())
    black[C].append(D)
    black[D].append(C)

ans = [False for _ in range(N)]

def freinds(i):
    visited = []

    Q = deque()
    Q.append(white[i])
    while Q:
        for q in Q.popleft():
            if q in visited:
                continue
            else:
                Q.append(white[q])
                visited.append(q)

    cnt = len(visited) - 1
    for v in visited:
        ans[v] = cnt    

for i in range(N):
    if ans[i]: continue
    else:
        # print(i) 
        freinds(i)

#print(ans)

for i in range(N):
    cnt = 0
    for b in black[i]:
        if ans[i] == ans[b]:
            cnt += 1
    black[i] = cnt

for i in range(N):
    ans[i] = ans[i] - len(white[i]) - black[i]

#print(ans, white, black)
print(*ans)

'''
from collections import deque

N, M, K = map(int, input().split())
white = [[] for _ in range(N)]
for _ in range(M):
    A, B = map(lambda s: int(s)-1, input().split())
    white[A].append(B)
    white[B].append(A)

black = [[] for _ in range(N)]
for _ in range(K):
    C, D = map(lambda s: int(s)-1, input().split())
    black[C].append(D)
    black[D].append(C)

#print(white, black)

ans = [0 for _ in range(N)]

def freinds(i):
    visit = [False for _ in range(N)]
    visit[i] = True

    Q = deque()
    Q.append(white[i])
    while Q:
        for q in Q.popleft():
            #print('q', q, i, visit)
            if visit[q]:
                continue
            else:
                Q.append(white[q])
                if q not in white[i] and q not in black[i]:
                    ans[i] += 1
                visit[q] = True
                #print('cnt')

for i in range(N):
    freinds(i)

print(ans)
'''