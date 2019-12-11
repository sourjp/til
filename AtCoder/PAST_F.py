def nCr(n, r):
    r = min(r, n-r)

    numerator = 1
    for i in range(n, n-r, -1):
        numerator *= i

    denominator = 1
    for i in range(r, 1, -1):
        denominator *= i

    return numerator // denominator

s_num = int(input())

tmp_list = []
words_list = []
for i in range(s_num):
    word2num = 0
    tmp_list = [w for w in input()]
    tmp_list.sort()
    tmp = ''.join(tmp_list)
    words_list.append(tmp)

words_list.sort()
words_list.append('end')
ans = 0
count = 1
for i in range(s_num):
    if words_list[i] != words_list[i + 1]:
        if count > 1:
            ans += nCr(count, 2)
        count = 1
    else:
        count += 1

print(ans)
