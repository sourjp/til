n = int(input())

i = 0
ab = []
while i < n:
    a, b = map(int, input().split())
    ab.append((a, b)) 
    i += 1

ab.sort(key=lambda x: x[1])

i = 0
ans = 'Yes'
days = 0
while i < n:
    days += ab[i][0]
    if days > ab[i][1]:
        ans = 'No'
        break
    i += 1
print(ans)