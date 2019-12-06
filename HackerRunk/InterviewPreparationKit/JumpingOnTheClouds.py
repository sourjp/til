#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the jumpingOnClouds function below.
def jumpingOnClouds(c):
    c.append(1)
    c.append(1)
    count_step = 0
    i = 0

    while i < n:
        if c[i+2] == 0:
            i += 2
        else:
            i += 1
        count_step +=1
    return count_step - 1

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    c = list(map(int, input().rstrip().split()))

    result = jumpingOnClouds(c)

    fptr.write(str(result) + '\n')

    fptr.close()
