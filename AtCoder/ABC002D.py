n, m = map(int, input().split())

def func(n, m):
    if m == 0: return 1

    hash = [[] for _ in range(n)]
    for _ in range(m):
        x, y = map(int, input().split())
        hash[x-1].append(y-1)
        hash[y-1].append(x-1)

    return hash

ans = 0
for i in range(2**N):
    state = set(j for j in range(N) if 1 & (i >> j))
 
    # その派閥が作れる -> True
    flag = True
    for j in range(N):
        # 派閥リストにない議員
        if j not in state:
            continue
        # True
        elif state - BP[j] == {j}:
            continue
        # False
        else:
            flag = False
    
    if flag:
        ans = max(ans, len(state))
 
print(ans)