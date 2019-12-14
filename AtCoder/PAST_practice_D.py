qube = input()

zero_count = qube.count('0')
one_count = qube.count('1')

ans = min(zero_count, one_count)

print(ans * 2)

