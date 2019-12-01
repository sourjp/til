'''
- INPUT:
10

- OUTPUT:
Normal: 89
[1, 1, 2, 0, 0, 0, 0, 0, 0, 0, 0]
[1, 1, 2, 3, 0, 0, 0, 0, 0, 0, 0]
[1, 1, 2, 3, 5, 0, 0, 0, 0, 0, 0]
[1, 1, 2, 3, 5, 8, 0, 0, 0, 0, 0]
[1, 1, 2, 3, 5, 8, 13, 0, 0, 0, 0]
[1, 1, 2, 3, 5, 8, 13, 21, 0, 0, 0]
[1, 1, 2, 3, 5, 8, 13, 21, 34, 0, 0]
[1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 0]
[1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
Dynamic: 89
[1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
[1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
[1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
[1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
[1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
[1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
[1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
[1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
[1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
Reverse: 89
'''

n = 10

def FibonacciNormal(n):
    if n == 0 or n == 1:
        return 1
    return FibonacciNormal(n-1) + FibonacciNormal(n-2)


F = [0 for _ in range(n+1)]
def FibonacciDynamic(n):
    if n == 0 or n == 1:
        F[n] = 1
        return F[n]
    if F[n] != 0:
        return F[n]
    F[n] = FibonacciDynamic(n-1) + FibonacciDynamic(n-2)
    print(F)
    return F[n]


FF = [0 for _ in range(n+1)]
def FibonacciReverse(n):
    FF[0] = 1
    FF[1] = 1
    for i in range(2,n+1):
        print(F)
        FF[i] = FF[i-1] + FF[i-2]
    return FF[n]

print('Normal:', FibonacciNormal(n))
print('Dynamic:', FibonacciDynamic(n))
print('Reverse:', FibonacciReverse(n))