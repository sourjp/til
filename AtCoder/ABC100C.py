num = int(input())
flag_list = [int(i) for i in input().split()]

ans = 0

for val in flag_list:
    while val % 2 == 0:
        val //= 2
        ans += 1

print(ans)