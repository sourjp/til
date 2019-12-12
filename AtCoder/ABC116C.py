n = int(input())
l = [int(i) for i in input().split()]

ans = 0
l.insert(0, 0)
for i in range(n):
    diff = l[i+1] - l[i] 
    if diff > 0:
        ans += diff
    else:
        pass

print(ans)