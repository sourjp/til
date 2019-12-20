n, yen = map(int, input().split())

stop_calc = False
limit_tt = yen // 10000

for i in range(limit_tt+1):
    limit_ft = n - i

    for j in range(limit_ft+1):
        check = yen - (10000*i + 5000*j)

        if check%1000 == 0 and 0 <= check//1000 <= limit_ft - j:
            k = check // 1000

            if n == i+j+k:
                stop_calc = True
                break

    if stop_calc:
        break

if stop_calc: print(i, j, k)
else: print('-1 -1 -1')


'''
num, yen = map(int, input().split())

for i in range(num + 1):
    cal1 = yen
    if cal1 < 10000 * i:
        break
    else:
        cal1 -= 10000 * i
        
        for j in range(num + 1):
            cal2 = cal1
            if i + j > num:
                break
            elif cal2 < 5000 * j:
                break
            else:
                cal2 -= 5000 * j
                if cal2 % 1000 == 0:
                    z = cal2 // 1000
                    if i + j + z == num:
                        print(i, j, z)
                        exit()

print(-1, -1, -1)
'''