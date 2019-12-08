s = input()

n = len(s) // 2

words_left = s[:n]
words_right = s[n:]

count = 0
i = 0
while i < n:
    j = i * -1 - 1
    if words_left[i] != words_right[j]:
        count += 1
    else:
        pass
    i += 1
    
print(count)