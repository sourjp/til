num, res = map(int, input().split())
check_list = [int(i) for i in input().split()]

cnt = 0
i = 0
j = 0
math = check_list[0]
check_list.append(0)
while i < num:
    if math >= res:
        cnt += num - i
        math -= check_list[j]
        j += 1
    else:
        i += 1
        math += check_list[i]

print(cnt)