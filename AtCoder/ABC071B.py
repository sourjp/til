s = input()

letters = list(map(chr, range(97, 123)))
ans = sorted(set(letters) - set(s))

print(ans[0] if ans else 'None')