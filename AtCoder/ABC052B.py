N = int(input())
S = input()

ans = 0
x = 0

for order in S:
    if order == 'I':
        x += 1
    else:
        x -= 1
    ans = max(ans, x)

print(ans)