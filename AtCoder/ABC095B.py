n, x = map(int, input().split())
input_list = [int(input()) for _ in range(n)]

cnt = (x-sum(input_list)) // min(input_list)
print(cnt + n)