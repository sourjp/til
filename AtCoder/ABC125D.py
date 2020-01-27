n = int(input())
a = list(map(int, input().split()))
aa = []
cnt = 0
mval = float('inf')
for val in a:
    if val <= 0:
        cnt += 1
        mval = min(abs(val), mval)
    aa.append(abs(val))

if cnt % 2 == 0:
    print(sum(aa))
else:
    ans = 0
    for val in a:
        if val == mval: ans += mval
        ans += abs(val)
    print(ans)