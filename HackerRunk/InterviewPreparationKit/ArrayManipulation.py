#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the arrayManipulation function below.
def arrayManipulation(n, queries):
    queue_list = [int(0) for i in range(n + 1)]
    for data in queries:
        start, end, point = map(int, data)
        start -= 1
        queue_list[start] += point
        queue_list[end] -= point

    ans = 0
    plus = 0
    for val in queue_list:
        plus += val 
        ans = max(ans, plus)

    return ans

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nm = input().split()

    n = int(nm[0])

    m = int(nm[1])

    queries = []

    for _ in range(m):
        queries.append(list(map(int, input().rstrip().split())))

    result = arrayManipulation(n, queries)

    fptr.write(str(result) + '\n')

    fptr.close()


'''
def arrayManipulation(n, queries):
    que_list = [int(0) for i in range(n)]
    for start, end, point in queries:
        start -= 1
        que_list[start:end] = [que_list[i] + point for i in range(start,end)]
        print(que_list)
    return max(que_list)
'''

'''
def arrayManipulation(n, queries):
    que_dict = {}
    for start, end, point in queries:
        start -= 1
        for i in range(start, end):
            if i in que_dict:
                que_dict[i] += point
            else:
                que_dict[i] = point
    return max(que_dict.values())
'''
