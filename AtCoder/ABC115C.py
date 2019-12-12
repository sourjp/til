n, k = map(int, input().split())

input_list = []
for i in range(n):
    input_list.append(int(input()))

input_list.sort()

ans = float('inf')
ans_index = 0
for i in range(n-k+1):
    h = input_list[i+k-1] - input_list[i]
    ans = min(ans, h)

print(ans)

    