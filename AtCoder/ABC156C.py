N = int(input())
X = list(map(int, input().split()))

X.sort()
ans = []
for i in range(X[0], X[-1]+1):
    tmp = 0
    for j in range(N):
        tmp += (abs(X[j]-i))**2
    ans.append(tmp)

print(min(ans))