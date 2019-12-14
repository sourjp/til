peoples, limit = map(int, input().split())
talls = [int(i) for i in input().split()]

count = 0
for tall in talls:
    if tall >= limit:
        count += 1

print(count)
