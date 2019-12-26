n, m = map(int, input().split())
start_list = []
end_list = []

for _ in range(m):
    s, e = map(int, input().split())

    if s == 1:
        start_list.append(e)
    if e == n:
        end_list.append(s)

possible = False
for i in end_list:
    if i in start_list:
        possible = True
        break        

print('POSSIBLE' if possible else 'IMPOSSIBLE')