n = int(input())
divide = 10 ** 9 + 7

a = [format(i, '060b') for i in map(int, input().split())]
ans = []

for i in range(60):
    bit_list = [b[59-i] for b in a]
    val = bit_list.count('0') * bit_list.count('1')
    ans.append((val * 2 ** i))

print(sum(ans)%divide)