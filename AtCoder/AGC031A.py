num = int(input())
words = input()
mod = 10**9+7

words_count = {}
for key in words:
    if key in words_count:
        words_count[key] += 1
    else:
        words_count[key] = 1

ans = 1
for key, val in words_count.items():
    ans *= (val + 1)

print((ans - 1) % mod)