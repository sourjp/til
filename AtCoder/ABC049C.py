words = input()

checker = ['dream', 'dreamer', 'erase', 'eraser']
i = len(words)

while i > 0:
    if words[i-5:i] in checker: i -= 5
    elif words[i-6:i] in checker: i -= 6
    elif words[i-7:i] in checker: i -= 7
    else: break

print('YES' if i == 0 else 'NO')  