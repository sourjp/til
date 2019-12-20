n = int(input())

while n <= 999:
    if n%111 == 0:
        break
    n += 1

print(n)