n = int(input())
id_list = map(int, input().split())

memo = [0 for _ in range(n+1)]

for index, i in enumerate(id_list, 1):
    memo[i] = index

del memo[0]
print(*memo)