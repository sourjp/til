s = input()

acgt = ['A', 'C', 'G', 'T']
ans = 0
char_cnt = 0
for c in s:
    if c in acgt: char_cnt += 1
    else: char_cnt = 0
    ans = max(ans, char_cnt)

print(ans)