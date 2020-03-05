N, M = map(int, input().split())
SC = [[] for _ in range(N)]

error = False
for _ in range(M):
    s, c = map(int, input().split())
    s -= 1
    if SC[s] and SC[s] != c:
        error = True
        break
    else:
        SC[s] = c

if error:
    print(-1)
elif SC[0] == 0 and len(SC) > 1:
    print(-1)
else:
    if not SC[0] and len(SC) == 1:
        SC[0] = 0
    if not SC[0] and len(SC) > 1:
        SC[0] = 1
    if len(SC) > 1 and not SC[1]:
        SC[1] = 0
    if len(SC) > 2 and not SC[2]:
        SC[2] = 0
    print(''.join(map(str,SC)))
