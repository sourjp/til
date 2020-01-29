x, y, z, k = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
C = list(map(int, input().split()))
result = []

for c in range(z):
    for b in range(y):
        for a in range(x):
            result.append(A[a] + B[b] + C[c])

result.sort()
[print(val) for val in result[-k:][::-1]]