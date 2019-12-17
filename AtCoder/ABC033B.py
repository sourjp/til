n = int(input())

max_s = 0
max_p = 0
smry = 0
for i in range(n):
    s, p = input().split()
    smry += int(p)
    if max_p < int(p):
        max_p = int(p)
        max_s = s

get_half = smry // 2

if max_p > get_half:
    print(max_s)
else:
    print('atcoder')

