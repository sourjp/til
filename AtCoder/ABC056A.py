a, b = map(str, input().split())

if a == 'H' and b == 'D' or a == 'D' and b == 'H':
    print('D')
else:
    print('H')