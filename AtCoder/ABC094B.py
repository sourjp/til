n, m, x = map(int, input().split())
input_list = list(map(int, input().split()))

left = 0
right = 0
for i in input_list:
    if i < x: left += 1
    elif i > x: right += 1

print(min(left, right))