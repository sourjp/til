#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the checkMagazine function below.
def checkMagazine(magazine, note):
    magazine.sort()
    note.sort()

    j = -1
    for i in range(len(note)):
        j += 1
        if j >= len(magazine):
            return print('No')

        if note[i] != magazine[j]:
            while note[i] != magazine[j]:
                if j >= len(magazine) - 1:
                    return print('No')
                j += 1
        
    return print('Yes')

                

if __name__ == '__main__':
    mn = input().split()

    m = int(mn[0])

    n = int(mn[1])

    magazine = input().rstrip().split()

    note = input().rstrip().split()

    checkMagazine(magazine, note)
