h = int(input())

cnt = 1
while h // 2 > 0:
    h //= 2
    cnt += 1

print(2 ** cnt - 1)