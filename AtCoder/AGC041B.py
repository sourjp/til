n, m, v, p = map(int, input().split())
scores = sorted(list(map(int, input().split())))

get_line = scores[-p]

cnt = 0
for i in range(n-p):
    if scores[i] + m < get_line:
        cnt += 1

print(n-cnt)
