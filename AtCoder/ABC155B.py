n = int(input())
A = list(map(int, input().split()))

def func(A):
    for a in A:
        #print(a)
        if a % 2 != 0: continue
        if a % 3 == 0 or a % 5 == 0: continue
        return 'DENIED'
    return 'APPROVED'

print(func(A))