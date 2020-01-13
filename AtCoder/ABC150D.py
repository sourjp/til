import fractions
import functools

def lcm_base(x, y):
    return (x * y) // fractions.gcd(x, y)

def lcm(*numbers):
    return functools.reduce(lcm_base, numbers, 1)


n, m = map(int, input().split())
aset = set(map(int, input().split()))
aset = list(x // 2 for x in aset)

llcm = lcm(*aset)

for a in aset:
    if (llcm // a) % 2 == 0:
        ans = 0
        break
else:
    ans = (m // llcm + 1) // 2

print(ans)

'''
import fractions
import functools

def lcm_base(x, y):
    return (x * y) // fractions.gcd(x, y)

def lcm(*numbers):
    return functools.reduce(lcm_base, numbers, 1)


n, m = map(int, input().split())
aset = set(map(int, input().split()))
amax = max(aset)


llcm = lcm(*aset)
minllcm = llcm // 2


divide = m // minllcm
if divide % 2 == 0:
    print(divide // 2)
else:
    print(divide // 2 + 1)
'''