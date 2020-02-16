n = int(input())
memo = {}

for _ in range(n):
    s = input()
    if s in memo: memo[s] += 1
    else: memo[s] = 1

memo = sorted(memo.items(), key=lambda x:x[1], reverse=True)
mn = memo[0][1]

alist = []
for val in memo:
    a, b = val
    if b == mn: alist.append(a)
    else: break

alist.sort()
for ans in alist:
    print(ans)