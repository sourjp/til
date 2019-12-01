import fractions

def lcm(a,b):
    return a * b // fractions.gcd(a,b)

N = int(input())
T = []
for _ in range(N):
    T.append(int(input()))

ans = 1
for i in range(N):
    ans = lcm(T[i], ans)

print(ans)  