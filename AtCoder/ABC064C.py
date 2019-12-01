N = int(input())
A = [int(i) for i in input().split()]

def CheckColor(a, count):
    if 1 <= a and a <= 399:
        count[0] += 1
    elif 400 <= a and a <= 799:
        count[1] += 1
    elif 800 <= a and a <= 1199:
        count[2] += 1
    elif 1200 <= a and a <= 1599:
        count[3] += 1
    elif 1600 <= a and a <= 1999:
        count[4] += 1
    elif 2000 <= a and a <= 2399:
        count[5] += 1
    elif 2400 <= a and a <= 2799:
        count[6] += 1
    elif 2800 <= a and a <= 3199:
        count[7] += 1
    else:
        count[8] += 1

ans = 0
count = [0 for _ in range(9)]

for a in A:
    CheckColor(a, count)

for c in count:
    if c != 0:
        ans += 1

print(max(ans, 1), ans + count[8])