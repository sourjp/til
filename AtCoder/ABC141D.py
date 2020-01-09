import heapq

n, m = map(int, input().split())
input_list = list(map(int, input().split()))

input_list = [-x for x in input_list]

heapq.heapify(input_list)
discount_element = heapq.heappop(input_list)

i = 0
while i < m:
    discount_element = -(-(discount_element) // 2)
    heapq.heappush(input_list, discount_element)
    discount_element = heapq.heappop(input_list)
    i += 1

heapq.heappush(input_list, discount_element)

print(-(sum(input_list)))

