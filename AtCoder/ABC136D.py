s = input() + 'R'

ans = [0 for _ in range(len(s)-1)]
cnt = 0
i = 0
while i < len(s)-1:
    cnt += 1
    if s[i] == 'R' and s[i+1] == 'L':
        ri = i
        li = i+1

    if s[i] == 'L' and s[i+1] == 'R':
        if cnt % 2 == 0:
            rval = cnt // 2
            lval = cnt //2
        
        else:
            if (i-ri) % 2 == 0:
                rval = cnt // 2 + 1
                lval = cnt // 2
            else:
                rval = cnt // 2
                lval = cnt // 2 + 1

        ans[ri] = rval
        ans[li] = lval
        cnt = 0

    i += 1

print(*ans)
