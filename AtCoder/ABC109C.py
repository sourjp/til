import fractions

def lcm(a,b):
    return fractions.gcd(a,b)

N, X = map(int, input().split())
map_list = [int(i) for i in input().split()]

map_len = []
for i in range(N):
    map_len.append(abs(X - map_list[i]))

ans = map_len[0]
for i in range(1, len(map_len)):
    ans = fractions.gcd(ans, map_len[i])
    i += 1

print(ans)