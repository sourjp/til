n = int(input())
input_list = list(map(int, input().split()))

cnt = 0
keep = True
while keep:
    for i in range(n):
        if input_list[i] % 2 != 0:
            keep = False
            break
        
        input_list[i] //= 2
    if not keep : break
    cnt += 1

print(cnt)