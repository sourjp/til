W, a, b = map(int, input().split())

if a < b:
    ans = a + W - b 
elif a > b:
    ans = a - b + W
else:
    ans = 0

if ans <= 0:
    print(0)
else:
    print(ans)