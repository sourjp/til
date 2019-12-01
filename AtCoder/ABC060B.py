A, B, C = map(int, input().split())

def Choose(A, B, C):
    if A == 1:
        return 'YES'
    for i in range(B):
        if C == (A * i) % B:
            return 'YES'
    return 'NO'

print(Choose(A, B, C))
