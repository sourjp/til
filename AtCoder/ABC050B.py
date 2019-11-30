N = int(input())
T = [int(i) for i in input().split()]
M = int(input())

cnt = 0
while cnt < M:
    P, X = map(int, input().split())

    ans = 0
    P -= 1
    for i in range(len(T)):
        if i == P: 
            ans += X
        else:
            ans += T[i]
    print(ans)
    cnt += 1