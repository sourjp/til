N, M = map(int, input().split())

A = []
B = []
for _ in range(N):
    A.append(input())
for _ in range(M):
    B.append(input())

def CheckExist(ai, aj):
    for bi in range(M):
        for bj in range(M):
            if A[ai+bi][aj+bj] != B[bi][bj]:
                return False
    return True

for ai in range(N - M + 1):
    for aj in range(N - M + 1):
        if CheckExist(ai, aj):
            print('Yes')
            exit(0)
print('No')