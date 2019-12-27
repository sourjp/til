n = int(input())
input_list = [int(input()) for _ in range(n)]

input_set = sorted(set(input_list))
d = {}

for i, data in enumerate(input_set):
    d[data] = i

for k in input_list:
    print(d[k])
