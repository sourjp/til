N = int(input())
A = []
B = []
for _ in range(N):
    a, b = map(int, input().split())
    A.append(a)
    B.append(b)

def math_range(start, end, a, b):
    return abs(start-a) + abs(a-b) + abs(end-b)

start_border = (max(A) + min(A)) // 2
end_border = (max(B) + min(B)) // 2

ans = []
for i in range(N):
    for j in range(N):
        start = A[i]
        end = B[j]
        #if start > start_border or end < end_border: continue

        distance = 0
        for k in range(N):
            distance += math_range(start, end, A[k], B[k])
        ans.append(distance)

#print(ans)
print(min(ans))
