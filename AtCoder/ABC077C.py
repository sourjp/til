import bisect

N = int(input())
A = sorted(list(map(int, input().split()))) 
B = sorted(list(map(int, input().split())))
C = sorted(list(map(int, input().split())))

#print(A)
#print(B)
#print(C)

a = [0]
b = [0]
for i in range(N):
    ai = bisect.bisect_right(B, A[i])
    a.append(N-ai+a[i])

    bi = bisect.bisect_right(C, B[i])
    b.append(N-bi+b[i])

#print(a)
#print(b)

ans = 0
for i in range(1, N+1):
    #print(b[-1] - b[-(a[i]-a[i-1])])
    ans += b[-1] - b[-(a[i]-a[i-1])-1]

print(ans)
