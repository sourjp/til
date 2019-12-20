a = int(input())
b = int(input())
c = int(input())
x = int(input())

cnt = 0
for i in range(a+1):
    for j in range(b+1):
        cc = x - i * 500 - j * 100

        if cc%50 == 0 and 0 <= cc//50 <= c:
            cnt += 1

print(cnt)