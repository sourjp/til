N = int(input())
H = []
S = []
right = 0
for _ in range(N):
    h, s = map(int, input().split())
    H.append(h)
    S.append(s)
    right = max(right, h+s*(N-1))

left = max(H)-1

def check(mid):
    tmp = []
    for i in range(N):
        tmp.append((mid-H[i]) // S[i])
    tmp.sort()

    print('t:', tmp)
    
    for i in range(N):
        if tmp[i] < i:
            return False
    return True


while right - left > 1:
    mid = (left+right) // 2

    print('lmr:', left, mid, right)

    if check(mid):
        right = mid
        print('right')
    else:
        left = mid
        print('left')

print(right)
