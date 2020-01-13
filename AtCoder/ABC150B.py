n = int(input())
s = input()

i = 0
cnt = 0
while i+2 < n:
    if 'ABC' == s[i:i+3]:
        cnt += 1
    i += 1
print(cnt)