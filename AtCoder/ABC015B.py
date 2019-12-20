import math

n = int(input())
data_list = map(int, input().split())

cal = 0
cnt = 0

for data in data_list:
    if data != 0:
        cnt += 1
        cal += data

print(math.ceil(cal/cnt))