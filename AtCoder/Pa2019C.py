n, m = map(int, input().split())
A = []
for _ in range(n):
    A.append(list(map(int, input().split())))

R = []
for i in range(m):
    for j in range(i+1, m):
        cnt = 0
        for k in range(n):
            cnt += max(A[k][i], A[k][j])
        R.append(cnt)

print(max(R))

