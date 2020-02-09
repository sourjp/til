n = int(input())
v = list(map(int, input().split()))
nev = []
ev = []
for i in range(n):
    if i%2 == 0: ev.append(v[i])
    else: nev.append(v[i])

