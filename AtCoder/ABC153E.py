def calc_m_value(M, A, B, N, h):
    return min([M[h - A[i]]+B[i] if A[i] <= h else B[i] for i in range(N)])

H, N = map(int, input().split())
A = []
B = []
for i in range(N):
    a, b = map(int, input().split())
    A.append(a)
    B.append(b)

M = [0] * (H+1)
for i in range(1, H+1):
    M[i] = calc_m_value(M, A, B, N, i)

print(M[H])
