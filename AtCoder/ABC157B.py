A = []
for _ in range(3):
    A.append(list(map(int, input().split())))

N = int(input())

C = [[False for _ in range(3)] for _ in range(3)]
for i in range(N):
    B = int(input())
    for j in range(3):
        if B in A[j]:
            bi = A[j].index(B)
            C[j][bi] = True

ans = 'No'

# TATE
for i in range(3):
    if C[0][i] + C[1][i] + C[2][i] == 3:
        ans = 'Yes'

# YOKO
for i in range(3):
    if C[i][0] + C[i][1] + C[i][2] == 3:
        ans = 'Yes'

# NANAME
if C[0][0] + C[1][1] + C[2][2] == 3:
    ans = 'Yes'

if C[0][2] + C[1][1] + C[2][0] == 3:
    ans = 'Yes'

print(ans)