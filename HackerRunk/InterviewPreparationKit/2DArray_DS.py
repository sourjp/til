#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the hourglassSum function below.
def hourglassSum(arr):
    ans = float('-inf')
    for i in range(6 - 2):
        for j in range(6 - 2):
            sum = 0
            sum += arr[i][j]
            sum += arr[i][j + 1]
            sum += arr[i][j + 2]
            sum += arr[i + 1][j + 1]
            sum += arr[i + 2][j]
            sum += arr[i + 2][j + 1]
            sum += arr[i + 2][j + 2]
            ans = max(ans, sum)
    return ans

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr = []

    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))

    result = hourglassSum(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
