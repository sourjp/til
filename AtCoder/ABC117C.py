def func(input_list):
    if n >= m:
        return 0

    input_list.sort()

    input_diff = []
    for i in range(m-1):
        diff = input_list[i+1] - input_list[i]
        input_diff.append(abs(diff))

    choice_pivot = [0]
    for i in range(n-1):
        pivot = max(input_diff)
        index = input_diff.index(pivot)
        input_diff[index] = 0
        choice_pivot.append(index+1)

    ans = 0
    choice_pivot.append(m)
    for i in range(len(choice_pivot)-1):
        start = choice_pivot[i]
        end = choice_pivot[i+1] - 1
        ans += input_list[end] - input_list[start]

    return ans

def func2(input_list):
    if n >= m:
        return 0

    input_list.sort()

    input_diff = []
    for i in range(m-1):
        diff = input_list[i+1] - input_list[i]
        input_diff.append(abs(diff))

    input_diff.sort(reverse=True)
    ans = input_list[-1] - input_list[0]
    for i in range(0, n-1):
        ans -= input_diff[i]

    return ans

n, m = map(int, input().split())
input_list = [int(i) for i in input().split()]

print(func2(input_list))