N, K = map(int, input().split())
ans = []
while N > 0:
    ans.append(N%K)
    N = N // K 
print(len(ans))