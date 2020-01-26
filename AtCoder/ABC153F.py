n, d, a = map(int, input().split())
bom = []

limit = 0
for _ in range(n):
    x, h = map(int, input().split())
    bom.append([x, h])
    limit = max(limit, x)

bom.sort(key=lambda x:x[0])

cnt = 0
left = 0
while left < n:
    #print(bom)
    if bom[left][1] > 0:
        right = bom[left][0]+2*d+1
        if bom[left][1] % a != 0: tmp = bom[left][1] // a + 1 
        else: tmp = bom[left][1] // a
        cnt += tmp
        i = left
        print(bom)
        if right > limit: right = limit
        while i < n and bom[i][0] <= right:
            #print('r', right, bom[i], i)
            bom[i][1] -= a * tmp
            i += 1
    left += 1
print(cnt)

