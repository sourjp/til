n = int(input())
A = list(map(int, input().split()))
mval = float('inf')
minus_cnt = 0
isZero = False
ans = 0

for a in A:
    if a < 0: minus_cnt += 1
    if a == 0: isZero
    mval = min(mval, abs(a))
    ans += abs(a)

if isZero or minus_cnt % 2 == 0: print(ans)
else: print(ans - mval*2)
