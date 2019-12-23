s = input()

leng = len(s) + 1

lr = [0] * leng
rl = [0] * leng

for i in range(1, leng):
    if s[i - 1] == '<':
        lr[i] = lr[i - 1] + 1

for i in range(leng - 1, 0, -1):
    if s[i - 1] == '>':
        rl[i - 1] = rl[i] + 1

ans_list = [max(rl[i], lr[i]) for i in range(leng)]

print(sum(ans_list))
