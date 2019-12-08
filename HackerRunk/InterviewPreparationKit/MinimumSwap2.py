#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the minimumSwaps function below.
def minimumSwaps(arr):
    ''' Swap Loop
    arr[i]で取得した値が、評価したいindexと異なれば、本来のindexも異なるはずなのでswapを続ける
    そして欲しい値が出るまでloopをすれば、他のindexもsortされるので無駄なカウントにならない

    1 [0, 2, 4, 1, 3, 5, 7]
    1 [0, 4, 2, 1, 3, 5, 7] c
    1 [0, 3, 2, 1, 4, 5, 7] c
    1 [0, 1, 2, 3, 4, 5, 7] c
    2 [0, 1, 2, 3, 4, 5, 7]
    3 [0, 1, 2, 3, 4, 5, 7]
    4 [0, 1, 2, 3, 4, 5, 7]
    5 [0, 1, 2, 3, 4, 5, 7]
    6 [0, 1, 2, 3, 4, 5, 7]
    '''
    swaps = 0
    i = 0
    while i < n - 1:
        if arr[i] != i + 1:
            tmp = arr[i]
            arr[i], arr[tmp - 1] = arr[tmp - 1], arr[i]
            swaps += 1
        else:
            i += 1
    return swaps

    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    res = minimumSwaps(arr)

    fptr.write(str(res) + '\n')

    fptr.close()
