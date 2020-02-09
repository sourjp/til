n = int(input())
k = int(input())

ans = 0 
if k == 1:
    if n < 10: ans = n
    else: ans = 9 + n // 10

elif k == 2:
    if n < 10: ans = 0
    elif n < 100: 

print(ans)