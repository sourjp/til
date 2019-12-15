import fractions
def gcdcheck(a, b):
    return fractions.gcd(a, b)

n = int(input())
monster_list = [int(i) for i in input().split()]

ans = monster_list[0]
for i in range(1, n):
    ans = gcdcheck(ans, monster_list[i])

print(ans)