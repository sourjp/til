H, W = map(int, input().split())

ans_list = []
i = 0

while i < H:
    input_list = input()
    ans_list.append(input_list)
    ans_list.append(input_list)
    i += 1

for _ in ans_list:
    print(_)