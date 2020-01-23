n, m = map(int, input().split())
cards = sorted(list(map(int, input().split())))

changer = []
for i in range(m):
    p, c = map(int, input().split())
    changer.append((p, c))

changer.sort(key=lambda x: x[1])

cur = 0
while len(changer) and cur < n:
    p, c = changer.pop()
    i = cur
    while i < cur + p and cur + p < n:
        if cards[i] < c: cards[i] = c
        else: break
        i += 1
    cur = i
print(sum(cards))

'''
n, m = map(int, input().split())
cards = sorted(list(map(int, input().split())))
sum_cards = [cards[0]]
for i in range(1, n):
    sum_cards.append(cards[i-1] + cards[i])

changer = []
for i in range(m):
    p, c = map(int, input().split())
    gap = p*c - sum_cards[p-1]
    changer.append((p, c, gap))

changer.sort(key=lambda x: x[2])

#print(changer)
left = 0
saved = 0
i = 0
j = m-1
while j >= 0:
    p, c, _ = changer[j]
    if i + p >= n: p = n - i - 1
    #print(i, p)
    if cards[i+p] <= c:
        #print('hit')
        left += p*c
        saved = p
        i = p
    else:
        k = 0
        while cards[i+k] <= c:
            #print(i, k)
            left += c
            k += 1
            saved = i+k
        break

    j -= 1

#print(left, cards, saved)
print(left + sum(cards[saved:]))
'''