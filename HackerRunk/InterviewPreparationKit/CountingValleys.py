#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the countingValleys function below.
def countingValleys(n, s):
    count = 0
    valley = 0
    enter_valley = False
    for word in s:
        if word == 'U':
            count += 1
        else:
            count -= 1
        if enter_valley == False:
            if 0 > count:
                enter_valley = True
                valley += 1
        else:
            if 0 <= count:
                enter_valley = False
    return valley

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    s = input()

    result = countingValleys(n, s)

    fptr.write(str(result) + '\n')

    fptr.close()
