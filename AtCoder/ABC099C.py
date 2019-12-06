
args = int(input())

ans = float('inf')
for i in range(args+1):
    count = 0

    args_six = i
    while args_six >= 6:
        count += args_six % 6
        args_six //= 6
    count += args_six

    args_nine = args - i
    while args_nine >= 9:
        count += args_nine % 9
        args_nine //= 9
    count += args_nine
    print(ans, count)
    ans = min(ans, count)

print(ans)