def even_case(input_list) -> int:
    input_list.sort()

    if input_list[0] == 0: return 0


    for i in range(1, len(input_list), 2):
        if input_list[i] % 2 == 0 or input_list[i] != input_list[i-1]:
            return 0

    ans = 2 ** (n//2)

    return ans


def odd_case(input_list) -> int:
    input_list.sort()

    if input_list[0] != 0: return 0

    if len(input_list) == 1: return 1

    if input_list[1] == 0: return 0

    for i in range(2, len(input_list), 2):
        if input_list[i] % 2 == 1 or input_list[i] != input_list[i-1]:
            return 0

    ans = 2 ** ((n-1) // 2)

    return ans

n = int(input())
input_list = list(map(int, input().split()))
math = 10 ** 9 + 7

if n % 2 == 0:
    result = even_case(input_list)
else:
    result = odd_case(input_list)

print(result % math)