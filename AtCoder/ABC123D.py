x, y, z, k = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
C = list(map(int, input().split()))

def func1():
    E = [a+b for a in A for b in B]
    E.sort()
    if len(E) > k: E = E[-k:]
    F = [c+e for c in C for e in E]
    F.sort()
    return F[-k:][::-1]

[print(val) for val in func1()]
