import heapq

n, m = map(int, input().split())
input_list = list(map(int, input().split()))

heapq._heapify_max(input_list)
print(heapq._heappop_max(input_list))
print(heapq._heappop_max(input_list))
