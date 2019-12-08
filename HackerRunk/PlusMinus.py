#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the plusMinus function below.
def plusMinus(arr):
    positive = 0
    negative = 0
    zero = 0
    for i in arr:
        if i > 0:
            positive += 1
        elif i < 0:
            negative += 1
        else:
            zero += 1
    
    po = round(positive / n, 6)
    ne = round(negative / n, 6)
    ze = round(zero / n, 6)
    print('{0:.6f}'.format(po))
    print('{0:.6f}'.format(ne))
    print('{0:.6f}'.format(ze))

if __name__ == '__main__':
    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
