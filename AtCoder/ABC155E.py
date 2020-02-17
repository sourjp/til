N = list(input())
n = [int(val) for val in reversed(N)] + [0]
ln = len(N)

ans = 0
for i in range(ln):
    if n[i] <= 4: a = n[i]
    elif n[i] == 5:
        if n[i+1] <= 4:
            a = n[i]
        else:
            a = 10 - n[i]
            n[i+1] += 1
    else:
        n[i+1] += 1
        a = 10 - n[i]
    ans += a

ans += n[ln]
print(ans)  
