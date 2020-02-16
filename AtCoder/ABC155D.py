N, K = map(int, input().split())
A = list(map(int, input().split()))

border = 0
A.sort()
alist = []
for i in range(N):
    for j in range(i+1, N):
        val = A[i]*A[j]
        if len(A) > K and val > border and A[j] > 0: break
        alist.append(val)
        border = max(val, border)

alist.sort()
#print(alist)
print(alist[K-1])
