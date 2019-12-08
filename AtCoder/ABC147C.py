#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the miniMaxSum function below.
def miniMaxSum(arr):
    arr.sort()
    n = len(arr)
    mini = sum(arr[:n-1]) 
    maxi = sum(arr[1:])

    print(mini, maxi)

if __name__ == '__main__':
    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)
