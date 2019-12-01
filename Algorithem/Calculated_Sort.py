'''
- INPUT:
7
2 5 1 3 2 3 0

- OUTPUT:
i: 0
index: [0, 2, 4, 6, 6, 7, 7]
output: [0, 0, 0, 0, 0, 0, 0]
i: 3
index: [0, 2, 4, 5, 6, 7, 7]
output: [0, 0, 0, 0, 0, 3, 0]
i: 2
index: [0, 2, 3, 5, 6, 7, 7]
output: [0, 0, 0, 2, 0, 3, 0]
i: 3
index: [0, 2, 3, 4, 6, 7, 7]
output: [0, 0, 0, 2, 3, 3, 0]
i: 1
index: [0, 1, 3, 4, 6, 7, 7]
output: [0, 1, 0, 2, 3, 3, 0]
i: 5
index: [0, 1, 3, 4, 6, 6, 7]
output: [0, 1, 0, 2, 3, 3, 5]
i: 2
index: [0, 1, 2, 4, 6, 6, 7]
output: [0, 1, 2, 2, 3, 3, 5]
[0, 1, 2, 2, 3, 3, 5]

'''

N = int(input())
input_list = [int(i) for i in input().split()]

index_list = [int(i*0) for i in range(N)]
output_list = [int(i*0) for i in range(N)]

for i in input_list:
    index_list[i] += 1

for i in range(1, N):
    index_list[i] += index_list[i - 1]

for i in input_list[::-1]:
    output_list[index_list[i] - 1] = i
    index_list[i] -= 1
    print('i:', i)
    print('index:', index_list)
    print('output:', output_list)

print(output_list)