import math

n = int(input())
traffic_list = [int(input()) for _ in range(5)]

print(4 + math.ceil(n/min(traffic_list)))