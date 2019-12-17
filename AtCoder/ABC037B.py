n, q = map(int, input().split())
base_list = [0 for _ in range(n)]

for i in range(q):
    l, r, t = map(int, input().split())
    for i in range(l-1, r):base_list[i] = t

print(*base_list, sep='\n')
