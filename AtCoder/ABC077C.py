n = int(input())
input_list = list(map(int, input().split()))
ans_list = input_list[::-2] + input_list[n%2::2]
print(*ans_list)

''' TLE
n = int(input())
input_list = list(map(int, input().split()))
q = []

for i in input_list:
    if i % 2 == 1:
        q.append(i)
    else:
        q.insert(0, i)

print(' '.join(map(str, q)))
'''

''' TLE
def operation(i, ans_list) -> list:
    ans_list.append(i)
    ans_list.reverse()

    return ans_list

n = int(input())
input_list = list(map(str, input().split()))
ans_list = []

for i in input_list:
    operation(i, ans_list)

print(' '.join(ans_list))
'''