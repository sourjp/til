'''
- INPUT:
12
13 19 9 5 12 8 7 4 21 2 6 11

- OUTPUT:
[] 2 [13, 19, 9, 5, 12, 8, 7, 4, 21, 6, 11]
[] 4 [13, 19, 9, 5, 12, 8, 7, 21, 6, 11]
[13, 19, 9, 5, 12, 8, 7, 6, 11] 21 []
[13, 9, 5, 12, 8, 7, 6, 11] 19 []
[9, 5, 8, 7, 6] 11 [13, 12]
[] 12 [13]
[5, 6] 7 [9, 8]
[8] 9 []
[5] 6 []
[2, 4, 5, 6, 7, 8, 9, 11, 12, 13, 19, 21]

'''
import random

N = int(input())
input_list = [int(i) for i in input().split()]

def QuickSort(input_list):
    high_list = []
    low_list = []
    if len(input_list) <= 1:
        return input_list
    pivot = random.choice(input_list)
    for a in range(len(input_list)):
        if pivot < input_list[a]:
            high_list.append(input_list[a])
        elif pivot > input_list[a]:
            low_list.append(input_list[a])
    print(low_list, pivot, high_list)
    high_list = QuickSort(high_list)
    low_list = QuickSort(low_list)
    return low_list + [pivot] + high_list

if __name__ == '__main__':
    print(QuickSort(input_list))
