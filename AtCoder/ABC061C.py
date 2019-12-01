N, K = map(int, input().split())


input_dict = {}

for _ in range(N):
    a, b = map(int, input().split())
    if a in input_dict:
        input_dict[a] += b
    else:
        input_dict[a] = b

input_dict = sorted(input_dict.items(), key=lambda x:x[0])

for i in range(len(input_dict)):
    K -= input_dict[i][1]
    if K <= 0:
        print(input_dict[i][0])
        break