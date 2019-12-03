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