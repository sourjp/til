num = int(input())
val_list = [int(i) for i in input().split()]

ans = 0

for val in val_list:
    ans += (val -1)

print(ans)