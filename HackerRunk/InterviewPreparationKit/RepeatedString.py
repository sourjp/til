#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the repeatedString function below.
def repeatedString(s, n):
    a_count = 0
    for word in s:
        if word == 'a':
            a_count += 1

    div = n // len(s)
    a_count *= div

    rem = n % len(s)
    
    for word in s[:rem]:
        if word == 'a':
            a_count += 1
    
    return a_count

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    n = int(input())

    result = repeatedString(s, n)

    fptr.write(str(result) + '\n')

    fptr.close()
