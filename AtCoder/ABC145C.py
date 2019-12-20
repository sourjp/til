import itertools
import math

def rt(x1, x2, y1, y2):
    cal = (x2-x1)**2 + (y2-y1)**2
    return math.sqrt(cal)

n = int(input())
patern = list(itertools.permutations(range(1,n+1), n))

input_list = []
for _ in range(1, n+1):
    x, y = map(int, input().split())
    input_list.append([x, y])

cal = 0
for i in range(len(patern)):
    for j in range(n-1):
        index = patern[i][j]
        index_ad = patern[i][j+1]
        x1 = input_list[j][0]
        x2 = input_list[j+1][0]
        y1 = input_list[j][1]
        y2 = input_list[j+1][1]
        print(x1, x2, y1, y2)
        cal += rt(x1, x2, y1, y2)
        print('_:', _, 'j:', j, cal)

print(cal/len(patern))
