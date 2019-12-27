'''
n, m = map(int, input().split())
start_list = []
end_list = []

for _ in range(m):
    s, e = map(int, input().split())

    if s == 1:
        start_list.append(e)
    elif e == n:
        end_list.append(s)

possible = False
for i in end_list:
    if i in start_list:
        possible = True
        break        

print('POSSIBLE' if possible else 'IMPOSSIBLE')

'''

n, m = map(int, input().split())
memo = [False] * n

possible = False
for _ in range(m):
    s, e = map(int, input().split())

    if s == 1:
        if memo[e]:
            possible = True
            break

        memo[e] = True

    elif e == n:
        if memo[s]:
            possible = True
            break

        memo[s] = True

print('POSSIBLE' if possible else 'IMPOSSIBLE')

