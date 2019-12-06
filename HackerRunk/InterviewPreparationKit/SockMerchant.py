#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the sockMerchant function below.
def sockMerchant(n, ar):
    count_socks = {}
    for key in ar:
        if key in count_socks:
            count_socks[key] += 1
        else:
            count_socks[key] = 1

    count = 0
    for key, val in count_socks.items():
        while val - 2 >= 0:
            count += 1
            val -= 2
    
    return count

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    ar = list(map(int, input().rstrip().split()))

    result = sockMerchant(n, ar)

    fptr.write(str(result) + '\n')

    fptr.close()

