N = int(input())
A = list(map(int, input().split()))

hs = {}
found = False
for i in range(N):
    if A[i] in hs: 
        found = True
        break
    else: hs[A[i]] = True

print('NO' if found else 'YES')