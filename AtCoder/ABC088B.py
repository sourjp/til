n = int(input())
cards = sorted(list(map(int, input().split())), reverse=True) 

ans = 0
for i in range(n):
    if i%2 == 0:
        ans += cards[i]
    else:
        ans -= cards[i]

print(ans)

