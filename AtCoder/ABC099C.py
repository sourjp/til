
args = int(input())

ans = float('inf')
for i in range(args):
    count = 0

    args_six = i
    while args_six >= 6:
        args_six //= 6
        count += 1
    count += args_six

    args_nine = args - i
    while args_nine >= 9:
        args_nine //= 9
        count += 1
    count += args_nine

    ans = min(ans, count)

print(ans)