#!/bin/python3

import os
import sys

#
# Complete the timeConversion function below.
#
def timeConversion(s):
    hh, mm, ss = map(int, s[:-2].split(':'))
    if s[-2:] == 'AM':
        x = 0
    else:
        x = 1

    hh = hh % 12 + x * 12
    hh = str(hh).zfill(2)
    mm = str(mm).zfill(2)
    ss = str(ss).zfill(2)

    time = ('{}:{}:{}'.format(hh, mm, ss))
    return time


if __name__ == '__main__':
    f = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = timeConversion(s)

    f.write(result + '\n')

    f.close()
