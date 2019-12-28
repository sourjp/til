abc = sorted(list(map(int, input().split())))

first = abc[2] - abc[0]
second = abc[2] - abc[1]

cnt = 0

if first % 2 == 0 and second % 2 == 0:
    cnt += first//2 + second//2

elif (first % 2 == 1 and second % 2 == 0) or (first % 2 == 0 and second % 2 == 1):
    cnt += first//2 + second//2 + 2

else:
    cnt += first//2 + second//2 + 1

print(cnt)